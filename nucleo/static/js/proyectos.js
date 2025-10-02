document.addEventListener("DOMContentLoaded", () => {
  const techSwiper = new Swiper(".tech-swiper", {
    loop: true,
    slidesPerView: 3    ,
    spaceBetween: 15,
    speed: 3000, // velocidad del movimiento
    autoplay: {
      delay: 0,
      disableOnInteraction: false
    },
    allowTouchMove: false, // evita interacción del usuario
    freeMode: true, // movimiento libre continuo
  });
});
