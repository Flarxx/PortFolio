document.addEventListener('DOMContentLoaded', () => {
    const swiper = new Swiper('.certSwiper', {
        slidesPerView: 3,
        spaceBetween: 20,
        loop: false,
        autoplay: false,
        pagination: { el: '.swiper-pagination', clickable: true },
        navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
        breakpoints: { 0: { slidesPerView: 1 }, 600: { slidesPerView: 2 }, 992: { slidesPerView: 3 } }
    });
});
