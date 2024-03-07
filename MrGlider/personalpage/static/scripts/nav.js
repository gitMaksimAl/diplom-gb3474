function CreateContainer(id) {
    let newItem = document.createElement("div");
    newItem.id = 'category';
    let innerItem = document.createElement("div");
    innerItem.id = id;
    newItem.appendChild(innerItem);
    return newItem;
}

function GetWindow(name) {
    let modalWindows = document.getElementsByClassName('modal-window active');
    if (!document.getElementById('category')) {
        let newItem = CreateContainer(name);
        for (let window of modalWindows) {
            window.appendChild(newItem);
            window.style.display = 'block';
        }
    }
    else {
        for (let window of modalWindows) {
            window.style.display = 'none';
            window.firstChild.remove();
        }
    }
}

function  GetCalendarWindow() {
    let modalWindows = document.getElementsByClassName('modal-window active');
    if (!document.getElementById('category')) {
        let newItem = CreateContainer('calendar');
        for (let window of modalWindows) {
            window.appendChild(newItem);
            window.style.display = 'block';
        }
        GetCalendar();
        GetData();
    }
    else {
        for (let window of modalWindows) {
            window.style.display = 'none';
            window.firstChild.remove();
        }
    }
}
