//Author: Joseph Tong
//Date: 1/31/21
//CS 344 Program 3 (Portfolio Project)

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <signal.h>
#include <string.h>

_Bool fgOnlyMode = 0;

int expandVar(char* inputStr, char* command) {
    int count = 0;

    for (int i = 0; i < strlen(inputStr); i++) {

        //Return error if command is too long
        if (count >= 2048) {
            return -1;
        }

        //Check for occurances of "$$"
        //If "$$" is not found, add the character to the command string
        if (!(inputStr[i] == '$' && inputStr[i + 1] == '$')) {
            command[count] = inputStr[i];
            count++;
        }

        //If "$$" is found, get pid, convert to string and concat with command
        else {
            char* pid = malloc(8 * sizeof(char));
            sprintf(pid, "%d", getpid());

            //Return error if command is too long
            if (count + strlen(pid) >= 2048) {
                return -1;
            }

            strcat(&command[count], pid);

            //Add the number of characters in pid to count to update command index
            count = count + strlen(pid);

            free(pid);

            //Skip second dollar sign
            i++;
        }
    }

    return 0;
}

int changeDir(char* dirName) {
    //Change pwd to user specified location or HOME if none provided
    if (dirName != NULL) {
        return chdir(dirName);
    }
    else {
        return chdir(getenv("HOME"));
    }
}

void showStat(pid_t pidNum, int statNum) {
    //Checks the status given by waitpid() and prints a status message
    if (WIFEXITED(statNum)) {
        printf("\nBackground PID %d has exited with exit value %d", pidNum, WEXITSTATUS(statNum));
        fflush(stdout);
    }
    else {
        printf("\nBackground PID %d has terminated due to signal %d", pidNum, WTERMSIG(statNum));
        fflush(stdout);
    }
}

void sigtstpHandler(int sigNum) {
    //Reverse the value of global variable fgOnlyMode and print info message
    if (!fgOnlyMode) {
        fgOnlyMode = 1;
        write(STDOUT_FILENO, "\nEntering foreground-only mode (& is now ignored)\n", 50);
        fflush(stdout);
    }
    else {
        fgOnlyMode = 0;
        write(STDOUT_FILENO, "\nExiting foreground-only mode\n", 30);
        fflush(stdout);
    }
}

