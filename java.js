'use strict'

const switcher = document.querySelector(".button");

switcher.addEventListener('click',function(){
    document.body.classList.toggle('tema')

    var className = document.body.className;
    if(className == "tema") {
        this.textcontent = "escuro";
        
    }
    else{
        this.textcontent = "claro";
    }

});



