console.log('Log: background/index.js, Launched');

function send(data) {
    let ws = new WebSocket('ws://localhost:3234/');

    ws.onopen = function (event) {
        console.log('ws.onopen', event);
        ws.send(data);
    };

    ws.onmessage = function (event) {
        console.log('resp', event.data)
    };
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    send(JSON.stringify({ request: request, sender: sender }));
});


chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    const s = JSON.stringify({ tabId: tabId, changeInfo: changeInfo, tab: tab });
    send(s);
    // console.log(tabId, changeInfo, tab);
    // if (changeInfo.status == 'complete') {
    //     chrome.tabs.query({ active: true }, function (tabs) {
    //         const msg = "Hello from background ?";
    //         console.log(msg)
    //         chrome.tabs.sendMessage(tabs[0].id, { "message": msg });
    //     })
    // }
});

