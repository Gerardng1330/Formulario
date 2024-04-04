/* Javascrips reutilizable para mostrar / esconder contraseñas */

/* Referencias */
const hidden_pass_icon = document.getElementById("hidden_pass_icon");
const showing_pass_icon = document.getElementById("showing_pass_icon");
const Contraseña = document.getElementById("Contraseña");
const Contraseña1 = document.getElementById("Contraseña1");
const login_form = document.getElementById("login_form");

/* Al darle click al ícono, se hace el toggle */
/* toggle para mostrar contraseña */
hidden_pass_icon.addEventListener("click", function () {
  Contraseña.type = "text";
  /* Si existe el campo Repetir contraseña, cámbialo también */
  if (Contraseña1) {
    Contraseña1.type = "text";
  }
  hidden_pass_icon.classList.add("hidden");
  showing_pass_icon.classList.remove("hidden");
});

showing_pass_icon.addEventListener("click", function () {
  Contraseña.type = "password";
  /* Si existe el campo Repetir contraseña, cámbialo también */
  if (Contraseña1) {
    Contraseña1.type = "password";
  }
  hidden_pass_icon.classList.remove("hidden");
  showing_pass_icon.classList.add("hidden");
});

/* Antes de enviar el formulario login el type ha de ser password */
if (login_form) {
  login_form.addEventListener("submit", (e) => {
    // Previene el envío predeterminado
    e.preventDefault();

    /* input type a password */
    Contraseña.type = "password";
    /* Si existe el campo Repetir contraseña, cámbialo también */
    if (Contraseña1) {
      Contraseña1.type = "password";
    }

    /* Envía el formulario a backend */
    login_form.submit();
  });
}

/* Antes de enviar el formulario registro el type ha de ser password */
if (registro_form) {
  registro_form.addEventListener("submit", (e) => {
    // Previene el envío predeterminado
    e.preventDefault();

    /* input type a password */
    Contraseña.type = "password";
    /* Si existe el campo Repetir contraseña, cámbialo también */
    if (Contraseña1) {
      Contraseña1.type = "password";
    }

    /* Envía el formulario a backend */
    registro_form.submit();
  });
}
