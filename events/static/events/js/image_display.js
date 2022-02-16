// Declare variables
const chooseDefault = document.getElementById("id_image");
const imgPreview = document.getElementById("img-preview");

// Add change event listener to file input field
chooseDefault.addEventListener("change", function () {
    var files = chooseDefault.files[0];
    if (files) {
        const fileReader = new FileReader();
        fileReader.readAsDataURL(files);
        // Add load event listener to file reader to display
        // chosen image file in img preview div
        fileReader.addEventListener("load", function () {
            imgPreview.style.display = "block";
            imgPreview.innerHTML += '<img src="' + this.result + '" />';
        });    
    }
});