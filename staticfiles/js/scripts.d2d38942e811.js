

//Cambiar estilos del formulario cuando el usuario completa el campo input
function changeStyle(input) {
    if (input.value !=="") {
        input.classList.add("filled")
    }else{
        input.classList.remove("filled")
    }
}

function closeMenu() {
    let navbarCollapse = document.querySelector('.navbar-collapse');
    if (navbarCollapse.classList.contains('show')) {
        navbarCollapse.classList.remove('show');
    }
}



