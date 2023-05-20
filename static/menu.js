/* Функция для скрытия/раскрытия меню */
function toggleMenu() {
    var navbar = document.getElementById("navbar");
    navbar.classList.toggle("show");
    }
    /* Функция для обработки нажатия клавиши "m" */
    document.addEventListener('keydown', function(event) {
    if (event.key === 'm') {
        toggleMenu();
    }
    });