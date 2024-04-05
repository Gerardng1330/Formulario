/* Referencias de los elementos de formulario.html */
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

/* Validaciones en tiempo real de formulario.html */
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
    validarEmail(email);
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

/* Previene que el form se envíe antes de validar los inputs.
  Se ejecuta cuando se da click al botón APLICAR AHORA */
aplicantes_form.addEventListener("submit", (e) => {
  // Previene el envío predeterminado
  e.preventDefault();

  /* Se asigna cada función que retorna true or false a una variable de validación general.*/
  const esFormularioValido = validarNombre(nombre) && validarApellido() && validarEmail(email) && validarRequerido(genero) && validarRequerido(nacionalidad) && validarFechaVacia(fecha_nacimiento) && validarFechaNacimiento() && validarAlergia() && validarRequerido(id_file) && validarRequerido(cv_file) && validarRequerido(codigo1) && validarTelefono(Telefono1) && validarRequerido(codigo3) && validarTelefono(telefono_emergencia) && validarRequerido(codigo2) && validarTelefono(Telefono2) && validarNombreContacto() && validarRequerido(direccion_principal) && validarDireccionSecundaria() && validarCiudad() && validarEstadoProvincia() && validarRequerido(Cargo1) && validarRequerido(Cargo2) && validarRequerido(turno) && validarRequerido(nivel_ingles) && validarFechaVacia(fecha_inicio) && validarFechaInicio() && validarRequerido(Transporte) && validarRequerido(Conociste) && validarReferencia();

  /* Si el correo no está repetido y el resto del form es válido, mándalo a la bd */
  if (esFormularioValido) {
    aplicantes_form.submit();
  }
});