int main() {

    //SIGTSTP mask. For blocking SIGTSTP while fg child processes run
    sigset_t sigtstpMask;
    sigaddset(&sigtstpMask, SIGTSTP);

    //Ignore SIGINT in parent and background child processes
    struct sigaction sigintAction = { 0 };
    sigintAction.sa_handler = SIG_IGN;
    sigemptyset(&sigintAction.sa_mask); //Do not block other signals
    sigintAction.sa_flags = 0;
    sigaction(SIGINT, &sigintAction, NULL);

    //Call sigtstpHandler upon receiving SIGTSTP in parent process
    struct sigaction sigtstpAction = { 0 };
    sigtstpAction.sa_handler = &sigtstpHandler;
    sigfillset(&sigtstpAction.sa_mask); //Block all signals while handler runs
    sigtstpAction.sa_flags = 0;
    sigaction(SIGTSTP, &sigtstpAction, NULL);

    pid_t children[256] = { 0 }; //Array of child process pid's
    int childCount = 0; //Count of child processes
    int childStat = 0; //Exit status of last foreground child process
    char* userInput = NULL;
    size_t length = 0;
    ssize_t nread;

    while (1) {

        //Poll background processes
        int bkgStat;
        for (int i = 0; i < 256; i++) {
            if (children[i] != 0) {

                //Check if background process has completed
                int result = waitpid(children[i], &bkgStat, WNOHANG);
                if (result != 0) {

                    //Print status of completed process and remove from children array
                    showStat(children[i], bkgStat);
                    childCount--;
                    children[i] = 0;
                }

            }
        }

        //Print prompt and get user command
        printf("\n: ");
        fflush(stdout);
        nread = getline(&userInput, &length, stdin);

        //Handle getline error
        if (nread == -1) {
            clearerr(stdin);
            continue;
        }

        userInput[strlen(userInput) - 1] = '\0'; //Remove unnecessary newline

        //Expand any $$
        char* command = malloc(2049 * sizeof(char));
        memset(command, '\0', 2049);
        int tooLong = expandVar(userInput, command);

        //Reprompt if command is >2048 characters
        if (tooLong == -1) {
            printf("\nError: The command was too long (limit 2048 characters).");
            fflush(stdout);
            free(command);
            continue;
        }

        //Check for " &" and set background flag if present
        _Bool background = 0;

        if (strcmp(&command[strlen(command) - 2], " &") == 0) {

            //Do not set background flag when fgOnlyMode is set
            if (!fgOnlyMode) {
                background = 1;
            }

            command[strlen(command) - 1] = '\0';
        }

        //Get the basic command
        char* savePointer;
        char* cmd = strtok_r(command, " \n", &savePointer);

        //If comment or no command entered, prompt user again
        if (cmd == NULL || cmd[0] == '#') {
            free(command);
            continue;
        }

        if (strcmp(cmd, "exit") == 0) {

            //Iterate through children, terminating active bg processes
            for (int i = 0; i < 256; i++) {
                if (children[i] != 0) {
                    kill(children[i], SIGTERM);
                    waitpid(children[i], &childStat, WNOHANG);
                }
            }
            free(command);
            break;
        }

        else if (strcmp(cmd, "cd") == 0) {
            char* dirName = strtok_r(NULL, " ", &savePointer);
            int errorNum = changeDir(dirName);

            //Check if pwd updated correctly, print error if not
            if (errorNum != 0) {
                perror(dirName);
                fflush(stderr);
            }
            free(command);
        }

        else if (strcmp(cmd, "status") == 0) {
            //Print status message based on value returned by waitpid for last foreground process
            if (WIFEXITED(childStat)) {
                printf("Exit value %d\n", WEXITSTATUS(childStat));
                fflush(stdout);
            }
            else {
                printf("Signal number %d\n", WTERMSIG(childStat));
                fflush(stdout);
            }
            free(command);
            continue;
        }

        else {
            //Get command arguments
            char* argList[513] = { '\0' };
            char* inputFile = malloc(256 * sizeof(char));
            char* outputFile = malloc(256 * sizeof(char));
            memset(inputFile, '\0', 256);
            memset(outputFile, '\0', 256);

            //Add the address of the base command to argList for exec
            argList[0] = cmd;

            char* token = strtok_r(NULL, " ", &savePointer);

            int argCount = 1;

            while (token != NULL) {

                if (argCount >= 512) {
                    break;
                }

                //Check for input redirection
                if (strcmp(token, "<") == 0) {
                    token = strtok_r(NULL, " ", &savePointer);
                    strcpy(inputFile, token);
                }

                //Check for output redirection
                else if (strcmp(token, ">") == 0) {
                    token = strtok_r(NULL, " ", &savePointer);
                    strcpy(outputFile, token);
                }

                //Add the argument to argList
                else {
                    argList[argCount] = token;
                    argCount++;
                }

                token = strtok_r(NULL, " ", &savePointer);
            }

            if (argCount >= 512 && token != NULL) {
                printf("\nToo many arguments (limit 512).");
                fflush(stdout);
                free(command);
                continue;
            }

            //Create child process only if there are <255 child processes
            pid_t childPID;
            if (childCount < 255) {
                childPID = fork();
            }
            else {
                printf("\nToo many child processes.");
                fflush(stdout);
                free(inputFile);
                free(outputFile);
                free(command);
                continue;
            }

            //Check if fork created correctly
            if (childPID == -1) {
                perror("Failed to create a new process");
                fflush(stderr);
                free(inputFile);
                free(outputFile);
                free(command);
                continue;
            }

            //Check if child process
            else if (childPID == 0) {

                //Ignore SIGTSTP in child processes
                sigtstpAction.sa_handler = SIG_IGN;
                sigemptyset(&sigtstpAction.sa_mask); //Don't block signals
                sigaction(SIGTSTP, &sigtstpAction, NULL);

                int oldIn = STDIN_FILENO;
                int oldOut = STDOUT_FILENO;

                //Perform background process input/output redirection
                if (background) {

                    //Redirect input to /dev/null
                    int nullIn = open("/dev/null", O_RDONLY);
                    if (nullIn == -1) {
                        perror("Input file error");
                        fflush(stderr);
                        exit(1);
                    }

                    int dupVal = dup2(nullIn, oldIn);
                    if (dupVal == -1) {
                        perror("Input redirect failed");
                        fflush(stderr);
                        exit(2);
                    }

                    //Redirect output to /dev/null
                    int nullOut = open("/dev/null", O_WRONLY | O_CREAT | O_TRUNC, 0640);
                    if (nullOut == -1) {
                        perror("Output file error");
                        fflush(stderr);
                        exit(1);
                    }

                    dupVal = dup2(nullOut, oldOut);
                    if (dupVal == -1) {
                        perror("Output redirect failed");
                        fflush(stderr);
                        exit(2);
                    }
                }

                else {
                    //Stop ignoring SIGINT in foreground child process
                    sigintAction.sa_handler = SIG_DFL;
                    sigfillset(&sigintAction.sa_mask);
                    sigaction(SIGINT, &sigintAction, NULL);
                }

                //Perform user specified input/output redirection
                if (inputFile[0] != '\0') {

                    //Redirect input to inputFile
                    int inputFD = open(inputFile, O_RDONLY);
                    if (inputFD == -1) {
                        perror(inputFile);
                        fflush(stderr);
                        exit(1);
                    }

                    int dupVal = dup2(inputFD, oldIn);
                    if (dupVal == -1) {
                        perror("Input redirect failed");
                        fflush(stderr);
                        exit(2);
                    }
                }

                if (outputFile[0] != '\0') {

                    //Redirect output to outputFile
                    int outputFD = open(outputFile, O_WRONLY | O_CREAT | O_TRUNC, 0640);
                    if (outputFD == -1) {
                        perror(outputFile);
                        fflush(stderr);
                        exit(1);
                    }

                    int dupVal = dup2(outputFD, oldOut);
                    if (dupVal == -1) {
                        perror("Output redirect failed");
                        fflush(stderr);
                        exit(2);
                    }
                }

                free(inputFile);
                free(outputFile);

                //Execute new program
                execvp(cmd, argList);
                perror(cmd);
                fflush(stderr);
                free(command);
                exit(1);
            }

            //Parent process
            else {

                //Find empty slot in children array
                int index = 0;
                while (children[index] != 0) {
                    index++;
                }

                //Track child process
                children[index] = childPID;
                childCount++;

                //Wait for foreground process to complete
                if (!background) {
                    sigprocmask(SIG_BLOCK, &sigtstpMask, NULL); //Block SIGTSTP
                    waitpid(childPID, &childStat, 0);
                    sigprocmask(SIG_UNBLOCK, &sigtstpMask, NULL); //Unblock SIGTSTP
                    childCount--;
                    children[index] = 0;

                    //Print message if fg process was terminated by signal
                    if (WIFSIGNALED(childStat)) {
                        printf("\nForeground process with PID %d terminated by signal %d\n",
                            childPID, WTERMSIG(childStat));
                        fflush(stdout);
                    }
                }

                //Print PID of background process
                else {
                    printf("Started background process with PID %d\n", childPID);
                    fflush(stdout);
                }

                free(inputFile);
                free(outputFile);
                free(command);
            }
        }
    }

    free(userInput);
    return 0;
}