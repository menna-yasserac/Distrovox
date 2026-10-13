#!/usr/bin/env bash
set -e
SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.local/share/voxy"
mkdir -p "$DEST/assets" "$HOME/.local/share/applications"
cp "$SOURCE_DIR/app.py" "$DEST/app.py"
cp "$SOURCE_DIR/assets/voxy_logo_mark.png" "$DEST/assets/voxy_logo_mark.png"
cp "$SOURCE_DIR/assets/voxy_icon.png" "$DEST/assets/voxy_icon.png"
chmod +x "$DEST/app.py"
cat > "$HOME/.local/share/applications/voxy.desktop" <<DESKTOP
[Desktop Entry]
Version=1.0
Type=Application
Name=Voxy
Comment=Voxy voice assistant
Exec=/usr/bin/python3 "$DEST/app.py"
Icon=$DEST/assets/voxy_icon.png
Terminal=false
Categories=Utility;Accessibility;
StartupNotify=true
DESKTOP
chmod +x "$HOME/.local/share/applications/voxy.desktop"
update-desktop-database "$HOME/.local/share/applications" >/dev/null 2>&1 || true
echo "Voxy installed. Search for 'Voxy' in the Ubuntu applications menu."
