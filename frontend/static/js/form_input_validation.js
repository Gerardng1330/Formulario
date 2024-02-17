/* Referencias de todos los inputs del form */
const form = document.getElementById("form");
const inputs = form.querySelectorAll("input"); /* Todos los inputs del form */
const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const email = document.getElementById("email");
const fecha_nacimiento = document.getElementById("fecha_nacimiento");
const alergia = document.getElementById("alergia");
const id_file = document.getElementById("id_file");
const cv_file = document.getElementById("cv_file");
const Telefono1 = document.getElementById("Telefono1");
const telefono_emergencia = document.getElementById("telefono_emergencia");
const Telefono2 = document.getElementById("Telefono2");
const nombre_contacto = document.getElementById("nombre_contacto");
const direccion_principal = document.getElementById("direccion_principal");
const direccion_secundaria = document.getElementById("direccion_secundaria");
const ciudad = document.getElementById("ciudad");
const Estado_Provincia = document.getElementById("Estado_Provincia");
const codigo_postal = document.getElementById("codigo_postal");
const fecha_inicio = document.getElementById("fecha_inicio");
const referencia = document.getElementById("referencia");

/* Previene que el form se envíe antes de validar los inputs.
Se ejecuta cuando se da click al botón APLICAR AHORA */
form.addEventListener("submit", (e) => {
  e.preventDefault();
  validarInputs();
});

/* Permite la validación a tiempo real.
Se ejecuta cuando cualquier valor de cualquier input dentro del form, cambia. */
form.addEventListener("input", (e) => {
  validarInputs();
});

/* Función que recibe un elemento html (el input) y un mensaje a mostrar (que se trae del html como variable, para permitir la internacionalización */
const setError = (element, message) => {
  const input_control = element.parentElement; /* Referencia de la div padre del input proporcionado */
  const message_display = input_control.querySelector(".message"); /* Referencia al span donde va el mensaje */
  message_display.innerText = message; /* Le asignamos el mensaje a mostrar en el span */
  message_display.classList.add("text-red"); /* Color de texto rojo para denotar error */
  message_display.classList.remove("text-lime-500");
  message_display.classList.remove("hidden"); /* Le quitamos la clase hidden para mostrar el mensaje */
};

/* Función que recibe un elemento html (el input) y un mensaje a mostrar (que se trae del html como variable, para permitir la internacionalización */
const setSuccess = (element, message) => {
  const input_control = element.parentElement; /* Referencia de la div padre del input proporcionado */
  const message_display = input_control.querySelector(".message"); /* Referencia al span donde va el mensaje */
  message_display.innerText = message; /* Le asignamos el mensaje a mostrar en el span */
  message_display.classList.add("text-lime-500"); /* Color de texto verde para denotar éxito */
  message_display.classList.remove("text-red");
  message_display.classList.remove("hidden"); /* Le quitamos la clase hidden para mostrar el mensaje */
};

/* Función para validar los inputs */
const validarInputs = () => {
  /* Obtenemos los valores de todos los inputs */
  const nombre_value = nombre.value.trim();
  const apellido_value = apellido.value.trim();
  const email_value = email.value.trim();
  const fecha_nacimiento_value = fecha_nacimiento.value.trim();
  const alergia_value = alergia.value.trim();
  const id_file_value = id_file.value.trim();
  const cv_file_value = cv_file.value.trim();
  const Telefono1_value = Telefono1.value.trim();
  const telefono_emergencia_value = telefono_emergencia.value.trim();
  const Telefono2_value = Telefono2.value.trim();
  const nombre_contacto_value = nombre_contacto.value.trim();
  const direccion_principal_value = direccion_principal.value.trim();
  const direccion_secundaria_value = direccion_secundaria.value.trim();
  const ciudad_value = ciudad.value.trim();
  const Estado_Provincia_value = Estado_Provincia.value.trim();
  const codigo_postal_value = codigo_postal.value.trim();
  const fecha_inicio_value = fecha_inicio.value.trim();
  const referencia_value = referencia.value.trim();

  /* ############ Validaciones ############ */
  /* Validación de cada campo required */
  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].value.trim() === "") {
      setError(inputs[i], "No puede dejar esta campo vacío");
      inputs[i].classList.add("border-red");
      inputs[i].classList.remove("border-gray-300");
      inputs[i].classList.remove("border-lime-500");
    }
  }

  /*   if (nombre_value === "" || apellido_value === "" || email_value === "" || fecha_nacimiento_value === "" || id_file_value === "" || cv_file_value === "" || Telefono1_value === "" || telefono_emergencia_value === "" || Telefono2_value === "" || nombre_contacto_value === "" || direccion_principal_value === "" || direccion_secundaria_value === "" || ciudad_value === "" || Estado_Provincia_value === "" || codigo_postal_value === "" || fecha_inicio_value === "") {
    setError(nombre, "Por favor, rellene el campo");
    nombre.classList.add("border-red");
    nombre.classList.remove("border-gray-300");
    nombre.classList.remove("border-lime-500");
  }  else {
    setSuccess(nombre, "Nombre correcto");
    nombre.classList.add("border-lime-500");
    nombre.classList.remove("border-gray-300");
    nombre.classList.remove("border-red");
  } */
};
