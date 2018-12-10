var main = function() {
    $('.form-control').focus(function () {
        $(this).addClass('borderAnimateForm');
    })
        .focusout(function() {
            $(this).removeClass('borderAnimateForm');
        })
}

$(document).ready(main);