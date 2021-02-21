// import isVisible from 'is-element-visible';

// function getClickables(){
//     //#TOD
//     return document.querySelectorAll('a')
// }

import keyboardjs from 'keyboardjs';

/*

1. Send all info
2. 

*/


// function bindKeys() {
//     keyboardjs.bind('a + b > c', (e) => {
//         console.log('a and b then c is pressed');
//     });
// }


function exportDOM() {
    const links = document.querySelectorAll('a');  
    
    if (links.length > 1) {
        // document.addEventListener('keydown', alert('x'))
        var out = [];
        links.forEach((el) => out.push({ rect: el.getBoundingClientRect()}, el.innerText, el.href));
        const parsed = JSON.stringify({head: document.head, body: document.body.innerHTML, links: out})
        console.log(parsed)
        chrome.runtime.sendMessage((parsed), function (response) {
            console.log(response);
        });
    } else {
        setTimeout(exportDOM, 300); // try again in 300 milliseconds
    }
}

// localStorage.setItem()

exportDOM();

console.log('Content script injected!');
console.log('Remember to reload extension, on update');
// ------------
// Content socket test


// printLine("Using the 'printLine' function from the Print Module");
chrome.tabs.query
