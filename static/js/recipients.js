const magnifier = document.querySelector('.bi-search');
const searchField = document.querySelector('.search-field');
const tableRows = document.querySelectorAll('tbody tr');

magnifier.addEventListener('click', () => {
    searchField.classList.toggle('visible-magnifier');

    setTimeout(() => {
        searchField.style.visibility = 'visible';
        searchField.animate([
            { width: '0px' },
            { width: '80%' }
        ], 
        {
            duration: 500,
            fill: 'forwards'
        })
    }, 200);
})

searchField.addEventListener('keyup', () => {
    let searchText = searchField.value.toLowerCase();

    for (let i = 0; i < tableRows.length; i++) {
        let surname = tableRows[i].children[1].textContent.toLowerCase();

        if (!surname.includes(searchText)) {
            tableRows[i].style.display = 'none';
        } else {
            tableRows[i].style.display = 'table-row';
        }
    }
})

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}