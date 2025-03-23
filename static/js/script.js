document.addEventListener("DOMContentLoaded", function () {
    // Handle fade-in animations on scroll
    const fadeElements = document.querySelectorAll(".fade-in");
    const aboutSections = document.querySelectorAll(".about-text, .about-image");

    function handleScroll() {
        [...fadeElements, ...aboutSections].forEach(section => {
            if (section.getBoundingClientRect().top < window.innerHeight - 50) {
                section.classList.add("visible");
            }
        });
    }

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Run on page load
});

// Lightbox functionality
function openLightbox(img) {
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");

    if (lightbox && lightboxImg) {
        lightbox.style.display = "flex";
        lightboxImg.src = img.src;
    }
}

function closeLightbox() {
    const lightbox = document.getElementById("lightbox");
    if (lightbox) {
        lightbox.style.display = "none";
    }
}

// Contact Form Submission Handling (Prevent Errors if Form is Missing)
const contactForm = document.getElementById("contactForm");
if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
        event.preventDefault();

        let formMessage = document.getElementById("form-message");
        if (formMessage) {
            formMessage.style.color = "gold";
            formMessage.innerText = "Thank you for your message! We will get back to you soon.";
        }

        this.reset();
    });
}

// Slideshow functionality
let slideIndex = 0;
const slides = document.getElementsByClassName("slide");
const dots = document.getElementsByClassName("dot");
let slideTimer;

function showSlides() {
    // Hide all slides
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
        dots[i].classList.remove("active");
    }
    
    // Move to next slide
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    
    // Show current slide
    slides[slideIndex - 1].classList.add("active");
    dots[slideIndex - 1].classList.add("active");
    
    // Change slide every 5 seconds
    clearTimeout(slideTimer);
    slideTimer = setTimeout(showSlides, 5000);
}

function changeSlide(n) {
    clearTimeout(slideTimer);
    slideIndex += n - 1;
    
    if (slideIndex > slides.length) {
        slideIndex = 1;
    } else if (slideIndex < 1) {
        slideIndex = slides.length;
    }
    
    showSlides();
}

function currentSlide(n) {
    clearTimeout(slideTimer);
    slideIndex = n - 1;
    showSlides();
}

// Start slideshow when page loads
if (document.getElementsByClassName("slideshow-container").length > 0) {
    showSlides();
}

// Mobile Navigation Toggle
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('show');
}
