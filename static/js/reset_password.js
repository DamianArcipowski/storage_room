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
    })
})

confirmButton.addEventListener('click', () => modalAlert.style.display = 'none');

const previousPageButton = document.getElementById('previous-page');

previousPageButton.addEventListener('click', () => window.location.href = '/');

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}