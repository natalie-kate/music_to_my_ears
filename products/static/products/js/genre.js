// Make Choose genre selected and disabled
$(document).ready(function () {
    option = document.querySelector("[value='12']");
    $(option).attr("selected", "true")
    $(option).attr("disabled", "disabled")
});
