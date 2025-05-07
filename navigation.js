document.addEventListener('DOMContentLoaded', () => {
    const currentPageName = window.location.pathname.split('/').pop();
    let currentPageNumber;

    if (currentPageName === 'index.html' || currentPageName === '') { // Treat index.html or root as page 1
        currentPageNumber = 1;
    } else {
        currentPageNumber = parseInt(currentPageName.replace('.html', ''));
    }

    const totalSlides = 12; // Assuming 12 HTML files named index.html, 2.html to 12.html

    function navigateToSlide(slideNumber) {
        if (slideNumber >= 1 && slideNumber <= totalSlides) {
            if (slideNumber === 1) {
                window.location.href = 'index.html';
            } else {
                window.location.href = `${slideNumber}.html`;
            }
        }
    }

    // Keyboard navigation
    document.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowRight') {
            if (currentPageNumber < totalSlides) navigateToSlide(currentPageNumber + 1);
        } else if (event.key === 'ArrowLeft') {
            if (currentPageNumber > 1) navigateToSlide(currentPageNumber - 1);
        }
    });

    // Functions for button clicks
    window.goToNextSlide = function() {
        if (currentPageNumber < totalSlides) {
            navigateToSlide(currentPageNumber + 1);
        }
    }

    window.goToPrevSlide = function() {
        if (currentPageNumber > 1) {
            navigateToSlide(currentPageNumber - 1);
        }
    }

    // Disable buttons at ends
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');

    if (prevButton && currentPageNumber === 1) {
        prevButton.disabled = true;
    }
    if (nextButton && currentPageNumber === totalSlides) {
        nextButton.disabled = true;
    }

    // Optional: Add buttons dynamically if you prefer not to modify HTML manually for each
    // This is a bit more advanced and might require more styling adjustments.
    // For now, we'll assume buttons are added directly in HTML.
}); 