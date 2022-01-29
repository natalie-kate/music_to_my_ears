const chooseDefault = document.getElementById("default-image");
const imgPreview = document.getElementById("default-img-preview");
const chooseImages = document.getElementById("additional-images");
const otherPreview = document.getElementById("img-preview");

if (chooseDefault) {
    chooseDefault.addEventListener("change", function () {
        getImgData(imgPreview, chooseDefault);
    });
}

chooseImages.addEventListener("change", function () {
    getImgData(otherPreview, chooseImages);
});

function getImgData(img, imgFiles) {
    var files = imgFiles.files;
    if (files.length > 1) {
        const arr = Array.from(files);
            arr.forEach(file => displayImg(file));
    } else {
        files = imgFiles.files[0];
        displayImg(files)
    }
    
    function displayImg(files) {
        if (files) {
            const fileReader = new FileReader();
            fileReader.readAsDataURL(files);
            fileReader.addEventListener("load", function () {
                img.style.display = "block";
                img.innerHTML += '<img src="' + this.result + '" />';
            });    
        }
    }
}