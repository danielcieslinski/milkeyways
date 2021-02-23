![](res/keyboard.png)

__*Missing bridge for synccing keyboard events across applications*__

---
## Outline
I hope to provide cross-platform solution, for handling user input. 
Supporting:
 - Conflict resolution
 - Optimal hotkey assignement, given measurable norm for a device
 - Global text completion

## Development

### Chrome extension
```
npm i
npm start
// This starts dev server, with webpack.
// Will auto-rebuild and bundle extension on every save
//
// Load unpacked in chrome
```
### Local server
```
python socketserver.py
```

Chrome extension will be sending data to `localhost:3232`.

