$(document).ready( function() {
    $(".nav li a").each( function () {
        var urlstr = window.location.href;
        if (urlstr.indexOf($(this).attr("href")) != -1 && $(this).attr("href") != "/") {
            $(this).parent().addClass("active");
        } else {
            $(this).parent().removeClass("active");
        }
    });
});