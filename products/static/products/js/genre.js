// Make Choose genre selected and disabled
$(document).ready(function () {
    var option = document.querySelector("[value='1']");
    $(option).before(
        "<option selected='true' value='0' disabled='disabled' placeholder='Choose Genre'>Choose Genre</option>");
});