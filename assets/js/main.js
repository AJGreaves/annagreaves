window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $(".navbar").addClass('invisible');
    } else {
        $(".navbar").removeClass('invisible');
    }
}