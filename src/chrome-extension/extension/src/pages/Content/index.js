// import isVisible from 'is-element-visible';

// function getClickables(){
//     //#TODO
//     return document.querySelectorAll('a')
// }

import KeyboardJS from 'keyboardjs'


KeyboardJS.bind('a', null, (e) => {
  alert('a is released');
});



function pollDOM() {
    const links = document.querySelectorAll('a');  
    

    if (links.length > 1) {
        document.addEventListener('keydown', alert('x'))

        KeyboardJS.bind('x')

        var out = [];
        links.forEach((el) => out.push({ rect: el.getBoundingClientRect()}));
        const parsed = JSON.stringify({document: document, links: out})
        chrome.runtime.sendMessage({data: parsed}, function (response) {
            console.log(response);
        });
    } else {
        setTimeout(pollDOM, 300); // try again in 300 milliseconds
    }
}

// localStorage.setItem()

pollDOM();

console.log('Content script injected!');
console.log('Remember to reload extension, on update');

// console.log('')

// printLine("Using the 'printLine' function from the Print Module");
