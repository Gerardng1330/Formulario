/* Referencias */
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
const copyright = document.getElementById("copyright");
const copiar_correo_button = document.getElementById("copiar_correo_button");
const svg_before_copy = document.getElementById("svg_before_copy");
const span_before_copy = document.getElementById("span_before_copy");
const svg_after_copy = document.getElementById("svg_after_copy");
const span_after_copy = document.getElementById("span_after_copy");
const body = document.querySelector("#body");

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
/* copyright.classList.add("pl-40"); */

/* Que el body no se pueda scrollear */
/* body.classList.add("overflow-hidden"); */

/* Copiar correo de arv a clipboard al hacer click */
copiar_correo_button.addEventListener("click", function () {
  /* Text to be copied */
  var text_to_copy = "support@arvcloud.com";

  /* Create a temporary textarea element to perform the copy command */
  var textarea = document.createElement("textarea");
  textarea.value = text_to_copy;
  document.body.appendChild(textarea);

  /* Select the text in the textarea */
  textarea.select();
  textarea.setSelectionRange(0, 99999); // For mobile devices

  /* Execute the copy command */
  document.execCommand("copy");

  /* Quitar estilos de before */
  svg_before_copy.classList.add("hidden");
  span_before_copy.classList.add("hidden");
  copiar_correo_button.classList.remove("bg-blue");
  copiar_correo_button.classList.remove("hover:bg-hoverblue");

  /* Poner estilos de after */
  svg_after_copy.classList.remove("hidden");
  span_after_copy.classList.remove("hidden");
  copiar_correo_button.classList.add("bg-sky");

  /* Volver a como estaba luego de unos segundos */
  setTimeout(function () {
    /* Poner estilos de before */
    svg_before_copy.classList.remove("hidden");
    span_before_copy.classList.remove("hidden");
    copiar_correo_button.classList.add("bg-blue");
    copiar_correo_button.classList.add("hover:bg-hoverblue");

    /* Quitar estilos de after */
    svg_after_copy.classList.add("hidden");
    span_after_copy.classList.add("hidden");
    copiar_correo_button.classList.remove("bg-sky");
  }, 2500);

  /* Remove the temporary textarea */
  document.body.removeChild(textarea);
});
