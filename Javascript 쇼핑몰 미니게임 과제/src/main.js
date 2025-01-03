
//Fetch the items from the JSON file
function loadItems() {
    return fetch("data/data.json") //fetch하면 response을 불러옴(데이터를 받아옴)
        .then(response => response.json()) //받아온 데이터가 성공적이면, json으로 변환하고
        .then(json => json.items); //json 안에 있은 items을 return
}

// Update the list with the given items
function dispalyItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join(" ");
}

// Create HTML item from the given data item
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item_thumbnail">
        <span class="item_description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;
    
    if (key == null || value == null) {
        return;
    }
    const filtered = items.filter(item => item[key] === value);
    dispalyItems(filtered);
}

function setEventListeners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener("click", () => dispalyItems(items));
    buttons.addEventListener('click', envet => onButtonClick(envet, items));
}

// main
loadItems() //item들을 동적으로 받아와서
    .then(items => {  //성공적으로 값을 전달해주면, 전달받은 items을 이용해서 
        dispalyItems(items); //items을 보여주고
        setEventListeners(items) //EventListeners를 등록하여, 버튼을 클릭했을 때, 적절하게 필터링
    })
    .catch(console.log)