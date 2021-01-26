![](mkw.png)

__*Towards unification of user input handling*__

<!-- // <kbd>/</kbd> - ```focus search``` -->

----

## Introduction
Recently it became an extremely popular practice for web applications, to enhance accessibility, through including keyboard shortcuts handling on the website. 

Due to the current limitation of the web, shortcuts are being assigned on the server side, through binding keyboard event listeners to the documents. 

This happens regardless of users' layout, keymappings and even other active shortcuts, injected into the site. 

This project aims to bring up the topic of estabilishing necessary standardizations of the common keyboard shortucts, by that bringing also more general topic, of communication schema for exchanging users' preferences across web applications.  

### Future of UI
Throughout recent years, into use have came multiple input devices that differ in design and capabilities. 
 Recently there is a broad research regarding various methods for controlling the computer, like [Gesture control](https://link.springer.com/chapter/10.1007/978-981-15-3639-7_96), or using [BCI](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface).
  Each of them will require to create an explicit mapping of actions in order to adapt them to the keyboard oriented web. Using methods proposed in this project it will be possible to enable the control in web applications, not needing to create any adaptation on the side of the application.


# Keyboards
Keyboard oriented navigation is the key for efficiency while using computer.
This has been known for a long time especially among linux users and developers, who came up with software like **vim** and emacs.
 Keyboards, vary in, language, layout, and especially available keys. Some of these are causing serious problems like <kbd>⌘</kbd> on apple devicies, taking role of usall <kbd>ctrl</kbd>. 

One of this project goals is to come up with solution, where all this differences will be held on clients' side instead of having them covered on the server's side. I'm mentioning this [below](#outline)

  <!-- More about keyboards [here](keyboards.md) -->

## Outline
To integrate the sync of OS and Web apps, I propose creating:

### **Client side** 
   - Local keyboard manager
   - Browser plugin that securely connects with local keyboard manager.

### **Server**
   - Very tiny, js library, that will implement a wrapper, around existing keyboard event bindings, allowing client to manipulate keyboard shortcuts.
  

   - [this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) looks, like a reasonable thing to use.


 However, I still dont feel like having the great idea, for defining this process and don't feel qualified enough for defining such.
   - Submit an issue, if you'd wish to contribute.

   I've also created a [question](https://stackoverflow.com/questions/64820525/user-preference-client-server-dialogue) on stack overflow, thinking most of the time that I'm just having some serious knowledge gaps and just missing a very obvious concept.

### 

## Overall goals
### User side
- Assigning conflict-free keyboard shortcuts.
- Endless keyboard modes.
  - Kinda "every key is modifier" idea
- Context-aware auto mode switching.
- Detection of input mode in browser 
- One global shortcut for listing active mappings.
  
   <kbd>super</kbd> + <kbd>?</kbd>

### In the browser
Considering that extension is installed on both sides
- Ability to remap shortcuts, that are in conflict with already assigned
- Consistent navigation on all the websites using `milkeyways`
- Enabling additionall non-conflicting keybindings using another extensions like, `Vimium`

### Web application side
Simply enabling accessibility for all the devices, not having to create any explicit case handling.

## Types of actions
...
