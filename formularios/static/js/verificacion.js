
function numeros(elementId) {
  document.getElementById(elementId).addEventListener('input', function (event) {
      // Eliminar caracteres no numéricos
      var inputValue = event.target.value.replace(/\D/g, '');
      // Limitar a 10 dígitos
      inputValue = inputValue.substring(0, 10);
      // Actualizar el valor del campo
      event.target.value = inputValue;
  });
}

numeros('Telefono1');
numeros('Telefono2');
numeros('Telefono3');
numeros('Codigo4');

$(document).ready(function () {
  // Muestra el modal al cargar la página
  $('#politicasModal').modal('show');

  // Cierra el modal cuando se hace clic en "Aceptar Políticas"
  $('#aceptarPoliticas').click(function () {
      $('#politicasModal').modal('hide');
  });
});

//validacion de campos
document.addEventListener("DOMContentLoaded",function(){
  var nombreInput = document.getElementById("nombre");
  var nombreErrorMessage = document.getElementById("nombre-error-message");

  var apellidoInput = document.getElementById("Apellido");
  var apellidoErrorMessage = document.getElementById("Apellido-error-message");

  var telefonoInput = document.getElementById("Telefono1");
  var telefonoErrorMessage = document.getElementById("telefono-error-message");

  nombreInput.addEventListener("input", function () {
      var nombreValue = nombreInput.value;
      var nombreLength = nombreValue.length;

      if (nombreLength > 2 && nombreLength <= 20) {
          nombreInput.setCustomValidity('');
          nombreErrorMessage.innerText = '';
      } else {
          nombreInput.setCustomValidity('Por favor, ingrese un nombre más de 2 caracteres');
          nombreErrorMessage.innerText = 'Por favor, ingrese un nombre más de 2 caracteres';
      }
  });

  apellidoInput.addEventListener("input", function () {
      var apellidoValue = apellidoInput.value;
      var apellidoLength = apellidoValue.length;

      if (apellidoLength > 2 && apellidoLength <= 20) {
          apellidoInput.setCustomValidity('');
          apellidoErrorMessage.innerText = '';
      } else {
          apellidoInput.setCustomValidity('Por favor, ingrese un apellido más de 2 caracteres');
          apellidoErrorMessage.innerText = 'Por favor, ingrese un apellido más de 2 caracteres';
      }
  });

  telefonoInput.addEventListener("input", function () {
      var telefonoValue = telefonoInput.value.replace(/\D/g, ''); // Eliminar caracteres no numéricos
      var telefonoLength = telefonoValue.length;

      if (telefonoLength === 7) {
          // El número de teléfono es válido
          telefonoInput.setCustomValidity('');
          telefonoErrorMessage.innerText = ''; // Limpiar el mensaje de error
      } else {
          // El número de teléfono no es válido, establecer un mensaje de error
          telefonoInput.setCustomValidity('Por favor, ingrese un número de teléfono válido de 7 dígitos.');
          telefonoErrorMessage.innerText = 'Por favor, ingrese un número de teléfono válido de 7 dígitos.';
      }
  });

  // Mostrar el mensaje de error cuando se intente enviar el formulario
  apellidoInput.addEventListener('invalid', function () {
      if (apellidoInput.validity.valueMissing) {
          apellidoInput.setCustomValidity('Este campo es obligatorio.');
          apellidoErrorMessage.innerText = 'Este campo es obligatorio.';
      }
  });

  telefonoInput.addEventListener('invalid', function () {
      if (telefonoInput.validity.valueMissing) {
          telefonoInput.setCustomValidity('Este campo es obligatorio.');
          telefonoErrorMessage.innerText = 'Este campo es obligatorio.';
      }
    });

    var form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        if (!apellidoInput.checkValidity()) {
            event.preventDefault();
        }
    });
    // Evitar que el formulario se envíe si el número de teléfono no es válido
    var form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        if (!telefonoInput.checkValidity()) {
            event.preventDefault();
        }
    });
});