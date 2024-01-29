/*
 현재가 데이터 생성 자바스크립트 

async function fetchData() {
	try {
	    // 'data' 객체를 생성하고 key-value 쌍을 설정합니다.
	    const data = {
	        key1: "value1",
	        key2: "value2",
	        // FastAPI로 전송할 추가 데이터는 여기에 추가할 수 있습니다.
	    };
	
	    // fetch 함수를 사용하여 지정된 URL로 POST 요청을 보냅니다.
	    const response = await fetch('http://127.0.0.1:8000/', {
	        method: 'POST',
	        headers: {
	            'Content-Type': 'application/json',
	        },
	        // 'data'를 JSON 문자열로 변환하여 요청 본문에 포함시킵니다.
	        body: JSON.stringify(data),
	    });
	
	    // 응답을 기다리고 JSON으로 파싱합니다.
	    const result = await response.json();
		console.log(result);
	    // 결과를 각각의 컨테이너에 추가합니다.
	    displayResultsInContainers(result);
	} catch (error) {
	    console.error("Error fetching data:", error);
	}
}

function displayResultsInContainers(result) {
    // ID가 'parent-container'인 부모 컨테이너 엘리먼트를 찾습니다.
    const parentContainer = document.getElementById('parent-container');

    // 부모 컨테이너가 존재하는지 확인한 후 추가 작업을 수행합니다.
    if (parentContainer) {
        // 각각의 컨테이너에 테이블을 생성하여 추가합니다.
        result.forEach((item, index) => {
            const container = createContainerWithTable(item);
            parentContainer.appendChild(container);
        });
    } else {
        console.error("부모 컨테이너를 찾을 수 없습니다.");
    }
}

function createContainerWithTable(data) {
    // 컨테이너 엘리먼트를 생성합니다.
    const container = document.createElement('div');
    container.classList.add('result-container'); // 필요시 클래스 추가

    // 테이블 엘리먼트를 생성합니다.
    const table = document.createElement('table');
    table.classList.add('new-table'); // 새로운 테이블에 클래스 추가

    // 각각의 데이터 항목에 대해 테이블 행을 생성합니다.
    for (const key in data) {
        const row = table.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);

        // 테이블 셀에 key와 value를 설정합니다.
        cell1.textContent = key;
        cell2.textContent = data[key];
    }

    // 테이블을 컨테이너에 추가합니다.
    container.appendChild(table);

    return container;
}

// fetchData 함수 호출
fetchData();
//setInterval(fetchData, 1000); // 5000 밀리초(5초)로 설정*/