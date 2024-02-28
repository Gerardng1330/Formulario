/* Realiza todos los cambios necesarios a las clases cuando el usuario acepte las políticas */
function aceptarPoliticas() {
  let body = document.querySelector("#body");
  let static_modal = document.querySelector("#static-modal");
  let form_container = document.querySelector("#form_container");

  body.classList.remove("overflow-hidden");
  static_modal.classList.add("hidden");
  form_container.classList.remove("blur-sm");
}
