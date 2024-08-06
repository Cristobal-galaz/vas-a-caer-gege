document.addEventListener('DOMContentLoaded', function() {
    // Manejo del modal de cliente y empresa
    document.getElementById('cliente-btn').addEventListener('click', function() {
        $('#cliente-modal').modal('show');
    });

    document.getElementById('empresa-btn').addEventListener('click', function() {
        $('#empresa-modal').modal('show');
    });

    // Manejo del modal de pago
    document.getElementById('pay-btn').addEventListener('click', function() {
        $('#payment-modal').modal('show');
    });

    // Cierra el modal cuando se hace clic en el botón de cierre
    document.querySelectorAll('.close').forEach(function(closeButton) {
        closeButton.addEventListener('click', function() {
            $('.modal').modal('hide');
        });
    });

    // Manejo de los formularios de login (solo como ejemplo, adapta según tu lógica)
    const clienteLoginForm = document.getElementById('cliente-login-form');
    if (clienteLoginForm) {
        clienteLoginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Aquí puedes agregar la lógica para autenticar al cliente
            alert('Cliente logueado con éxito');
        });
    }

    const empresaLoginForm = document.getElementById('empresa-login-form');
    if (empresaLoginForm) {
        empresaLoginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Aquí puedes agregar la lógica para autenticar a la empresa
            alert('Empresa logueada con éxito');
        });
    }
});
