document.addEventListener('DOMContentLoaded', function () {
  const swiper = new Swiper('.certificados-swiper', {
    effect: 'coverflow',          // "profundidad" tipo coverflow
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',       // ancho por CSS .swiper-slide { width: ... }
    spaceBetween: 30,
    loop: true,
    coverflowEffect: {
      rotate: 0,
      stretch: -60,
      depth: 200,
      modifier: 1,
      slideShadows: false
    },
    autoplay: {
      delay: 4200,
      disableOnInteraction: false
    },
    lazy: {
      loadPrevNext: true,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.custom-next',
      prevEl: '.custom-prev',
    },
    keyboard: {
      enabled: true,
      onlyInViewport: true,
    }
  });

  // Pausar autoplay al pasar el ratón (mejora UX)
  const target = document.querySelector('.certificados-swiper');
  target.addEventListener('mouseenter', () => swiper.autoplay.stop());
  target.addEventListener('mouseleave', () => swiper.autoplay.start());
});
