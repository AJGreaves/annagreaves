window.onscroll = function () {
    scrollFunction();
};

/**
 * Adds dark background to navbar when user scrolls down, adds necessary contrast so menu items are readable.
 */
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('navbar').classList.add('dark-background');
    } else {
        document.getElementById('navbar').classList.remove('dark-background');
    }
}

// sets current year for copyright info in footer
document.getElementById("year").innerHTML = new Date().getFullYear();