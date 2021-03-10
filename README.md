![](res/keyboard.png)
__*Missing bridge for synccing keyboard events across applications*__

---
## Outline
I hope to provide cross-platform solution, for handling user input. 
Supporting:
 - Conflict resolution
 - Optimal hotkey assignement, given measurable norm for a device
 - Global text completion


# Installation


## Development

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

