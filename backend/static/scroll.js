let currentTop = 0;
document.getElementById('scrollToTop').addEventListener('click', function() {
    window.scrollTo({
        top: currentTop - window.innerHeight,
        behavior: 'smooth'
    });
    if (currentTop >= window.innerHeight){
        currentTop -= window.innerHeight;
    }
    else {
        currentTop = 0
    }
});

document.getElementById('scrollToBottom').addEventListener('click', function() {
    window.scrollTo({
        top: currentTop + window.innerHeight,
        behavior: 'smooth'
    });
    currentTop += window.innerHeight;
});
