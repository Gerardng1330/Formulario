/* Referencias de todos los elementos e inputs del form */
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
/* const codigo_postal = document.getElementById("codigo_postal"); */
const Cargo1 = document.getElementById("Cargo1");
const Cargo2 = document.getElementById("Cargo2");
const turno = document.getElementById("turno");
const nivel_ingles = document.getElementById("nivel_ingles");
const fecha_inicio = document.getElementById("fecha_inicio");
const Transporte = document.getElementById("Transporte");
const Conociste = document.getElementById("Conociste");
const referencia = document.getElementById("referencia");

/* Inicialización de expresiones regulares */
const letrasRegex = /^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]+$/;
const numerosRegex = /^[0-9]+$/;
const nombreApellidoRegex = /^[A-ZáéíóúÁÉÍÓÚüÜñÑ][a-záéíóúÁÉÍÓÚüÜñÑ]*$/;
const emailRegex = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
const espacioRegex = /^\s+$/;
const nombreContactoRegex = /^[A-ZáéíóúÁÉÍÓÚüÜñÑ][a-záéíóúÁÉÍÓÚüÜñÑ]+ [A-ZáéíóúÁÉÍÓÚüÜñÑ][a-záéíóúÁÉÍÓÚüÜñÑ]+$/;
const ciudadEstadoRegex = /^[A-ZáéíóúÁÉÍÓÚüÜñÑ][a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]*$/;
const longitud_max = 30;

/* Previene que el form se envíe antes de validar los inputs.
Se ejecuta cuando se da click al botón APLICAR AHORA */
form.addEventListener("submit", (e) => {
  e.preventDefault();
  /* Se agrega cada función para que la validación al hacer "submit" sea independiente a los eventos de validación a tiempo real */
  validarNombre();
  validarApellido();
  validarEmail();
  validarGenero();
  validarNacionalidad();
  validarFechaNacimientoVacia();
  validarFechaNacimiento();
  validarAlergia();
  validarID();
  validarCV();
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

/* Función para validar selects, que no estén vacíos. Recibe el input. */
function validarRequerido(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
  } else {
    setSuccess(input, "");
  }
}

/* Función para validar números de teléfono */
function validarTelefono(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
  } else if (!numerosRegex.test(input.value.trim())) {
    /* Solo se aceptan números */
    setError(input, m_telefono_regex);
  } else if (input.value.trim().length > 9) {
    /* Longitud máxima */
    setError(input, m_telefono_formato);
  } else {
    setSuccess(input, "");
  }
}

