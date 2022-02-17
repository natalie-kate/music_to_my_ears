// Make Choose genre selected and disabled
$(document).ready(function () {
    var option = document.querySelector("[value='14']");
    $(option).attr("selected", "selected");
    $(option).attr("disabled", "disabled");
});
