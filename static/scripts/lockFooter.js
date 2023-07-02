// Check if the page has scrolling
    function hasScrolling() {
        return document.body.scrollHeight > window.innerHeight;
    }
    function updateFooterStyle() {
        var footer = document.querySelector('#footerCustom');
        if (hasScrolling()) {
            footer.classList.remove('no-scrolling');
        } else {
            footer.classList.add('no-scrolling');
        }
    }

    // Update footer style on page load and resize
    window.addEventListener('load', updateFooterStyle);
    window.addEventListener('resize', updateFooterStyle);