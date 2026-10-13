# Voxy GUI — Linux / Python

A Tkinter desktop GUI inspired by the supplied Voxy mockup. Includes Home,
Listening demo, Processing, Success/Error, History, and Settings screens. Uses
an extracted logo mark from the supplied reference image and includes an app icon.

## Run directly

```bash
sudo apt install python3-tk
python3 app.py
```

## Add Voxy to the Applications menu

From this extracted folder, run:

```bash
chmod +x install.sh
./install.sh
```

This installs the app to `~/.local/share/voxy` and creates a `Voxy.desktop`
launcher in `~/.local/share/applications`. Voxy should then appear in the
Ubuntu applications grid/search; you can right-click it to add it to Favorites.

## Demo commands

- `open YouTube`
- `open YouTube and search for lo-fi music`
- `open Google`
- `open browser`
- `open terminal`
- `search for cats`
- `make a folder called DemoFolder`
- `take a screenshot`

Listening is currently a demo screen. Connect it to the team's speech-to-text
module and NLP intent parser for real voice commands. Commands are deliberately
routed through a small allowlist rather than passed to an unrestricted shell.
