const categoryCheckboxes = document.querySelectorAll('input[type=checkbox]');
const tableBody = document.querySelector('tbody');

categoryCheckboxes.forEach(box => {
    box.addEventListener('click', fetchGoodsStockFromDatabase);
})

function getAllTickedCategories() {
    let tickedBoxes = [];

    categoryCheckboxes.forEach(box => {
        
        if (box.checked == true) {
            tickedBoxes.push(box.previousElementSibling.textContent);
        }
    })

    return tickedBoxes;
}

function fetchGoodsStockFromDatabase() {
    const pickedCategories = getAllTickedCategories();
    let categoriesString = new String();

    for (let i = 0; i < pickedCategories.length; i++) {
        categoriesString += `'${pickedCategories[i]}', `;
    }

    let lastComma = categoriesString.lastIndexOf(',');
    let correctedCategories = categoriesString.substring(0, lastComma);
    
    clearTableBody();

    if (pickedCategories.length > 0) {
        fetch(`/goods_stock/${correctedCategories}`)
        .then(response => response.json())
        .then(data => fillTableWithReturnedData(data))
    }
}

function fillTableWithReturnedData(data) {
    clearTableBody();

    for (let i = 0; i < data.length; i++) {
        let row = document.createElement('tr');
        
        for (let j = 0; j < data[i].length; j++) {

            let cell = document.createElement('td');
            cell.textContent = data[i][j];
            row.appendChild(cell);
        }

        tableBody.appendChild(row);
    }
}

function clearTableBody() {
    const existingRows = tableBody.children;

    for (let i = 0; i < existingRows.length; i++) {
        tableBody.removeChild(existingRows[i]);
    }
}