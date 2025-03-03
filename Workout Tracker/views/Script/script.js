document.addEventListener('DOMContentLoaded', bindButtons);

function addRow(tableBody, rowData, index){
    var newRow = document.createElement("tr");
    newRow.id = rowData[index].id

    var nameCell = document.createElement("td");
    nameCell.textContent = rowData[index].name;
    newRow.appendChild(nameCell);

    var repsCell = document.createElement("td");
    repsCell.textContent = rowData[index].reps;
    newRow.appendChild(repsCell);

    var weightCell = document.createElement("td");
    weightCell.textContent = rowData[index].weight;
    newRow.appendChild(weightCell);

    var lbsCell = document.createElement("td");
    if (rowData[index].lbs) {
        lbsCell.textContent = "lbs";
    } else {
        lbsCell.textContent = "kgs";
    }
    newRow.appendChild(lbsCell);

    var dateCell = document.createElement("td");
    var retDate = rowData[index].date;
    var year = retDate.slice(0, 4);
    var month = retDate.slice(5, 7);
    var day = retDate.slice(8, 10);
    dateCell.textContent = month + "-" + day + "-" + year;
    newRow.appendChild(dateCell)

    var editCell = document.createElement("td");
    var editButton = document.createElement("input");
    editButton.type = "submit";
    editButton.value = "Edit";
    editButton.addEventListener('click', function(event){

        var editName = document.createElement("input");
        editName.type = "text";
        editName.maxLength = "255";
        editName.value = nameCell.textContent;
        nameCell.textContent = "";
        nameCell.appendChild(editName);

        var editReps = document.createElement("input");
        editReps.type = "number";
        editReps.value = repsCell.textContent;
        repsCell.textContent = "";
        repsCell.appendChild(editReps);

        var editWeight = document.createElement("input");
        editWeight.type = "number";
        editWeight.value = weightCell.textContent;
        weightCell.textContent = "";
        weightCell.appendChild(editWeight);

        var editLbs = document.createElement("select");
        var lbsOpt = document.createElement("option");
        lbsOpt.value = 1;
        lbsOpt.textContent = "lbs";
        var kgsOpt = document.createElement("option");
        kgsOpt.value = 0;
        kgsOpt.textContent = "kgs"
        editLbs.appendChild(lbsOpt);
        editLbs.appendChild(kgsOpt);
        if (lbsCell.textContent == "lbs") {
            lbsOpt.selected = true;
            kgsOpt.selected = false;
        } else {
            lbsOpt.selected = false;
            kgsOpt.selected = true;
        }
        lbsCell.textContent = "";
        lbsCell.appendChild(editLbs);

        var editDate = document.createElement("input");
        editDate.type = "date";
        editDate.value = dateCell.textContent.slice(6, 10) + "-" +
        dateCell.textContent.slice(0, 2) + "-" +
        dateCell.textContent.slice(3, 5);
        dateCell.textContent = "";
        dateCell.appendChild(editDate);

        var saveButton = document.createElement("input");
        saveButton.type = "submit";
        saveButton.value = "Save";
        saveButton.addEventListener('click', function(event){
            var req = new XMLHttpRequest();

            var payload = {id:null, name:null, reps:null, weight:null, lbs:null, date:null};
            payload.id = newRow.id;
            payload.name = editName.value;
            payload.reps = editReps.value;
            payload.weight = editWeight.value;
            payload.lbs = editLbs.value;
            payload.date = editDate.value;

            req.open('POST', '/update', true);
            req.setRequestHeader('Content-Type', 'application/json');

            req.addEventListener('load', function(){
                if(req.status >= 200 && req.status < 400){
                    buildTable();
                } else {
                    console.log("Error! " + req.statusText);
                }
            });
            req.send(JSON.stringify(payload));
            event.preventDefault();
        });
        editCell.appendChild(saveButton);
        editCell.removeChild(editButton);
    });
    editCell.appendChild(editButton);
    newRow.appendChild(editCell);

    var delCell = document.createElement("td");
    var delButton = document.createElement("input");
    delButton.type = "submit";
    delButton.value = "Delete";
    delButton.addEventListener('click', function(event){
        var req = new XMLHttpRequest();

        var payload = {id: null};
        payload.id = newRow.id

        req.open('POST', '/del', true);
        req.setRequestHeader('Content-Type', 'application/json');

        req.addEventListener('load', function(){
            if(req.status >= 200 && req.status < 400){
                var tableBody = document.getElementById("tableData");
                tableBody.removeChild(newRow);
            } else {
                console.log("Error! " + req.statusText);
            }
        });
        req.send(JSON.stringify(payload));
        event.preventDefault();
    });
    delCell.appendChild(delButton);
    newRow.appendChild(delCell);

    tableBody.appendChild(newRow);
}

function buildTable(){
    var req = new XMLHttpRequest();
    req.open('GET', '/fill', true);
    req.setRequestHeader('Content-Type', 'application/json');
    req.addEventListener('load', function(){
        if(req.status >= 200 && req.status < 400){

            var response = JSON.parse(req.responseText);
            var tableData = JSON.parse(response.tableData);
            var tableBody = document.getElementById("tableData");

            while (tableBody.firstChild) {
                tableBody.removeChild(tableBody.firstChild);
            }

            for (var i = 0; i < tableData.length; i++){
                addRow(tableBody, tableData, i);
            }
        } else {
            console.log("Error! " + req.statusText);
        }
    });
    req.send(null);
    event.preventDefault();
}

function bindButtons(){

    buildTable();

    document.getElementById('insertButton').addEventListener('click', function(event){
        var req = new XMLHttpRequest();

        var payload = {name:null, reps:null, weight:null, lbs:null, date:null};
        payload.name = document.getElementById('name').value;
        payload.reps = document.getElementById('reps').value;
        payload.weight = document.getElementById('weight').value;
        payload.lbs = document.getElementById('lbs').value;
        payload.date = document.getElementById('date').value;

        req.open('POST', '/', true);
        req.setRequestHeader('Content-Type', 'application/json');

        req.addEventListener('load', function(){
            if(req.status >= 200 && req.status < 400){
                var response = JSON.parse(req.responseText);
                var errOut = document.getElementById("errMsg");

                if (response.errMsg){
                    errOut.textContent = response.errMsg;
                } else {
                    errOut.textContent = "";
                    var tableData = JSON.parse(response.tableData);
                    var tableBody = document.getElementById("tableData");
                    addRow(tableBody, tableData, 0);
                }
            } else {
                console.log("Error! " + req.statusText);
            }
        });
        req.send(JSON.stringify(payload));
        event.preventDefault();
    });
}