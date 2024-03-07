const container = document.getElementById("container");

const cloneContainer = container.cloneNode(true);
cloneContainer.id = 'dark-body';
document.body.appendChild(cloneContainer);
cloneContainer.classList.remove("active");

const darkContainerImage = document.querySelector("#dark-body .home-image img");
let imgSrc = document.querySelector("#container .home-image img").src.split('.');
imgSrc[imgSrc.length -2] = imgSrc[imgSrc.length - 2].concat('_dark');

const toggleIcons = document.querySelectorAll(".toggle-icon");
const icons = document.querySelectorAll(".toggle-icon i");
const darkContainer = document.querySelector("#dark-body");
darkContainer.querySelector('.home-image img').src = imgSrc.join('.');

darkContainer.querySelector('.modal-window').classList.remove('active');
const modalWindows = document.getElementsByClassName('modal-window');

toggleIcons.forEach(toggle => {
    toggle.addEventListener("click", () => {

        toggle.classList.add("disabled");
        setTimeout(() => {
            toggle.classList.remove("disabled");
        }, 1500);

        icons.forEach(icon => {
            icon.classList.toggle("bx-sun");
        })

        container.classList.toggle("active");
        darkContainer.classList.toggle("active");

        let modalWindow = document.getElementById('category');
        if (modalWindow) modalWindow.remove();

        for (const window of modalWindows) {
            window.classList.toggle('active');
        }
    })
})
