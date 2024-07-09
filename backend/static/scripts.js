let slideIndex = 0;
let slides;
let dots;

function showSlides(index) {
    slides = document.getElementsByClassName('slider-item');
    dots = document.getElementsByClassName('dot');

    if (index >= slides.length) {
        slideIndex = 0;
    } else if (index < 0) {
        slideIndex = slides.length - 1;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }

    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(' active', '');
    }

    slides[slideIndex].style.display = 'flex';  // Use 'flex' instead of 'block'
    dots[slideIndex].className += ' active';
    console.log('Showing slide:', slideIndex);  // Debug log
}

function nextSlide() {
    console.log('Next slide');  // Debug log
    showSlides(++slideIndex);
}

function prevSlide() {
    console.log('Previous slide');  // Debug log
    showSlides(--slideIndex);
}

function currentSlide(index) {
    showSlides(slideIndex = index);
}

document.addEventListener('DOMContentLoaded', () => {
    showSlides(slideIndex);
    document.querySelector('.prev').addEventListener('click', prevSlide);
    document.querySelector('.next').addEventListener('click', nextSlide);
    const dotsContainer = document.querySelector('.dots-container');
    dotsContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('dot')) {
            const index = Array.from(dotsContainer.children).indexOf(e.target);
            currentSlide(index);
        }
    });
});





function updateTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const currentTime = `${hours}:${minutes}`;
    document.getElementById('current-time').textContent = currentTime;
}

setInterval(updateTime, 1000);
updateTime();

