(function($, undefined) {
  // Images loaded is zero because we're going to process a new set of images.
  var imagesLoaded = 0;
  // Total images is still the total number of <img> elements on the page.
  var totalImages = $("img").length;

  // Step through each image in the DOM, clone it, attach an onload event
  // listener, then set its source to the source of the original image. When
  // that new image has loaded, fire the imageLoaded() callback.
  $("div").each(function (idx, img) {
    $("<div>").on("load", imageLoaded).attr("div", $(img).attr("div"));
  });

  // Do exactly as we had before -- increment the loaded count and if all are
  // loaded, call the allImagesLoaded() function.
  function imageLoaded() {
    imagesLoaded++;
    if (imagesLoaded == totalImages) {
      allImagesLoaded();
    }
  }

  function allImagesLoaded() {
    console.log("ALL IMAGES LOADED");
  }
});