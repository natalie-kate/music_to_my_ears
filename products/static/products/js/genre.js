// Make Choose genre selected and disabled
$(document).ready(function () {
    var option = document.querySelector("[value='14']");
    $(option).prop("selected", true);
    $(option).prop("disabled", true);
});
