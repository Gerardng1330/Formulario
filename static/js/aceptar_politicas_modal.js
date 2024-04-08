/* Referencias */
const body = document.querySelector("#body");
const static_modal = document.querySelector("#static-modal");
const form_container = document.querySelector("#form_container");
const aceptar_politicas_button = document.querySelector("#aceptar_politicas_button");

if (aceptar_politicas_button) {
  document.addEventListener("DOMContentLoaded", function () {
    aceptar_politicas_button.addEventListener("click", function () {
      /* Esconder el modal */
      body.classList.remove("overflow-hidden");
      static_modal.classList.add("hidden");
      form_container.classList.remove("blur-sm");
      /* Generación de la cookie */
      const randomValue = politicas_aceptadas_uuid;
      document.cookie = "pltc=" + randomValue + "; max-age=" + 365 * 24 * 60 * 60 + "; path=/";
      /* Hay que agregar esto     Secure; HttpOnly;    cuando htttps esté configurado  */
      console.log(document.cookie);
    });
  });
}
