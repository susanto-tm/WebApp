var main = function(){
    // Insert functions here
    $('.nav-icon').click(function() {
        $('.icon')
            .toggleClass('menu')
            .toggleClass('close'); 
    })
    $('.content-markdown').each(function() {
        var content = $(this).text();
        console.log(content);
        var markedContent = marked(content);
        console.log(markedContent);
        $(this).html(markedContent);

    })
};


// variable main will run when website is loaded
$(document).ready(main);