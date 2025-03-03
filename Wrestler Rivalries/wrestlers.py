# Author: Joseph D Tong
# Date: 11/5/2020
# Description: Takes data on wrestlers and their rivalries from an input file and determines whether the wrestlers can
# be placed in two opposing groups based on those rivalries. If so, prints a possible grouping.

import sys


class Vertex:
    """Represents a vertex on a graph."""
    def __init__(self):
        self.color = "white"
        self.adj = []
        self.start = 0
        self.finish = 0

    def set_adj(self, vertex):
        self.adj.append(vertex)

    def set_start(self, time):
        self.start = time

    def set_finish(self, time):
        self.finish = time

    def set_color(self, color):
        self.color = color

    def get_finish(self):
        return self.finish

    def get_color(self):
        return self.color

    def get_adj(self):
        return self.adj


def dfs_visit(graph, vertex, time):
    """Recursive portion of depth_first_search."""
    time += 1
    graph[vertex].set_start(time)
    graph[vertex].set_color('black')  # Not necessary to track gray vertices for this problem
    for rival in graph[vertex].get_adj():
        if graph[rival].get_color() == 'white':
            time = dfs_visit(graph, rival, time)  # time must be returned to track it between recursive calls
    time += 1
    graph[vertex].set_finish(time)
    return time


def depth_first_search(graph):
    """
    Performs a depth-first search of a graph, setting the color, start time, and finish time of each vertex as it is
    discovered and fully searched.
    """
    time = 0
    for vertex in graph:
        if graph[vertex].get_color() == 'white':
            time = dfs_visit(graph, vertex, time)


def categorize_wrestlers(wrestlers, rivalries):
    """
    Takes a list of wrestler names and a list of rivalries and determines whether the wrestlers can be sorted into two
    opposing groups based on the rivalries.
    """
    graph = {}

    # Create a vertex on the graph for each wrestler
    for wrestler in wrestlers:
        vertex = Vertex()
        graph[wrestler] = vertex

    # Add both wrestlers in each rivalry to each other's adjacency list
    for rivalry in rivalries:
        graph[rivalry[0]].set_adj(rivalry[1])
        graph[rivalry[1]].set_adj(rivalry[0])

    # Perform depth-first search on the graph, recording finishing times of each vertex.
    depth_first_search(graph)

    bbfs = []
    heels = []
    for vertex in graph:

        # Group the wrestlers based on whether finishing time was even or odd
        if graph[vertex].get_finish() % 2 == 0:
            bbfs.append(vertex)
        else:
            heels.append(vertex)

        # If two adjacent vertices (rival wrestlers) have both have odd or both have even finishing times, the wrestlers
        # cannot be properly grouped
        for rival in graph[vertex].get_adj():
            if (graph[vertex].get_finish() + graph[rival].get_finish()) % 2 == 0:
                print("Impossible")
                return

    # Print the groupings of the wrestlers
    bbfs_str = "Babyfaces: "
    heels_str = "Heels: "
    for wrestler in bbfs:
        bbfs_str += wrestler
        bbfs_str += " "
    for wrestler in heels:
        heels_str += wrestler
        heels_str += " "
    print("Yes Possible")
    print(bbfs_str)
    print(heels_str)


def process_file(input_file):
    """Reads data on wrestlers and rivalries from an input file and uses it to call categorize_wrestlers."""
    with open(input_file) as source:
        wrestlers = []
        rivalries = []

        # Get the number of wrestlers from the file
        num_wrestlers = int(source.readline())

        # Append the name of each wrestler to the list of wrestlers
        for i in range(0, num_wrestlers):
            wrestlers.append(source.readline()[0:-1])

        # Get the number of rivalries from the file
        num_rivalries = int(source.readline())

        # Create a list of the two wrestler's names for each rivalry and append it to the list of rivalries
        for i in range(0, num_rivalries):
            rivalry = []
            rivalry_str = source.readline()
            rival = ''
            for char in rivalry_str:
                if char == ' ':
                    rivalry.append(rival)
                    rival = ''
                rival += char
            rivalry.append(rival[1:-1])
            rivalries.append(rivalry)

        categorize_wrestlers(wrestlers, rivalries)


def main():
    process_file(sys.argv[1])


if __name__ == "__main__":
    main()
