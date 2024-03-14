const devDomain = 'http://localhost:8000/'
const domain = 'https://maskim-al.ru/'


function CreateWindow(name) {
    let modalWindow = document.querySelector('.modal-window.active');
    if (modalWindow.firstChild && modalWindow.firstChild.id === name) {
        modalWindow.style.display = 'none';
        modalWindow.firstChild.remove();
        return null;
    }
    modalWindow.innerHTML = `<div id="${name}"></div>`;
    modalWindow.style.display = 'block';
    return modalWindow.firstChild;
}

function GetSkills() {
    let targetElement = CreateWindow('skills');
    if (targetElement) {
        (async () => {
            const response = await fetch(`${devDomain}skills/`);
            let skills = await response.json();
            for (const skill of skills) {
                let skillDiv = document.getElementById(skill.name);
                if (!skillDiv) {
                    skillDiv = document.createElement('ul');
                    skillDiv.id = skill.name;
                    targetElement.appendChild(skillDiv);
                }
                let li = document.createElement('li');
                li.innerHTML = `<h3>${skill.title}</h3><p>${skill.description}</p>`;
                skillDiv.appendChild(li);
            }
        })();
    }
}


function GetProjects() {
    let targetElement = CreateWindow('projects');
    if (targetElement) {
        (async() => {
            const response = await fetch(`${devDomain}projects/`);
            let projects = await response.json();
            for (const project of projects) {
                let projectDiv = document.getElementById(project.name);
                if (!projectDiv) {
                    projectDiv = document.createElement('ul');
                    projectDiv.id = project.name;
                    targetElement.appendChild(projectDiv);
                }
                let li = document.createElement('li');
                li.innerHTML = `<h3>${project.task}</h3><a>${project.website}</a>`;
                projectDiv.appendChild(li);
            }
        })();
    }
}


function GetContact() {
    let targetElement = CreateWindow('contact');
    if (targetElement) {

    }
}


function GetCerts() {
    let targetElement = CreateWindow('certificates');
    if (targetElement) {
        (async() => {
            const response = await fetch(`${devDomain}certificates/`);
            let certs = await response.json();
            for (const cert of certs) {
                let certDiv = document.getElementById(cert.publisher);
                if (!certDiv) {
                    certDiv = document.createElement('ul');
                    certDiv.id = cert.publisher;
                    targetElement.appendChild(certDiv);
                }
                let li = document.createElement('li');
                li.innerHTML = `<h3>${cert.title}</h3>`;
                certDiv.appendChild(li);
            }
        })();
    }
}


function GetContact() {
    let targetElement = CreateWindow('contact');
    if (targetElement) {
        (async () => {
            const response = await fetch(`${devDomain}contact/`);
            let form = await response.json();
            targetElement.appendChild(document.createElement('form'));
            targetElement.firstChild.innerHTML = form.form;
            targetElement.firstChild.action = `${devDomain}contact/`;
            targetElement.firstChild.method = 'post';
            // targetElement.firstChild.onsubmit = SendForm;
            let input = document.createElement('input');
            let token = document.createElement('input');
            token.type = 'hidden';
            token.id = 'csrf_token';
            token.name = 'csrfmiddlewaretoken';
            token.value = form.csrfmiddlewaretoken;
            input.type = 'button';
            input.onclick = SendForm;
            targetElement.firstChild.appendChild(input);
            targetElement.firstChild.appendChild(token);
        })();
    }
}


function SendForm() {
    let targetElement = document.getElementById('contact');
    let form =  {
        'email': document.getElementById('id_email').value,
        'subject': document.getElementById('id_subject').value,
        'message': document.getElementById('id_message').value,
        'csrfmiddlewaretoken': document.getElementById('scrf_token').value
    };
    (async () => {
        const post_response = await fetch(`${devDomain}contact/`,{
            method: 'post',
            headers: {
                'Content-type': 'application/x-www-form-urlencoded'
            },
            body: JSON.stringify(form)
        });
        let answer = await post_response.json();
        targetElement.innerHTML = `<p>${answer.message}</p>`;
    })();
}


function  GetCalendarWindow() {
    let modalWindows = document.getElementsByClassName('modal-window active');
    if (!document.getElementById('category')) {
        let newItem = CreateWindow('calendar');
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
