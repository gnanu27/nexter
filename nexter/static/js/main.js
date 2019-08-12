


// const home_height = document.querySelector(".HomeContainer__hero").offsetHeight;

const navbar =()=>{
    if (window.pageYOffset > 200){
        document.querySelector('.navigation').classList.add('navigation_onscroll');
    }

    if(window.pageYOffset < 200){
        document.querySelector('.navigation').classList.remove('navigation_onscroll');

    }
}

setTimeout(()=>{
    $('#message').fadeOut('slow');
}, 3000);