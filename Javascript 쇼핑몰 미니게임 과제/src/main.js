
//Fetch the items from the JSON file
function loadItems() {
    return fetch("data/data.json") //fetch하면 response을 불러옴(데이터를 받아옴)
    .then(response => response.json()) //받아온 데이터가 성공적이면, json으로 변환하고
    .then(json => json.items); //json 안에 있은 items을 return
}


// main
loadItems() //item들을 동적으로 받아와서
    .then(items => {  //성공적으로 값을 전달해주면, 전달받은 items을 이용해서 
        console.log(items);
        //dispalyItems(items); //items을 보여주고
        //setEventListeners(items) //EventListeners를 등록하여, 버튼을 클릭했을 때, 적절하게 필터링
    })
    .catch(console.log)