/* Validaciones por campo */
document.addEventListener("DOMContentLoaded", function () {
  /* Validar nombre */
  nombre.addEventListener("input", function validarNombre() {
    if (nombre.value.trim() === "") {
      /* Campo requerido */
      setError(nombre, m_campo_requerido);
    } else if (!nombreApellidoRegex.test(nombre.value.trim())) {
      /* Inicia con mayúscula? */
      setError(nombre, m_nombre_formato);
    } else if (espacioRegex.test(nombre.value.trim())) {
      /* Escribió más de un nombre? */
      setError(nombre, m_nombre_formato);
    } else if (nombre.value.trim().length < 3) {
      /* Longitud mínima */
      setError(nombre, m_longitud_min);
    } else if (nombre.value.trim().length > longitud_max) {
      /* Longitud máxima */
      setError(nombre, m_longitud_max);
    } else {
      setSuccess(nombre, "");
    }
  });

  /* Validar apellido */
  apellido.addEventListener("input", function validarApellido() {
    if (apellido.value.trim() === "") {
      /* Campo requerido */
      setError(apellido, m_campo_requerido);
    } else if (!nombreApellidoRegex.test(apellido.value.trim())) {
      /* Inicia con mayúscula? */
      setError(apellido, m_apellido_formato);
    } else if (espacioRegex.test(apellido.value.trim())) {
      /* Escribió más de un apellido? */
      setError(apellido, m_apellido_formato);
    } else if (apellido.value.trim().length < 3) {
      /* Longitud mínima */
      setError(apellido, m_longitud_min);
    } else if (apellido.value.trim().length > longitud_max) {
      /* Longitud máxima */
      setError(apellido, m_longitud_max);
    } else {
      setSuccess(apellido, "");
    }
  });

  /* Validar email */
  email.addEventListener("input", function validarEmail() {
    if (email.value.trim() === "") {
      /* Campo requerido */
      setError(email, m_campo_requerido);
    } else if (email.value.trim().length < 3 || email.value.trim().length > 30 || !emailRegex.test(email.value.trim())) {
      /* Longitud mínima y máxima - Formato ejemplo@email.com */
      setError(email, m_email_formato);
    } else {
      setSuccess(email, "");
    }
  });

  /* Validar género */
  genero.addEventListener("click", function () {
    validarRequerido(genero);
  });

  /* Validar nacionalidad */
  nacionalidad.addEventListener("click", function () {
    validarRequerido(nacionalidad);
  });

  /* Validar fecha_nacimiento */
  /* Si das click y no ingresas nada (vas a otro campo) */
  fecha_nacimiento.addEventListener("blur", function validarFechaNacimientoVacia() {
    if (fecha_nacimiento.value.trim() === "") {
      /* Campo requerido */
      setError(fecha_nacimiento, m_campo_requerido);
    }
  });

  /* Si los valores del input cambian */
  fecha_nacimiento.addEventListener("input", function validarFechaNacimiento() {
    var fecha_actual = new Date();
    var fecha_ingresada = new Date(fecha_nacimiento.value.trim());
    var diferencia_dias = Math.floor((fecha_actual - fecha_ingresada) / (1000 * 60 * 60 * 24));
    console.log(diferencia_dias);
    if (diferencia_dias < 0) {
      /* Fecha futura? */
      setError(fecha_nacimiento, m_fecha_futura);
    } else if (diferencia_dias < 6570) {
      /* Debes tener mínimo 18 años */
      setError(fecha_nacimiento, m_edad_minima);
    } else {
      setSuccess(fecha_nacimiento, "");
    }
  });

  /* Validar discapacidad / alergia */
  alergia.addEventListener("input", function validarAlergia() {
    if (alergia.value.trim() === "") {
      /* Campo requerido */
      setError(alergia, m_campo_requerido);
    } else if (!letrasRegex.test(alergia.value.trim())) {
      /* Formato de texto */
      setError(alergia, m_letras_regex);
    } else if (alergia.value.trim().length > longitud_max) {
      /* Longitud mínima */
      setError(alergia, m_longitud_max);
    } else {
      setSuccess(alergia, "");
    }
  });

  /* Validar id_file */
  function validarID() {
    if (id_file.value.trim() === "") {
      /* Campo requerido */
      setError(id_file, m_campo_requerido);
    } else {
      setSuccess(id_file, "");
    }
  }

  /* Validar cv_file */
  function validarCV() {
    if (cv_file.value.trim() === "") {
      /* Campo requerido */
      setError(cv_file, m_campo_requerido);
    } else {
      setSuccess(cv_file, "");
    }
  }

  /* Validar codigo1 */
  codigo1.addEventListener("click", function validarCodigo1() {
    validarRequerido(codigo1);
  });

  /* Validar Telefono1 */
  Telefono1.addEventListener("input", function validarTelefono1() {
    validarTelefono(Telefono1);
  });

  /* Validar codigo3 */
  codigo3.addEventListener("click", function validarCodigo3() {
    validarRequerido(codigo3);
  });

  /* Validar telefono_emergencia */
  telefono_emergencia.addEventListener("input", function validarTelefonoEmergencia() {
    validarTelefono(telefono_emergencia);
  });

  /* Validar codigo2 */
  codigo2.addEventListener("click", function validadCodigo2() {
    validarRequerido(codigo2);
  });

  /* Validar Telefono2 */
  Telefono2.addEventListener("input", function validarTelefono2() {
    validarTelefono(Telefono2);
  });

  /* Validar nombre_contacto */
  nombre_contacto.addEventListener("input", function validarNombreContacto() {
    if (nombre_contacto.value.trim() === "") {
      /* Campo requerido */
      setError(nombre_contacto, m_campo_requerido);
    } else if (!nombreContactoRegex.test(nombre_contacto.value.trim())) {
      /* Está incorrecto el formato "Nombre Apellido"? */
      setError(nombre_contacto, m_nombre_contacto_formato);
    } else if (nombre_contacto.value.trim().length > longitud_max) {
      /* Longitud máxima */
      setError(nombre_contacto, m_longitud_max);
    } else {
      setSuccess(nombre_contacto, "");
    }
  });

  /* Validar direccion_principal */
  direccion_principal.addEventListener("input", function validarDireccionPrincipal() {
    validarRequerido(direccion_principal);
  });

  /* La dirección secundaria no es requerida */

  /* Validar Ciudad */
  ciudad.addEventListener("input", function validarCiudad() {
    if (ciudad.value.trim() === "") {
      /* Campo requerido */
      setError(ciudad, m_campo_requerido);
    } else if (!ciudadEstadoRegex.test(ciudad.value.trim())) {
      /* Validación del formato Ciudad */
      setError(ciudad, m_ciudad_formato);
    } else if (ciudad.value.trim().length < 3) {
      /* Longitud mínima */
      setError(ciudad, m_longitud_min);
    } else if (ciudad.value.trim().length > longitud_max) {
      /* Longitud máxima */
      setError(ciudad, m_longitud_max);
    } else {
      setSuccess(ciudad, "");
    }
  });

  /* Validar Estado / Provincia */
  Estado_Provincia.addEventListener("input", function validarEstadoProvincia() {
    if (Estado_Provincia.value.trim() === "") {
      /* Campo requerido */
      setError(Estado_Provincia, m_campo_requerido);
    } else if (!ciudadEstadoRegex.test(Estado_Provincia.value.trim())) {
      /* Validación del formato Ciudad */
      setError(Estado_Provincia, m_provincia_formato);
    } else if (Estado_Provincia.value.trim().length < 3) {
      /* Longitud mínima */
      setError(Estado_Provincia, m_longitud_min);
    } else if (Estado_Provincia.value.trim().length > longitud_max) {
      /* Longitud máxima */
      setError(Estado_Provincia, m_longitud_max);
    } else {
      setSuccess(Estado_Provincia, "");
    }
  });

  /* Validar Cargo1 */
  Cargo1.addEventListener("click", function validarCargo1() {
    validarRequerido(Cargo1);
  });

  /* Validar Cargo2 */
  Cargo2.addEventListener("click", function validarCargo2() {
    validarRequerido(Cargo2);
  });

  /* Validar turno */
  turno.addEventListener("click", function validarTurno() {
    validarRequerido(turno);
  });

  /* Validar nivel_ingles */
  nivel_ingles.addEventListener("click", function validarNivelIngles() {
    validarRequerido(nivel_ingles);
  });

  /* Validar fecha_inicio */
  /* Si das click y no ingresas nada (vas a otro campo) */
  fecha_inicio.addEventListener("blur", function validarFechaInicioVacia() {
    if (fecha_inicio.value.trim() === "") {
      /* Campo requerido */
      setError(fecha_inicio, m_campo_requerido);
    }
  });

  /* Si los valores del input cambian */
  fecha_inicio.addEventListener("input", function validarFechaInicio() {
    var fecha_actual = new Date();
    var fecha_ingresada = new Date(fecha_inicio.value.trim());
    var diferencia_dias = Math.floor((fecha_actual - fecha_ingresada) / (1000 * 60 * 60 * 24));
    console.log(diferencia_dias);
    if (diferencia_dias <= -365) {
      /* Más de 1 año? */
      setError(fecha_inicio, m_fecha_inicio);
    } else if (diferencia_dias >= 0) {
      /* Fecha pasada */
      setError(fecha_inicio, m_fecha_inicio);
    } else {
      setSuccess(fecha_inicio, "");
    }
  });

  /* Validar transporte */
  Transporte.addEventListener("click", function validarTransporte() {
    validarRequerido(Transporte);
  });

  /* Validar Conociste */
  Conociste.addEventListener("click", function validarConociste() {
    validarRequerido(Conociste);
  });

  /* Validar referencia */
  referencia.addEventListener("input", function validarReferencia() {
    if (referencia.value.trim() === "") {
      /* La referencia no es requerida */
      setSuccess(referencia, "");
    } else if (!nombreContactoRegex.test(referencia.value.trim())) {
      /* Está incorrecto el formato "Nombre Apellido"? */
      setError(referencia, m_nombre_contacto_formato);
    } else if (referencia.value.trim().length > longitud_max) {
      /* Longitud máxima */
      setError(referencia, m_longitud_max);
    } else {
      setSuccess(referencia, "");
    }
  });
});
