const registerButton = document.getElementById('register');

registerButton.addEventListener('click', () => window.location.href = '/register');

const inputFields = document.querySelectorAll('input');
const modalAlert = document.querySelector('.custom-alert');
const submitButton = document.getElementById('submit-btn');
const confirmButton = document.getElementById('confirm-btn');

submitButton.addEventListener('click', e => {

    inputFields.forEach(input => {
        if (input.value == '') {
            e.preventDefault();
            modalAlert.style.display = 'block';
            modalAlert.animate([
                {'top': '-10em'},
                {'top': '1em'}
            ],
            {
                duration: 600,
                fill: 'forwards'
            })
        }
    });
})

confirmButton.addEventListener('click', () => modalAlert.style.display = 'none');

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}