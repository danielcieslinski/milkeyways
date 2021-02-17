// import '../../assets/img/icon-34.png';
// import '../../assets/img/icon-128.png';


function send(data) {
    let ws = new WebSocket('ws://localhost:3234/');
    // messages = document.createElement('ul');

    ws.onopen = function (event) {
        // console.log('ws.onopen', event);
        ws.send(data) // This calls ws on message.
    };

    ws.onmessage = function (event) {
        console.log('ws.onmessage, called with data:', data);
    }

};

// chrome.runtime.onmessage(message, )

// chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//     if (tabs.l > 0) {
//         chrome.tabs.sendMessage(tabs[0].id, { greeting: "hello" }, function (response) {
//             console.log(response.farewell);
//         });
//     }
// });


// chrome.tabs.sendMessage()


chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    var tabdata = { tabId: tabId, changeInfo: changeInfo, tab: tab };
    
    if (changeInfo.status === 'complete') {
            // node = document.getRootNode();
            tabdata.special_message = ['SPECIAL SPECIAL MESSAFEW!!!!!!!'];
        }
    
        send(tabdata);


    // if (changeInfo.status == 'complete') {
    //     chrome.tabs.query({ active: true }, function (tabs) {
    //         const msg = "Hello from background ?";
    //         console.log(msg)
    //         chrome.tabs.sendMessage(tabs[0].id, { "message": msg });
    //     })
    // }
});