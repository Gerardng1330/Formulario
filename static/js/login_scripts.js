/* Referencias */
const hidden_pass_icon = document.getElementById("hidden_pass_icon");
const showing_pass_icon = document.getElementById("showing_pass_icon");
const Contraseña = document.getElementById("Contraseña");
const login_form = document.getElementById("login_form");

/* Al darle click al ícono, se hace el toggle */
hidden_pass_icon.addEventListener("click", function () {
  Contraseña.type = "text";
  hidden_pass_icon.classList.add("hidden");
  showing_pass_icon.classList.remove("hidden");
});

showing_pass_icon.addEventListener("click", function () {
  Contraseña.type = "password";
  hidden_pass_icon.classList.remove("hidden");
  showing_pass_icon.classList.add("hidden");
});

/* Antes de enviar el formulario el type ha de ser password */
login_form.addEventListener("submit", (e) => {
  // Previene el envío predeterminado
  e.preventDefault();

  /* input type a password */
  Contraseña.type = "password";

  /* Envía el formulario a backend */
  login_form.submit();
});
