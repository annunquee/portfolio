document.addEventListener('DOMContentLoaded', function () {
    const gallery = document.getElementById('project-gallery');
    const nextBtn = document.getElementById('next-btn');
    const prevBtn = document.getElementById('prev-btn');

    let scrollAmount = 0;
    const scrollStep = 200; 

    nextBtn.addEventListener('click', function () {
        gallery.scrollBy({ left: scrollStep, behavior: 'smooth' });
    });

    prevBtn.addEventListener('click', function () {
        gallery.scrollBy({ left: -scrollStep, behavior: 'smooth' });
    });
});
