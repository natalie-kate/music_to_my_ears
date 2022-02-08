// Declare variables
const chooseDefault = document.getElementById("default-image");
const imgPreview = document.getElementById("default-img-preview");
const chooseImages = document.getElementById("additional-images");
const otherPreview = document.getElementById("img-preview");

// If there is a chooseDefault input add change event listener and
// send input and div thats to display the images to getImgData function
if (chooseDefault) {
    chooseDefault.addEventListener("change", function () {
        getImgData(imgPreview, chooseDefault);
    });
}

// Add change event listener to other image input field and send
// input and div thats to display the images to getImgData function
chooseImages.addEventListener("change", function () {
    getImgData(otherPreview, chooseImages);
});

// Get each file that has been input and send to displayImg function
function getImgData(img, imgFiles) {
    var files = imgFiles.files;
    if (files.length > 1) {
        const arr = Array.from(files);
            arr.forEach(file => displayImg(file));
    } else {
        files = imgFiles.files[0];
        displayImg(files)
    }
    
    // Takes each individual image file an displays in div
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