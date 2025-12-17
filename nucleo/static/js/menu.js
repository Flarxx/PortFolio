const toggle = document.getElementById("menuToggle");
const nav = document.querySelector("nav");
const icon = toggle.querySelector("i"); // el icono de Feather

toggle.addEventListener("click", () => {
  // toggle clase active al nav
  nav.classList.toggle("active");

  // cambiar icono según estado
  if(nav.classList.contains("active")) {
    icon.setAttribute("data-feather", "x"); // cambia a X
  } else {
    icon.setAttribute("data-feather", "menu"); // vuelve al menú
  }

  // reemplaza los iconos feather
  feather.replace();
});
