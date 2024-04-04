/* Referencias */
const send_button = document.getElementById("send_button");
const timer_container = document.getElementById("timer_container");
const timer_bar = document.getElementById("timer_bar");
const alerta = document.getElementById("alerta");
const alerta_message = document.getElementById("alerta_message").innerText;

/* Al cargar el sitio, automaticamente se activa el timer y desactiva el botón.*/
document.addEventListener("DOMContentLoaded", function () {
  setInterval(() => {
    /* Luego de un intervalo de 1s, se activa el botón y se desactiva el timer. */
    timer_container.classList.remove("opacity-100");
    timer_container.classList.add("opacity-0");

    send_button.classList.remove("bg-gray-200");
    send_button.classList.add("bg-blue");

    send_button.classList.remove("text-gray-400");
    send_button.classList.add("text-white");

    send_button.classList.remove("pointer-events-none");
  }, 5000);
});

/* Transición para mostrar alerta */
if (alerta_message !== "") {
  alerta.classList.remove("opacity-0");
  alerta.classList.add("opacity-100");
  alerta.classList.remove("translate-y-2");
}
