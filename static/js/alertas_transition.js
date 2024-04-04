const alerta = document.getElementById("alerta");
const alerta_message = document.getElementById("alerta_message").innerText;

/* Transición para mostrar alerta */
if (alerta_message !== "") {
  alerta.classList.remove("opacity-0");
  alerta.classList.add("opacity-100");
  alerta.classList.remove("translate-y-2");
}
