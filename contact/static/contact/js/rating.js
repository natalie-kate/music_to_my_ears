// Add checked attribute to first rating
// Change ratings labels to vinyls
$(document).ready(function () {
  $("#id_rate_us_1").attr('checked', 'checked');
  $(".form-check-label" ).each(function( index ) {
    let html =("<i class='fas fa-record-vinyl' aria-hidden='true'></i>");
    $(this).html(html.repeat(index));
  });
});
