/* Referencias de todos los botones */
/* const btn_contrasena = document.getElementById("btn_contrasena");
const btn_proteccion = document.getElementById("btn_proteccion");
const btn_act_politicas = document.getElementById("btn_act_politicas");
const btn_act_terminos = document.getElementById("btn_act_terminos");
const btn_eliminacion = document.getElementById("btn_eliminacion");
const btn_tiempo = document.getElementById("btn_tiempo");
const btn_copia = document.getElementById("btn_copia");
const btn_derechos_autor = document.getElementById("btn_derechos_autor");
const btn_servicios_pago = document.getElementById("btn_servicios_pago");
const btn_empresas_rel = document.getElementById("btn_empresas_rel");
const btn_reembolso = document.getElementById("btn_reembolso");
const btn_inicio = document.getElementById("btn_inicio"); */

/* Refencia de la página activa */
const active_page = window.location.pathname.substring(4);
/* Trae cada link y lo verifica */
const sidebarButtons = document.querySelectorAll(".sidebar_button").forEach((link) => {
  /* Si la referencia del link es la página activa */
  if (link.href.includes(active_page)) {
    /* Quita las clases de botón inactivo */
    link.classList.remove("hover:bg-gray-100");
    link.classList.remove("hover:bg-opacity-50");
    /* Agrega las clases de botón activo */
    link.classList.add("bg-sky");
    link.classList.add("bg-opacity-10");
    link.classList.add("text-sky");
  } else {
    /* Quita las clases de botón activo */
    link.classList.remove("bg-sky");
    link.classList.remove("bg-opacity-10");
    link.classList.remove("text-sky");
    /* Regrésale las clases de botón inactivo */
    link.classList.add("hover:bg-gray-100");
    link.classList.add("hover:bg-opacity-50");
  }
});

/* Centrar mensaje de copyright solo en las políticas (por el descuadre del sidebar) */
const copyright = document.getElementById("copyright");
copyright.classList.add("pl-40");
