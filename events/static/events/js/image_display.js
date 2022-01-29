const chooseDefault = document.getElementById("id_image");
const imgPreview = document.getElementById("img-preview");

chooseDefault.addEventListener("change", function () {
    var files = chooseDefault.files[0]
    if (files) {
        const fileReader = new FileReader();
        fileReader.readAsDataURL(files);
        fileReader.addEventListener("load", function () {
            imgPreview.style.display = "block";
            imgPreview.innerHTML += '<img src="' + this.result + '" />';
        });    
    }
});