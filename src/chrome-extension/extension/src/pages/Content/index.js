import isVisible from 'is-element-visible';
import keyboardjs from 'keyboardjs';


var groupBy = function (xs, f) {
    var di = {};
    xs.forEach((e,i) => {
        let v = f(e)
        if (!di.hasOwnProperty(v)) {
		    di[v] = [];
        }
        di[v].push(e);
    });
    return di
};


function setStyle(elements, style) {
    elements.forEach(e => e.style.backgroundColor=style);
}

let colors = ['blue', 'yellow', 'green', 'pink']

function bindKeys(elements) {
    console.log('assigning')
    let keys = Object.keys(elements)
    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        console.log(key,elements[key])
    }
    keyboardjs.bind('ctrl+shift+k', (e) => {
        window.location = 'https://danielcieslinski.com'
    });
}

function euclidean(elements){
    let intViewportHeight = window.innerHeight;
    let intViewportWidth = window.innerWidth;
    // TODO
}


function exportDOM() {
    const links = document.querySelectorAll('a');

    if (links.length > 1) {
        let grouped = groupBy(links, isVisible);
        bindKeys(grouped)
        // document.addEventListener('keydown', alert('x'))
        var out = [];
        links.forEach((el) => out.push({ rect: el.getBoundingClientRect() , text: el.innerText, link: el.href}));
        const parsed = JSON.stringify({ head: document.head, body: document.body.innerHTML, links: out })
        chrome.runtime.sendMessage(parsed, function (response) {
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
