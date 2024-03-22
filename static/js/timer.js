/* Referencias */
const resend_token_button = document.getElementById("resend_token_button"),
  timer_container = document.getElementById("timer_container"),
  timer_bar = document.getElementById("timer_bar");

/* Al cargar el documento no se puede reenviar token hasta un segundo después */
document.addEventListener("DOMContentLoaded", function () {
  setInterval(() => {
    resend_token_button.classList.add("bg-blue");
    resend_token_button.classList.remove("bg-gray-300");
    resend_token_button.classList.add("text-white");
    resend_token_button.classList.remove("text-gray-400");
  }, 5000);
});

/* Apenas cargue el sitio, inicia la cuenta regresiva */
resend_token_button.addEventListener("click", function () {
  resend_token_button.classList.remove("bg-blue");
  resend_token_button.classList.add("bg-gray-300");
  resend_token_button.classList.remove("text-white");
  resend_token_button.classList.add("text-gray-400");
});
