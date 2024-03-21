/* Referencias */
const resend_token_button = document.getElementById("resend_token_button"),
  timer_container = document.getElementById("timer_container"),
  timer_bar = document.getElementById("timer_bar");

/* Al cargar el documento no se puede reenviar token hasta un segundo después */
document.addEventListener("DOMContentLoaded", function () {
  timer_bar.classList.add("w-[0%]");
  timer_bar.classList.remove("w-full");
  resend_token_button.classList.add("pointer-events-none");
  resend_token_button.classList.remove("bg-blue");
  resend_token_button.classList.add("bg-gray-300");
  resend_token_button.classList.remove("text-white");
  resend_token_button.classList.add("text-gray-400");

  setInterval(() => {
    resend_token_button.classList.remove("pointer-events-none");
    resend_token_button.classList.add("bg-blue");
    resend_token_button.classList.remove("bg-gray-300");
    resend_token_button.classList.add("text-white");
    resend_token_button.classList.remove("text-gray-400");
    timer_bar.classList.remove("w-[0%]");
    timer_bar.classList.add("w-full");
    timer_container.classList.add("opacity-0");
    timer_container.classList.remove("opacity-100");
  }, 5000);
});

/* Apenas cargue el sitio, inicia la cuenta regresiva */
resend_token_button.addEventListener("click", function () {});
