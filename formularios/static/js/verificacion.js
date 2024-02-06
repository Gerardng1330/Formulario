//elimina los caracteres a los telefonos
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
  numeros('telefono_emergencia');
  numeros('codigo_postal');
  
  $(document).ready(function () {
    // Muestra el modal al cargar la página
    $('#politicasModal').modal('show');
  
    // Cierra el modal cuando se hace clic en "Aceptar Políticas"
    $('#aceptarPoliticas').click(function () {
        $('#politicasModal').modal('hide');
    });
  });
  
  document.addEventListener("DOMContentLoaded", function () {
    // Función reutilizable para validar campos
    function validarCampo(input, mensajeError) {
        input.addEventListener("input", function () {
            var valor = input.value.trim(); // Eliminar espacios en blanco al principio y al final
            var longitud = valor.length;
  
            if (longitud > 2 && longitud <20) {
                input.setCustomValidity('');
                mensajeError.innerText = '';
            } else {
                input.setCustomValidity('Debe llenar este campo');
                mensajeError.innerText = 'Debe llenar este campo';
            }
        });
    }
  
    function validarTelefonos(input,mensajeError){
      input.addEventListener("input", function () {
        var valor = input.value.trim(); // Eliminar espacios en blanco al principio y al final
        var longitud = valor.length;
  
        if (longitud > 2 && longitud <20) {
            input.setCustomValidity('');
            mensajeError.innerText = '';
        } else {
            input.setCustomValidity('Por favor, ingrese un número de teléfono válido de 7 dígitos.');
            mensajeError.innerText = 'Por favor, ingrese un número de teléfono válido de 7 dígitos.';
        }
    });
    }
    
    
   
    // Obtener referencias a los elementos de referencia y comentario
  
    var nombreInput = document.getElementById("nombre");
    var nombreErrorMessage = document.getElementById("nombre-error-message");
  
    var apellidoInput = document.getElementById("Apellido");
    var apellidoErrorMessage = document.getElementById("Apellido-error-message");
  
    var alergiaInput = document.getElementById("alergia");
    var alergiaErrorMessage = document.getElementById("alergia-error-message");
  
    var ReferidoInput = document.getElementById("Referido");
    var ReferidoErrorMessage = document.getElementById("Referido-error-message");
  
    var telefono1Input = document.getElementById("Telefono1");
    var telefono1ErrorMessage = document.getElementById("Telefono1-error-message")
  
    var telefono2Input = document.getElementById("Telefono2");
    var telefono2ErrorMessage = document.getElementById("Telefono2-error-message")
  
    var telefono3Input = document.getElementById("telefono_emergencia");
    var telefono3ErrorMessage = document.getElementById("Telefono3-error-message")
  
    var direccion1Input = document.getElementById("Direccion1");
    var direccion1ErrorMessage = document.getElementById("Direccion1-error-message")
  
    var direccion2Input = document.getElementById("Direccion2");
    var direccion2ErrorMessage = document.getElementById("Direccion2-error-message")
  
    // Aplicar la lógica y mensajes de error a ambos campos
    
    validarCampo(nombreInput, nombreErrorMessage);
    validarCampo(apellidoInput, apellidoErrorMessage);
    validarCampo(alergiaInput, alergiaErrorMessage);
    validarCampo(ReferidoInput, ReferidoErrorMessage);
    validarCampo(direccion1Input,direccion1ErrorMessage);
    validarCampo(direccion2Input,direccion2ErrorMessage);
    validarTelefonos(telefono1Input, telefono1ErrorMessage);
    validarTelefonos(telefono2Input, telefono2ErrorMessage);
    validarTelefonos(telefono3Input, telefono3ErrorMessage);
  });
  