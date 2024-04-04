// Obtén todos los elementos <a> dentro del menú desplegable de idiomas
var itemsIdiomas = document.querySelectorAll("#dropdownIdiomas a");

// Adjunta el evento de clic a cada elemento <a>
itemsIdiomas.forEach(function (item) {
  item.addEventListener("click", function (event) {
    // Evitar que el enlace se abra
    event.preventDefault();

    // Envía los datos del formulario al cambiar de idioma
    var formulario = document.getElementById("form");
    var datosFormulario = new FormData(formulario);
    var idiomaSeleccionado = this.getAttribute("href").split("/")[1];

    // Realiza una solicitud POST al servidor con los datos del formulario y el idioma seleccionado
    fetch("/formulario_enviado/", {
      method: "POST",
      body: datosFormulario,
    }).then(function (response) {
      // Redirige a la nueva página con el idioma seleccionado
      window.location.href = "/formulario_idioma/?idioma=" + idiomaSeleccionado;
    });
  });
});
