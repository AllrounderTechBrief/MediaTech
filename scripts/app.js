let slideIndex = 0;
function rotateSlides() {
    const slides = document.querySelectorAll('.slide');
    if (slides.length === 0) return;
    
    // Remove active class from everyone
    slides.forEach(s => {
        s.classList.remove('active');
        // Stop playing video when slide is hidden
        const iframe = s.querySelector('iframe');
        if (iframe) {
            const src = iframe.src;
            iframe.src = src; // Resets video playback
        }
    });

    // Show current slide
    slides[slideIndex].classList.add('active');
    slideIndex = (slideIndex + 1) % slides.length;
}

// Start rotation every 10 seconds (gives time for video viewing)
setInterval(rotateSlides, 10000);
window.onload = rotateSlides;
