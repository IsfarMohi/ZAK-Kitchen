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

// Mobile Navigation Toggle
function toggleMenu() {
    document.querySelector(".nav-links")?.classList.toggle("show");
}
