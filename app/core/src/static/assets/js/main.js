let animado = document.querySelectorAll(".animado");

function mostrarScroll(){
    let scrollTop = document.documentElement.scrollTop;
    for(var i = 0; i < animado.length; i++){
        let alturaAni = animado[i].offsetTop;
        if(alturaAni - 300 < scrollTop){
            animado[i].style.opacity = 1;
        }
    }
}

window.addEventListener('scroll', mostrarScroll);
