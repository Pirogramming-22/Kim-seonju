let attempts = 9; //const : 재할당 X -> let 사용
let answer = [];

window.onload = initGame;

//게임 초기화 함수
function initGame() {
    attempts = 9;
    document.getElementById('attempts').innerText = attempts;

    answer = generateRandomNumbers(); 
    //console.log("정답: ", answer);

    clearInput();

    document.getElementById("results").innerHTML = ""; //**innerHTML**은 HTML 태그까지 포함한 전체 내용을 다룸
    document.getElementById("game-result-img").src = ""; //이미지가 표시되지 않도록

}

//중복되지 않는 랜덤 숫자 3개 생성함수
function generateRandomNumbers() {
    const numbers = [];
    while (numbers.length < 3) {
        const num = Math.floor(Math.random() * 10); //Math.random(): 0이상 1미만의 실수 생성 / Math.floor(): 소수점을 버려 정수를 반환 / Math.random() * 10 : 0이상 10미만 = 0~9
        if (!numbers.includes(num)) {               //중복 방지
            numbers.push(num);
        }
    }
    return numbers;
}

//입력 초기화 함수
//value: 입력 값(input) vs innterText: 태그 안의 텍스트 콘텐츠 (div, span, p)
function clearInput() {
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
    document.getElementById("number1").focus();
}

//숫자 확인 함수
function check_numbers() {
    let input1 = document.getElementById('number1').value;
    let input2 = document.getElementById('number2').value;
    let input3 = document.getElementById('number3').value;

    if (!isValidInput(input1) || !isValidInput(input2) || !isValidInput(input3)) {
        clearinput();
        return;
    }

    //입력값을 숫자 배열(정수)로 변환
    //**parseInt** : 문자열을 정수로 변환 !
    let guess = [parseInt(input1), parseInt(input2), parseInt(input3)];

    let result = calculateResult(guess);

    displayResult(guess,result);

    //시도 횟수 감소
    attempts--;
    document.getElementById('attempts').innerText = attempts;
    
    checkGameOver(result);

}

//입력 검증 함수
function isValidInput(input) {
    if (input !== "" && !isNaN(input) && 0 <= input && input <= 9) { // **isNaN**은 "Not-a-Number"를 판별하는 함수, !isNaN(input)는 input이 숫자이거나 숫자로 변환 가능한 값
        return true;
    }
    return false;
}

//결과 계산 함수
function calculateResult(guess) {
    let strike = 0;
    let ball = 0;

    for (let i=0; i<3; i++) {
        if (guess[i] === answer[i]) {
            strike++; //위치와 숫자 모두 일치
        }
        else if (answer.includes(guess[i])) {
            ball++; //위치는 다르지만 숫자만 일치
        }
    }

    return {strike, ball};
}

//결과 출력 함수
function displayResult(guess, result) {
    let resultDiv = document.getElementById('results');
    let resultText = document.createElement("p") // <p> 요소 생성
    resultText.textContent = `${guess.join(" ")} : ${result.strike} S ${result.ball} B`; //texContent : 텍스트 값 설정
    resultDiv.appendChild(resultText);
}

//게임 종료 확인 함수
function checkGameOver(result) {
    let resultImg = document.getElementById("game-result-img");

    if (result.strike === 3) {
        resultImg.src = "success.png";
        disableGame();
    }
    else if (attempts <= 0) {
        resultImg.src = "fail.png";
        disableGame();
    }

}

//게임 종료 시 버튼 비활성화
//querySelector : CSS 선택자를 사용(.submit-button/#submit-button/button.submit-button)
//**.disabled = true ** : 선택된 요소의 disabled 속성을 true로 설정하여 버튼을 비활성화
function disableGame() {
    document.querySelector(".submit-button").disabled = true;
}
