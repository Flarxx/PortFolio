document.addEventListener("DOMContentLoaded", () => {
  const swiper = new Swiper(".certificados-swiper", {
    loop: true,
    slidesPerView: 1,
    spaceBetween: 30,
    grabCursor: true,
    centeredSlides: true,

    navigation: {
      nextEl: ".custom-next",
      prevEl: ".custom-prev",
    },

    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },

    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },

    speed: 800, // animación más suave
  });
});
