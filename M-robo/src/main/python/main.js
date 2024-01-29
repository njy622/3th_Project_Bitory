const outputDiv = document.getElementById('output');

async function fetchData(url, headers, params) {
    try {
        const response = await axios.get(url, { headers, params });
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error.message);
        throw error;
    }
}

async function fetchMarketData() {
    const priceList = [];
    const coinShopDict = await fetchCoinShopDict();

    for (const market of coinShopDict.market) {
        const url = 'https://api.upbit.com/v1/ticker';
        const headers = { 'accept': 'application/json' };
        const params = { 'markets': market };

        const responseData = await fetchData(url, headers, params);
        priceList.push(responseData);
        console.log(responseData)
    }

    return priceList;
}

async function fetchCoinShopDict() {
    try {
        const response = await axios.get('https://api.upbit.com/v1/ticker');
        return response.data;
    } catch (error) {
        console.error('Error fetching coin shop data:', error.message);
        throw error;
    }
}


async function processPriceList(priceList) {
    const priceList2 = [];
    const priceList3 = [];
    const explanationName = []; // Assume there's an array or data source for explanation names

    for (const entry of priceList) {
        for (const key in entry) {
            if (key !== "{'name': 'too_many_requests'}" && key !== 'name') {
                priceList2.push(entry[key]);
            }
        }
    }

    for (let i = 0; i < priceList2.length; i++) {
        for (let j = 0; j < priceList2.length; j++) {
            for (const key in priceList2[j]) {
                for (let k = 0; k < explanationName.length; k++) {
                    if (key === explanationName[k].split(' ')[0]) {
                        key = explanationName[k] + ': ' + priceList2[j][key];
                        priceList3.push(key);
                    }
                }
            }
        }
    }

    return priceList3;
    console.log(priceList3)
}


function splitTotalPrice(priceList3) {
    const totalPrice2 = [];

    for (let i = 0; i < priceList3.length; i++) {
        totalPrice2.push(priceList3.slice(26 * i, 26 * (i + 1)));
    }

    return totalPrice2;
}

async function displayData() {
    const priceList = await fetchMarketData();
    const priceList3 = await processPriceList(priceList);
    const totalPrice2 = splitTotalPrice(priceList3);

    const outputHtml = totalPrice2.map(item => `<p>${item.join(', ')}</p>`).join('');
    outputDiv.innerHTML = outputHtml;
}

// 실행
displayData();
