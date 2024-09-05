document.addEventListener('mousemove', function (e) {
    const hero = document.querySelector('.hero');
    const x = (e.clientX / window.innerWidth) * 100;
    const y = (e.clientY / window.innerHeight) * 100;

    gallery.style.backgroundPosition = `${x}% ${y}%`;
});