/* ReferenciaS a los elementos */
const aplicantes_form = document.getElementById("aplicantes_form");
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
const Cargo1 = document.getElementById("Cargo1");
const Cargo2 = document.getElementById("Cargo2");
const turno = document.getElementById("turno");
const nivel_ingles = document.getElementById("nivel_ingles");
const fecha_inicio = document.getElementById("fecha_inicio");
const Transporte = document.getElementById("Transporte");
const Conociste = document.getElementById("Conociste");
const referencia = document.getElementById("referencia");

const registro_form = document.getElementById("registro_form");
const usuario = document.getElementById("usuario");
/* hidden_pass_icon, showing_pass_icon, Contraseña and Contraseña1 declaration in show_hide_password.js */
const eight_char = document.getElementById("eight_char");
const numbers = document.getElementById("numbers");
const lower = document.getElementById("lower");
const upper = document.getElementById("upper");
const special = document.getElementById("special");
const pass_security_container = document.getElementById("pass_security_container");

const correo_recuperar_form = document.getElementById("correo_recuperar_form");
const correo_activacion_form = document.getElementById("correo_activacion_form");
const password_reset_form = document.getElementById("password_reset_form");

/* Inicialización de expresiones regulares */
const letrasRegex = /^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]+$/;
const numerosRegex = /^[0-9]+$/;
const nombreApellidoRegex = /^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]*$/;
const emailRegex = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
const espacioRegex = /^\s+$/;
const nombreContactoRegex = /^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+\s[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+$/;
const ciudadEstadoRegex = /^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]*$/;
const longitud_max = 30;

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
function validarRequerido(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

function validarTelefono(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (!numerosRegex.test(input.value.trim())) {
    /* Solo se aceptan números */
    setError(input, m_telefono_regex);
    return false;
  } else if (input.value.trim().length > 9) {
    /* Longitud máxima */
    setError(input, m_telefono_formato);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

function validarNombre(input) {
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
  } /* else if (nombre.value.trim().length < 3) {
    Longitud mínima 
    setError(nombre, m_longitud_min);
    return false;
  }*/ else if (input.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(input, m_longitud_max);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

function validarApellido() {
  if (apellido.value.trim() === "") {
    /* Campo requerido */
    setError(apellido, m_campo_requerido);
    return false;
  } else if (!nombreApellidoRegex.test(apellido.value.trim())) {
    /* Inicia con mayúscula? */
    setError(apellido, m_apellido_formato);
    return false;
  } else if (espacioRegex.test(apellido.value.trim())) {
    /* Escribió más de un apellido? */
    setError(apellido, m_apellido_formato);
    return false;
  } /*else if (apellido.value.trim().length < 3) {
     Longitud mínima 
    setError(apellido, m_longitud_min);
    return false;
  }*/ else if (apellido.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(apellido, m_longitud_max);
    return false;
  } else {
    setSuccess(apellido, "");
    return true;
  }
}

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

/* Valida el input de email, incluído correo ya registrado */
async function validarEmail(input, model, app) {
  /* Obtener el csrftoken */
  const csrftoken = document.cookie
    .split("; ")
    .find((row) => row.startsWith("csrftoken="))
    .split("=")[1];

  try {
    // Petición AJAX usando fetch, se manda el url da la vista temporal y el model que se quiere usar
    const modelName = model; // Nombre del modelo
    const appName = app; //Nombre de la aplicación donde está el modelo
    const url = `/obtener_emails/?model=${modelName}&app=${appName}`;
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken, // Don't forget to include the CSRF token
      },
    });

    // Supongamos que 'jsonListaCorreos' es tu lista en formato JSON
    let emails_list = await response.json();

    // Validaciones
    if (input.value.trim() === "") {
      /* Campo requerido */
      setError(input, m_campo_requerido);
      return false;
    } else if (emails_list.includes(input.value.trim())) {
      setError(input, m_correo_registrado);
      return false;
    } else if (input.value.trim().length > 30 || !emailRegex.test(input.value.trim())) {
      /* Longitud máxima - Formato ejemplo@email.com */
      setError(input, m_email_formato);
      return false;
    } else {
      setSuccess(input, "");
      return true;
    }
  } catch (error) {
    console.error("Error fetching registered emails:", error);
  }
}

/* Valida el input de email. Sin correo ya registrado */
function validarFormatoEmail(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (input.value.trim().length > 30 || !emailRegex.test(input.value.trim())) {
    /* Longitud máxima - Formato ejemplo@email.com */
    setError(input, m_email_formato);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

function validarFechaVacia(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else {
    return true;
  }
}

function validarFechaNacimiento() {
  var fecha_actual = new Date();
  var fecha_ingresada = new Date(fecha_nacimiento.value.trim());
  var diferencia_dias = Math.floor((fecha_actual - fecha_ingresada) / (1000 * 60 * 60 * 24));
  if (fecha_nacimiento.value.trim() === "") {
    /* Campo requerido */
    setError(fecha_nacimiento, m_campo_requerido);
    return false;
  } else if (diferencia_dias < 0) {
    /* Fecha futura? */
    setError(fecha_nacimiento, m_fecha_futura);
    return false;
  } else if (diferencia_dias < 6570) {
    /* Debes tener mínimo 18 años */
    setError(fecha_nacimiento, m_edad_minima);
    return false;
  } else {
    setSuccess(fecha_nacimiento, "");
    return true;
  }
}

function validarAlergia() {
  if (alergia.value.trim() === "") {
    /* Campo requerido */
    setError(alergia, m_campo_requerido);
    return false;
  } else if (!letrasRegex.test(alergia.value.trim())) {
    /* Formato de texto */
    setError(alergia, m_letras_regex);
    return false;
  } else if (alergia.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(alergia, m_longitud_max);
    return false;
  } else {
    setSuccess(alergia, "");
    return true;
  }
}

function validarNombreContacto() {
  if (nombre_contacto.value.trim() === "") {
    /* Campo requerido */
    setError(nombre_contacto, m_campo_requerido);
    return false;
  } else if (!nombreContactoRegex.test(nombre_contacto.value.trim())) {
    /* Está incorrecto el formato "Nombre Apellido"? */
    setError(nombre_contacto, m_nombre_contacto_formato);
    return false;
  } else if (nombre_contacto.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(nombre_contacto, m_longitud_max);
    return false;
  } else {
    setSuccess(nombre_contacto, "");
    return true;
  }
}

function validarDireccionSecundaria() {
  if (direccion_secundaria.value.trim() !== "") {
    /* La direccion_secundaria no es requerida. */
    setSuccess(direccion_secundaria, "");
    return true;
  } else {
    setSuccess(direccion_secundaria, "");
    return true;
  }
}

function validarCiudad() {
  if (ciudad.value.trim() === "") {
    /* Campo requerido */
    setError(ciudad, m_campo_requerido);
    return false;
  } else if (!ciudadEstadoRegex.test(ciudad.value.trim())) {
    /* Validación del formato Ciudad */
    setError(ciudad, m_ciudad_formato);
    return false;
  } /*else if (ciudad.value.trim().length < 3) {
     Longitud mínima 
    setError(ciudad, m_longitud_min);
    return false;
  }*/ else if (ciudad.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(ciudad, m_longitud_max);
    return false;
  } else {
    setSuccess(ciudad, "");
    return true;
  }
}

function validarEstadoProvincia() {
  if (Estado_Provincia.value.trim() === "") {
    /* Campo requerido */
    setError(Estado_Provincia, m_campo_requerido);
    return false;
  } else if (!ciudadEstadoRegex.test(Estado_Provincia.value.trim())) {
    /* Validación del formato Ciudad */
    setError(Estado_Provincia, m_provincia_formato);
    return false;
  } /*else if (Estado_Provincia.value.trim().length < 3) {
     Longitud mínima 
    setError(Estado_Provincia, m_longitud_min);
    return false;
  }*/ else if (Estado_Provincia.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(Estado_Provincia, m_longitud_max);
    return false;
  } else {
    setSuccess(Estado_Provincia, "");
    return true;
  }
}

function validarFechaInicio() {
  var fecha_actual = new Date();
  var fecha_ingresada = new Date(fecha_inicio.value.trim());
  var diferencia_dias = Math.floor((fecha_actual - fecha_ingresada) / (1000 * 60 * 60 * 24));
  if (fecha_inicio.value.trim() === "") {
    /* Campo requerido */
    setError(fecha_inicio, m_campo_requerido);
    return false;
  } else if (diferencia_dias <= -365) {
    /* Más de 1 año? */
    setError(fecha_inicio, m_fecha_inicio);
    return false;
  } else if (diferencia_dias >= 0) {
    /* Fecha pasada */
    setError(fecha_inicio, m_fecha_inicio);
    return false;
  } else {
    setSuccess(fecha_inicio, "");
    return true;
  }
}

function validarReferencia() {
  if (referencia.value.trim() === "") {
    /* La referencia no es requerida. */
    setSuccess(referencia, "");
    return true;
  } else if (!nombreContactoRegex.test(referencia.value.trim())) {
    /* Está incorrecto el formato "Nombre Apellido"? */
    setError(referencia, m_nombre_contacto_formato);
    return false;
  } else if (referencia.value.trim().length > longitud_max) {
    /* Longitud máxima */
    setError(referencia, m_longitud_max);
    return false;
  } else {
    setSuccess(referencia, "");
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

function validarContraseña(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (espacioRegex.test(input.value.trim())) {
    /* Ingresó algún espacio? */
    setError(input, m_contrasena_space);
    return false;
  } else {
    /* Si no está vacío o tiene algún espacio, revisa el formato de seguridad */
    /* inicialización de variables de verificación */
    var v_eight_char = false,
      v_numbers = false,
      v_numbers = false,
      v_lower = false,
      v_upper = false,
      v_special = false;
    /* Más de 8 caracteres? */
    if (input.value.trim().length >= 8) {
      eight_char.classList.remove("text-gray-400");
      eight_char.classList.add("text-lime-500");
      v_eight_char = true;
    } else {
      eight_char.classList.add("text-gray-400");
      eight_char.classList.remove("text-lime-500");
      v_eight_char = false;
    }
    /* Contiene números? */
    var regex = /\d/;
    if (regex.test(input.value.trim())) {
      numbers.classList.remove("text-gray-400");
      numbers.classList.add("text-lime-500");
      v_numbers = true;
    } else {
      numbers.classList.add("text-gray-400");
      numbers.classList.remove("text-lime-500");
      v_numbers = false;
    }
    /* Contiene lower case? */
    var regex = /[a-z]/;
    if (regex.test(input.value.trim())) {
      lower.classList.remove("text-gray-400");
      lower.classList.add("text-lime-500");
      v_lower = true;
    } else {
      lower.classList.add("text-gray-400");
      lower.classList.remove("text-lime-500");
      v_lower = false;
    }
    /* Contiene upper case? */
    var regex = /[A-Z]/;
    if (regex.test(input.value.trim())) {
      upper.classList.remove("text-gray-400");
      upper.classList.add("text-lime-500");
      v_upper = true;
    } else {
      upper.classList.add("text-gray-400");
      upper.classList.remove("text-lime-500");
      v_upper = false;
    }
    /* Contiene caracteres especiales? */
    var regex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
    if (regex.test(input.value.trim())) {
      special.classList.remove("text-gray-400");
      special.classList.add("text-lime-500");
      v_special = true;
    } else {
      special.classList.add("text-gray-400");
      special.classList.remove("text-lime-500");
      v_special = false;
    }

    /* Si verif es true significa que todo se cumple */
    if (v_eight_char == true && v_numbers == true && v_lower == true && v_upper == true && v_special == true) {
      setSuccess(input, "");
      return true;
    } else {
      setError(input, m_contrasena_formato);
      return false;
    }
  }
}

function validarContraseña1(input) {
  if (input.value.trim() === "") {
    /* Campo requerido */
    setError(input, m_campo_requerido);
    return false;
  } else if (input.value.trim() !== Contraseña.value.trim()) {
    /* Las contraseñas no son iguales? */
    setError(input, m_contrasena_match);
    return false;
  } else {
    setSuccess(input, "");
    return true;
  }
}

/* Si APLICANTES_FORM está presente*/
if (aplicantes_form) {
  /* Validaciones en tiempo real de APLICANTES_FORM en formulario.html  */
  document.addEventListener("DOMContentLoaded", function () {
    /* Validar nombre */
    nombre.addEventListener("input", function () {
      validarNombre(nombre);
    });

    /* Validar apellido */
    apellido.addEventListener("input", function () {
      validarApellido();
    });

    /* Validar email */
    email.addEventListener("input", function () {
      validarEmail(email, "Usuario", "formularios");
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
    fecha_nacimiento.addEventListener("blur", function () {
      validarFechaVacia(fecha_nacimiento);
    });
    /* Si los valores del input cambian */
    fecha_nacimiento.addEventListener("input", function () {
      validarFechaNacimiento();
    });

    /* Validar discapacidad / alergia */
    alergia.addEventListener("input", function () {
      validarAlergia();
    });

    /* id_file se valida al mandar el formulario */

    /* cv_file se valida al mandar el formulario */

    /* Validar codigo1 */
    codigo1.addEventListener("click", function () {
      validarRequerido(codigo1);
    });

    /* Validar Telefono1 */
    Telefono1.addEventListener("input", function (event) {
      // Eliminar caracteres no numéricos
      var inputValue = event.target.value.replace(/\D/g, "");
      // Actualizar el valor del campo
      event.target.value = inputValue;
      validarTelefono(Telefono1);
    });

    /* Validar codigo3 */
    codigo3.addEventListener("click", function () {
      validarRequerido(codigo3);
    });

    /* Validar telefono_emergencia */
    telefono_emergencia.addEventListener("input", function (event) {
      // Eliminar caracteres no numéricos
      var inputValue = event.target.value.replace(/\D/g, "");
      // Actualizar el valor del campo
      event.target.value = inputValue;
      validarTelefono(telefono_emergencia);
    });

    /* Validar codigo2 */
    codigo2.addEventListener("click", function () {
      validarRequerido(codigo2);
    });

    /* Validar Telefono2 */
    Telefono2.addEventListener("input", function (event) {
      // Eliminar caracteres no numéricos
      var inputValue = event.target.value.replace(/\D/g, "");
      // Actualizar el valor del campo
      event.target.value = inputValue;
      validarTelefono(Telefono2);
    });

    /* Validar nombre_contacto */
    nombre_contacto.addEventListener("input", function () {
      validarNombreContacto();
    });

    /* Validar direccion_principal */
    direccion_principal.addEventListener("input", function () {
      validarRequerido(direccion_principal);
    });

    /* Validar direccion_secundaria. No es requerida */
    direccion_secundaria.addEventListener("input", function () {
      validarDireccionSecundaria();
    });

    /* Validar Ciudad */
    ciudad.addEventListener("input", function () {
      validarCiudad();
    });

    /* Validar Estado / Provincia */
    Estado_Provincia.addEventListener("input", function () {
      validarEstadoProvincia();
    });

    /* Validar Cargo1 */
    Cargo1.addEventListener("click", function () {
      validarRequerido(Cargo1);
    });

    /* Validar Cargo2 */
    Cargo2.addEventListener("click", function () {
      validarRequerido(Cargo2);
    });

    /* Validar turno */
    turno.addEventListener("click", function () {
      validarRequerido(turno);
    });

    /* Validar nivel_ingles */
    nivel_ingles.addEventListener("click", function () {
      validarRequerido(nivel_ingles);
    });

    /* Validar fecha_inicio */
    /* Si das click y no ingresas nada (vas a otro campo) */
    fecha_inicio.addEventListener("blur", function () {
      validarFechaVacia(fecha_inicio);
    });
    /* Si los valores del input cambian */
    fecha_inicio.addEventListener("input", function () {
      validarFechaInicio();
    });

    /* Validar transporte */
    Transporte.addEventListener("click", function () {
      validarRequerido(Transporte);
    });

    /* Validar Conociste */
    Conociste.addEventListener("click", function () {
      validarRequerido(Conociste);
    });

    /* Validar referencia. No es requerida */
    referencia.addEventListener("input", function () {
      validarReferencia();
    });
  });

  /*Validaciones a los inputs de APLICANTES_FORM en formulario.html al presionar submit. Previene submit con datos erróneos. */
  aplicantes_form.addEventListener("submit", (e) => {
    // Previene el envío predeterminado
    e.preventDefault();

    /* Se asigna cada función que retorna true or false a una variable de validación general.*/
    const esFormularioValido = validarNombre(nombre) && validarApellido() && validarEmail(email, "Usuario", "formularios") && validarRequerido(genero) && validarRequerido(nacionalidad) && validarFechaVacia(fecha_nacimiento) && validarFechaNacimiento() && validarAlergia() && validarRequerido(id_file) && validarRequerido(cv_file) && validarRequerido(codigo1) && validarTelefono(Telefono1) && validarRequerido(codigo3) && validarTelefono(telefono_emergencia) && validarRequerido(codigo2) && validarTelefono(Telefono2) && validarNombreContacto() && validarRequerido(direccion_principal) && validarDireccionSecundaria() && validarCiudad() && validarEstadoProvincia() && validarRequerido(Cargo1) && validarRequerido(Cargo2) && validarRequerido(turno) && validarRequerido(nivel_ingles) && validarFechaVacia(fecha_inicio) && validarFechaInicio() && validarRequerido(Transporte) && validarRequerido(Conociste) && validarReferencia();

    /* Si el correo no está repetido y el resto del form es válido, mándalo a la bd */
    if (esFormularioValido) {
      aplicantes_form.submit();
    }
  });
}

/* Si REGISTRO_FORM está presente */
if (registro_form) {
  /* Validaciones en tiempo real de REGISTRO_FORM en registro.html  */
  document.addEventListener("DOMContentLoaded", function () {
    /* Validar nombre */
    nombre.addEventListener("input", function () {
      validarNombreApellido(nombre);
    });

    /* Validar apellido */
    apellido.addEventListener("input", function () {
      validarNombreApellido(apellido);
    });

    /* Validar usuario */
    usuario.addEventListener("input", function () {
      validarUsuario(usuario);
    });

    /* Validar email */
    email.addEventListener("input", function () {
      validarEmail(email, "User", "auth_users");
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

    /* Validar repetir contraseña (Contraseña1) */
    Contraseña1.addEventListener("input", function () {
      validarContraseña1(Contraseña1);
    });
  });

  /*Validaciones a los inputs de REGISTRO_FORM en registro.html al presionar submit. Previene submit con datos erróneos. */
  registro_form.addEventListener("submit", (e) => {
    // Previene el envío predeterminado
    e.preventDefault();

    /* Se asigna cada función que retorna true or false a una variable de validación general.*/
    const esFormularioValido = validarNombreApellido(nombre) && validarNombreApellido(apellido) && validarUsuario(usuario) && validarEmail(email, "User", "auth_users") && validarContraseña(Contraseña) && validarContraseña1(Contraseña1);

    /* Si el correo no está repetido y el resto del form es válido, mándalo a la bd */
    if (esFormularioValido) {
      registro_form.submit();
    }
  });
}

/* Si CORREO_RECUPERAR_FORM está presente */
if (correo_recuperar_form) {
  /*Validaciones en tiempo real de CORREO_RECUPERAR_FORM en formulario.html */
  document.addEventListener("DOMContentLoaded", function () {
    /* Validar email */
    email.addEventListener("input", function () {
      validarFormatoEmail(email);
    });
  });

  /*Validaciones a los inputs de CORREO_RECUPERAR_FORM en recuperar.html al presionar submit. Previene submit con datos erróneos. */
  if (correo_recuperar_form) {
    correo_recuperar_form.addEventListener("submit", (e) => {
      // Previene el envío predeterminado
      e.preventDefault();

      /* Se asigna cada función que retorna true or false a una variable de validación general.*/
      const esFormularioValido = validarFormatoEmail(email);

      /* Si el correo no está repetido y el resto del form es válido, mándalo a la bd */
      if (esFormularioValido) {
        correo_recuperar_form.submit();
      }
    });
  }
}

/* Si CORREO_ACTIVACION_FORM está presente */
if (correo_activacion_form) {
  /*Validaciones en tiempo real de CORREO_ACTIVACION_FORM en activacion.html */
  document.addEventListener("DOMContentLoaded", function () {
    /* Validar email */
    email.addEventListener("input", function () {
      validarFormatoEmail(email);
    });
  });

  /*Validaciones a los inputs de CORREO_ACTIVACION_FORM en activacion.html al presionar submit. Previene submit con datos erróneos. */
  if (correo_activacion_form) {
    correo_activacion_form.addEventListener("submit", (e) => {
      // Previene el envío predeterminado
      e.preventDefault();

      /* Se asigna cada función que retorna true or false a una variable de validación general.*/
      const esFormularioValido = validarFormatoEmail(email);

      /* Si el correo no está repetido y el resto del form es válido, mándalo a la bd */
      if (esFormularioValido) {
        correo_activacion_form.submit();
      }
    });
  }
}

/* Si password_reset_form está presente */
if (password_reset_form) {
  /* Validaciones en tiempo real de password_reset_form en password_reset_confirm.html  */
  document.addEventListener("DOMContentLoaded", function () {
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

    /* Validar repetir contraseña (Contraseña1) */
    Contraseña1.addEventListener("input", function () {
      validarContraseña1(Contraseña1);
    });
  });

  /*Validaciones a los inputs de password_reset_form en password_reset_confirm.html al presionar submit. Previene submit con datos erróneos. */
  password_reset_form.addEventListener("submit", (e) => {
    // Previene el envío predeterminado
    e.preventDefault();

    /* Se asigna cada función que retorna true or false a una variable de validación general.*/
    const esFormularioValido = validarContraseña(Contraseña) && validarContraseña1(Contraseña1);

    /* Si el correo no está repetido y el resto del form es válido, mándalo a la bd */
    if (esFormularioValido) {
      password_reset_form.submit();
    }
  });
}
