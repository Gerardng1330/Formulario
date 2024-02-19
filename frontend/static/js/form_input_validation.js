/* Referencias de todos los inputs del form */
const form = document.getElementById("form");
const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const email = document.getElementById("email");
const genero = document.getElementById("genero");
const nacionalidad = document.getElementById("nacionalidad");
const fecha_nacimiento = document.getElementById("fecha_nacimiento");
const alergia = document.getElementById("alergia");
const id_file = document.getElementById("id_file");
const cv_file = document.getElementById("cv_file");
const codigo1 = document.getElementById("codigo1");
const Telefono1 = document.getElementById("Telefono1");
const codigo3 = document.getElementById("codigo3");
const telefono_emergencia = document.getElementById("telefono_emergencia");
const codigo2 = document.getElementById("codigo2");
const Telefono2 = document.getElementById("Telefono2");
const nombre_contacto = document.getElementById("nombre_contacto");
const direccion_principal = document.getElementById("direccion_principal");
const direccion_secundaria = document.getElementById("direccion_secundaria");
const ciudad = document.getElementById("ciudad");
const Estado_Provincia = document.getElementById("Estado_Provincia");
const codigo_postal = document.getElementById("codigo_postal");
const Cargo1 = document.getElementById("Cargo1");
const Cargo2 = document.getElementById("Cargo2");
const turno = document.getElementById("turno");
const nivel_ingles = document.getElementById("nivel_ingles");
const fecha_inicio = document.getElementById("fecha_inicio");
const Transporte = document.getElementById("Transporte");
const Conociste = document.getElementById("Conociste");
const referencia = document.getElementById("referencia");

/* Inicialización de expresiones regulares */
const letrasRegex = /^[a-zA-Z]+$/;
const numerosRegex = /^[0-9]+$/;
const nombreApellidoRegex = /^[A-Z][a-z]*$/;
const emailRegex = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
const espacioRegex = /^\s+$/;

/* Previene que el form se envíe antes de validar los inputs.
Se ejecuta cuando se da click al botón APLICAR AHORA */
form.addEventListener("submit", (e) => {
  e.preventDefault();
  validarNombre();
  validarApellido();
  validarEmail();
  validarGenero();
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

/* Validar nombre */
nombre.addEventListener("input", function validarNombre() {
  const input = nombre;
  const value = nombre.value.trim();

  if (value === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
  } else if (!nombreApellidoRegex.test(value)) {
    /* Inicia con mayúscula? */
    setError(input, m_nombre_formato);
  } else if (espacioRegex.test(value)) {
    /* Escribió más de un nombre? */
    setError(input, m_nombre_formato);
  } else if (value.length < 2 || value.length > 20) {
    /* Longitud mínima y máxima */
    setError(input, m_longitud_min_max);
  } else {
    setSuccess(input, "");
  }
});

/* Validar apellido */
nombre.addEventListener("input", function validarApellido() {
  const input = apellido;
  const value = apellido.value.trim();

  if (value === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
  } else if (!nombreApellidoRegex.test(value)) {
    /* Inicia con mayúscula? */
    setError(input, m_apellido_formato);
  } else if (espacioRegex.test(value)) {
    /* Escribió más de un apellido? */
    setError(input, m_apellido_formato);
  } else if (value.length < 2 || value.length > 20) {
    /* Longitud mínima y máxima */
    setError(input, m_longitud_min_max);
  } else {
    setSuccess(input, "");
  }
});

/* Validar email */
email.addEventListener("input", function validarEmail() {
  const input = email;
  const value = email.value.trim();

  if (value === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
  } else if (value.length < 2 || value.length > 30 || !emailRegex.test(value)) {
    /* Longitud mínima y máxima - Formato ejemplo@email.com */
    setError(input, m_email_formato);
  } else {
    setSuccess(input, "");
  }
});

/* Validar género */
genero.addEventListener("click", function validarGenero() {
  const input = genero;
  const value = genero.value.trim();

  if (value === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
  } else {
    setSuccess(input, "");
  }
});
