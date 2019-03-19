'use strict';
var gallery = document.getElementById("gallery");
var allSlides = gallery.querySelectorAll('img');
if (allSlides.length != 0) {
    for (var i = 0; i < allSlides.length; ++i)
        allSlides[i].setAttribute('data-index', i);

    var openedImage = document.getElementById('openedImage');
    var prevSlideButton = document.querySelector('#openedImageContainer .prevSlide');
    var nextSlideButton = document.querySelector('#openedImageContainer .nextSlide');
    var slideIndex = -1;

    prevSlideButton.addEventListener('click', function () {
        showSlide(--slideIndex);
    });

    nextSlideButton.addEventListener('click', function () {
        showSlide(++slideIndex);
    });

    gallery.addEventListener('click', showImage);

    function showSlide(index) {
        if (slideIndex >= allSlides.length)
            slideIndex = 0;
        else if (slideIndex < 0)
            slideIndex = allSlides.length - 1;
        openedImage.src = allSlides[slideIndex].src;
    }
    
    function showImage(event) {
        event.preventDefault();
        if (event.target.tagName == "IMG") {
            openedImage.src = event.target.src;
            slideIndex = event.target.getAttribute('data-index');
        }
    };

    /*
    gallery.addEventListener('mousedown', function (event) {
        event.preventDefault();
        var startX = event.clientX;

        gallery.onmousemove = function (event) {
            gallery.onclick = null;
            var distance = startX - event.clientX;
            gallery.scrollLeft += distance;
            startX = event.clientX;
        };

        gallery.onmouseup = function () {
            gallery.onmousemove = null;
            gallery.onmouseup = null;
            setTimeout(function () {
                gallery.onclick = showImage;
            }, 0);
        };
    });

    function showImage(event) {
        if (event.target.tagName == "IMG") {
            openedImage.src = event.target.src;
            slideIndex = event.target.getAttribute('data-index');
        }
    };
    */
}
