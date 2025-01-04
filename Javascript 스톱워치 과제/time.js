const timeDisplay = document.getElementById("time");
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const recordList = document.getElementById("record");
const resetButton = document.getElementById('reset');
const deleteButton = document.getElementById("del");
const wrapButton = document.getElementById("wrapbutton");


let timer; 
let isRunning = false; //타이머가 실행중인지 변수, 실행X
let elapsedTime = 0;   //경과된 시간

//시간 포맷 
function formatTime(ms) {
    const seconds = String(Math.floor(ms / 1000)).padStart(2, "0");
    const milliseconds = String(Math.floor((ms % 1000) / 10)).padStart(2, "0");
    return `${seconds}:${milliseconds}`;
}
  
//화면 업데이트
function updateDisplay() {
    timeDisplay.textContent = formatTime(elapsedTime);
}  


//타이머 시작
//Date.now() : 현재 시간을 밀리초 단위로 변환
//setInterval(funtion, delay) : 특정 간격으로 함수를 반복적으로 실행하는 함수
startButton.addEventListener('click', () => {
    if (!isRunning) { //실행중이지 않을때
        const startTime = Date.now() - elapsedTime; //재개 시, 경과 시간을 고려하여 타이머가 작동하도록

        timer = setInterval(() => {
            elapsedTime = Date.now() - startTime; //경과 시간 계산
            updateDisplay() //화면 업데이트

        }, 10) //0.01초

        isRunning = true;

    }
})

//기록 추가
function addRecord() {
    const listItem = document.createElement("li");
    listItem.textContent = formatTime(elapsedTime);

    const circleButton = document.createElement("button");
    circleButton.classList.add('circle_button');
    
    const checkIcon = document.createElement("span");
    checkIcon.textContent = '✔';
    checkIcon.classList.add('check_icon');
    checkIcon.style.display = "none"; // 기본적으로 숨김 처리

    circleButton.addEventListener('click', () => {
        if (checkIcon.style.display == "none") {
            checkIcon.style.display = 'inline';
        } else {
            checkIcon.style.display = "none";
        }
    });

    circleButton.appendChild(checkIcon); // 체크 표시를 버튼 내부에 추가
    listItem.prepend(circleButton); //기록 앞에 추가
    recordList.appendChild(listItem);

}

//타이머 정지
//clearInterval() : setInterval()로 설정한 주기의 실행을 멈추는 함수 = 타이머를 멈추는
stopButton.addEventListener('click', () => {
    if (isRunning) {   //실행중
        clearInterval(timer);
        isRunning = false;
        addRecord();
    }
})

//타이머 초기화
resetButton.addEventListener('click', () => {
    clearInterval(timer);
    elapsedTime = 0;
    isRunning = false;
    updateDisplay();
})

//삭제
//forEach : 각 기록 항목에 대해 반복 작업 수행
//record : 반복문에서 현재 처리중이 li 요소
deleteButton.addEventListener('click', () => {
    const records = recordList.querySelectorAll('li');
    records.forEach((record) => {
        const checkIcon = record.querySelector('.check_icon');
        if (checkIcon && checkIcon.style.display == 'inline'){
            record.remove();
        }
    });
});

//전체 선택
wrapButton.addEventListener('click', () => {
    const checkIcons = recordList.querySelectorAll('.check_icon');
    const wrapCheckIcon = wrapButton.querySelector('.check-icon');

    // 현재 상태 확인: 모든 체크 아이콘이 표시 중인지 확인
    // Array.from() : 배열로 변환
    const allChecked = Array.from(checkIcons).every(icon => icon.style.display === 'inline');

    if (allChecked) {
        // 모든 체크가 되어 있으면, wrapButton과 모든 아이콘 체크 해제
        wrapCheckIcon.style.display = 'none'; // wrapButton의 체크 해제
        checkIcons.forEach(icon => {
            icon.style.display = 'none'; // 모든 li의 체크 해제
        });
    } else {
        // 체크 안 되어 있으면, wrapButton과 모든 아이콘 체크 표시
        wrapCheckIcon.style.display = 'inline'; // wrapButton의 체크 표시
        checkIcons.forEach(icon => {
            icon.style.display = 'inline'; // 모든 li의 체크 표시
        });
    }
});

