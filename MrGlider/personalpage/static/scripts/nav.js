const dev_domen = 'http://localhost:8000'
const domen = 'https://maskim-al.ru'
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
        for (let item of modalWindows) {
            item.appendChild(newItem);
            item.style.display = 'block';
        }
    }
    else {
        for (let item of modalWindows) {
            item.style.display = 'none';
            item.firstChild.remove();
        }
    }
}

function GetSkills() {
    (async() => {
        GetWindow('skills');
        const targetElement = document.getElementById('skills');
        const response = await fetch(`${dev_domen}/skills/`);
        let skills = response.body;
        console.log(skills);
        for (const group of skills) {
            targetElement.innerHTML = `<h1>${group[0].name}</h1>`;
            group.forEach((skill) => {
                let header = document.createElement('h3');
                header.innerText = skill.title;
                targetElement.appendChild(header);
                let body = document.createElement('span');
                body.innerText = skill.description;
                targetElement.appendChild(body);
            })
        }
    })();
}

function  GetCalendarWindow() {
    let modalWindows = document.getElementsByClassName('modal-window active');
    if (!document.getElementById('category')) {
        let newItem = CreateContainer('calendar');
        for (let item of modalWindows) {
            item.appendChild(newItem);
            item.style.display = 'block';
        }
        GetCalendar();
        GetData();
    }
    else {
        for (let item of modalWindows) {
            item.style.display = 'none';
            item.firstChild.remove();
        }
    }
}
