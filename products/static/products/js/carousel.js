// Add active class to the first child of each carousel
$(document).ready(function () {
    $(".carousel-inner" ).each(function( index ) {
        $(this).children().first().addClass('active');
    });
});
