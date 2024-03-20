/* Referencias */
const registro_form = document.getElementById("registro_form");
const Nombre = document.getElementById("Nombre");
const Apellido = document.getElementById("Apellido");
const Usuario = document.getElementById("Usuario");
const Correo = document.getElementById("Correo");
const Contraseña = document.getElementById("Contraseña");
const Contraseña1 = document.getElementById("Contraseña1");
const hidden_pass_icon = document.getElementById("hidden_pass_icon");
const showing_pass_icon = document.getElementById("showing_pass_icon");
const eight_char = document.getElementById("eight_char");
const numbers = document.getElementById("numbers");
const lower = document.getElementById("lower");
const upper = document.getElementById("upper");
const special = document.getElementById("special");
const pass_security_container = document.getElementById("pass_security_container");

/* Inicialización de expresiones regulares */
const letrasRegex = /^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]+$/;
const numerosRegex = /^[0-9]+$/;
const nombreApellidoRegex = /^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]*$/;
const emailRegex = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
const espacioRegex = / /;
const nombreContactoRegex = /^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+\s[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+$/;
const ciudadEstadoRegex = /^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]*$/;
const longitud_max = 30;
const eight_char_regex =
  /* toggle para mostrar contraseña */
  hidden_pass_icon.addEventListener("click", function () {
    Contraseña.type = "text";
    Contraseña1.type = "text";
    hidden_pass_icon.classList.add("hidden");
    showing_pass_icon.classList.remove("hidden");
  });

showing_pass_icon.addEventListener("click", function () {
  Contraseña.type = "password";
  Contraseña1.type = "password";
  hidden_pass_icon.classList.remove("hidden");
  showing_pass_icon.classList.add("hidden");
});

/* Función que recibe un elemento html (el input) y un mensaje a mostrar (que se trae del html como variable, para permitir la internacionalización */
function setError(element, message) {
  const input_control = element.parentElement; /* Referencia: div padre del input proporcionado */
  const message_display = input_control.querySelector(".message"); /* Referencia: span del mensaje */
  message_display.classList.remove("hidden");
  message_display.innerText = message; /* Asignación: mensaje a mostrar en el span */
  message_display.classList.add("text-red");
  message_display.classList.remove("text-lime-500");
  element.classList.add("border-red"); /* Estilización del input */
  element.classList.remove("border-gray-300");
  element.classList.remove("border");
  element.classList.add("border-2");
  element.classList.remove("border-lime-500");
}

/* Función que recibe un elemento html (el input) y un mensaje a mostrar (que se trae del html como variable, para permitir la internacionalización */
function setSuccess(element, message) {
  const input_control = element.parentElement; /* Referencia: div padre del input proporcionado */
  const message_display = input_control.querySelector(".message"); /* Referencia: span del mensaje */
  message_display.classList.add("hidden");
  element.classList.add("border-lime-500"); /* Estilización del input */
  element.classList.remove("border-gray-300");
  element.classList.remove("border");
  element.classList.add("border-2");
  element.classList.remove("border-red");
}

/* Validation functions */
function validarNombreApellido(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (!nombreApellidoRegex.test(input.value.trim())) {
    /* Inicia con mayúscula? */
    setError(input, m_nombre_formato);
    return false;
  } else if (espacioRegex.test(input.value.trim())) {
    /* Escribió más de un nombre? */
    setError(input, m_nombre_formato);
    return false;
  } else if (input.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(input, m_longitud_max);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

function validarUsuario(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (espacioRegex.test(input.value.trim())) {
    /* Ingresó algún espacio? */
    setError(input, m_usuario_formato);
    return false;
  } else if (input.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(input, m_longitud_max);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

async function validarEmail() {
  /* Obtener el csrftoken */
  const csrftoken = document.cookie
    .split("; ")
    .find((row) => row.startsWith("csrftoken="))
    .split("=")[1];

  try {
    // Petición AJAX usando fetch
    const response = await fetch("/obtener_emails/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken, // Don't forget to include the CSRF token
      },
    });

    // Supongamos que 'jsonListaCorreos' es tu lista en formato JSON
    let emails_list = await response.json();

    // Validaciones
    if (Correo.value.trim() === "") {
      /* Campo requerido */
      setError(Correo, m_campo_requerido);
      return false;
    } else if (emails_list.includes(Correo.value.trim())) {
      setError(Correo, m_correo_registrado);
      return false;
    } else if (Correo.value.trim().length > 30 || !emailRegex.test(Correo.value.trim())) {
      /* Longitud mínima y máxima - Formato ejemplo@email.com */
      setError(Correo, m_email_formato);
      return false;
    } else {
      setSuccess(Correo, "");
      return true;
    }
  } catch (error) {
    console.error("Error fetching registered emails:", error);
  }
}

function validarContraseña(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (espacioRegex.test(input.value.trim())) {
    /* Ingresó algún espacio? */
    setError(input, m_contrasena_space);
    return false;
  } else if (input.value.trim().length >= 8) {
    /* 8+ caracteres */
    eight_char.classList.remove("text-gray-400");
    eight_char.classList.add("text-lime-500");
  } else if (input.value.trim().length >= 8) {
    /* Si todo del formato se cumple al mismo tiempo: */
    setSuccess(input, "");
    return true;
  } else {
    /* Si no se cumple nada de las validaciones de formato: */
    setError(input, m_contrasena_formato);
    return false;
  }
}

/* Validaciones por campo en tiempo real*/
document.addEventListener("DOMContentLoaded", function () {
  /* Validar nombre */
  Nombre.addEventListener("input", function () {
    validarNombreApellido(Nombre);
  });

  /* Validar apellido */
  Apellido.addEventListener("input", function () {
    validarNombreApellido(Apellido);
  });

  /* Validar usuario */
  Usuario.addEventListener("input", function () {
    validarUsuario(Usuario);
  });

  /* Validar email */
  Correo.addEventListener("input", function () {
    validarEmail();
  });

  /* Validar contraseña */
  Contraseña.addEventListener("input", function () {
    validarContraseña(Contraseña);
  });

  Contraseña.addEventListener("focus", function () {
    pass_security_container.classList.remove("opacity-0");
    pass_security_container.classList.add("opacity-100");
  });

  Contraseña.addEventListener("blur", function () {
    pass_security_container.classList.remove("opacity-100");
    pass_security_container.classList.add("opacity-0");
  });
});
