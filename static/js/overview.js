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
    
    tableBody.replaceChildren();

    if (pickedCategories.length > 0) {
        fetch(`/goods_stock/${correctedCategories}`)
        .then(response => response.json())
        .then(data => fillTableWithReturnedData(data))
    }
}

function fillTableWithReturnedData(data) {

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

const obligatoryNewGoodsInputs = document.querySelectorAll('.goods-inserter .obligatory');
const addNewItemButton = document.getElementById("add-item-button");

addNewItemButton.addEventListener('click', e => {
    obligatoryNewGoodsInputs.forEach(input => {

        if (input.value == '') {
            e.preventDefault();
            input.style.border = '1px solid #E21D12';
            input.style.backgroundColor = '#FCD8D6';
        }
    })
});

const obligatoryUpdateGoodsInputs = document.querySelectorAll('.goods-updater .obligatory');
const updateItemButton = document.getElementById("update-item-button");

updateItemButton.addEventListener('click', e => {
    obligatoryUpdateGoodsInputs.forEach(input => {

        if (input.value == '') {
            e.preventDefault();
            input.style.border = '1px solid #E21D12';
            input.style.backgroundColor = '#FCD8D6';
        }
    })
});

const obligatoryDeleteGoodsInputs = document.querySelectorAll('.goods-deleter .obligatory');
const deleteItemButton = document.getElementById("delete-item-button");

deleteItemButton.addEventListener('click', e => {
    obligatoryDeleteGoodsInputs.forEach(input => {

        if (input.value == '') {
            e.preventDefault();
            input.style.border = '1px solid #E21D12';
            input.style.backgroundColor = '#FCD8D6';
        }
    })
});

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}