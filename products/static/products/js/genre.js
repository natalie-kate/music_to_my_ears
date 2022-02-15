// Make Choose genre selected and disabled
$(document).ready(function () {
    option = document.querySelector("[value='choose_genre']");
    console.log(option)
    $(option).attr("selected", "true")
    $(option).attr("disabled", "disabled")
});
