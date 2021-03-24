# Milekeyways

![](res/keyboard.png)
__*Missing bridge for synccing keyboard events across applications*__

---
## Goals

 - Standarized hotkey assinging, across OS programs and web apps 
 - Conflict free assigning
 - Optimal hotkey assignement, given measurable any device with a norm $|.|$
 - Global text completion

# Done 


### Chrome extension
```bash
cd src/src/chrome-extension/extension/
npm i
npm start
```
This will start development server at localhost:3000 
For more details view the [README](src/chrome-extension/extension/README.md)

### Local server
```
python socketserver.py
```

Chrome extension will be sending data to `localhost:3232`.

