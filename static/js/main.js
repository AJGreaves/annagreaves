window.onscroll = function () {
    scrollFunction();
};

/**
 * Hides navbar when user scrolls down.
 */
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('navbar').classList.add('dark-background');
    } else {
        document.getElementById('navbar').classList.remove('dark-background');
    }
}