var main = function(){
    // Insert functions here
    $('.nav-icon').click(function(){
        $('.icon')
            .toggleClass('menu')
            .toggleClass('close');
    })
};


// variable main will run when website is loaded
$(document).ready(main);