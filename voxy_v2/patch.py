from pathlib import Path
p=Path('/tmp/voxy_v2/app.py')
s=p.read_text()
s=s.replace('import shutil\n', 'import shutil\nfrom pathlib import Path\n')
s=s.replace('        self.title("Voxy")\n', '''        self.title("Voxy")
        self.light_mode = False
        self._logo_image = None
        self._app_icon = None
        try:
            assets = Path(__file__).resolve().parent / "assets"
            self._logo_image = tk.PhotoImage(file=str(assets / "voxy_logo_mark.png"))
            self._app_icon = tk.PhotoImage(file=str(assets / "voxy_icon.png"))
            self.iconphoto(True, self._app_icon)
        except tk.TclError:
            pass
''')
s=s.replace('        self.light_mode = False\n        self.sound_feedback = False', '        self.sound_feedback = False', 1)
s=s.replace('        else:\n            self._settings_page()\n', '        else:\n            self._settings_page()\n        self.after_idle(self._apply_theme_tree)\n')
# Replace logo drawing with supplied logo asset and graceful fallback
start=s.index('    def _logo_mark(self, parent, size=64):')
end=s.index('\n    def _home_page(self):', start)
new='''    def _logo_mark(self, parent, size=64):
        if self._logo_image is not None:
            # Scale the supplied reference logo to the requested size.
            factor = max(1, round(400 / max(size, 1)))
            image = self._logo_image.subsample(factor, max(1, factor // 2))
            label = tk.Label(parent, image=image, bg=self._palette()["bg"], bd=0)
            label.image = image
            label.pack()
            return label
        canvas = tk.Canvas(parent, width=size, height=size, bg=self._palette()["bg"], highlightthickness=0)
        canvas.pack()
        canvas.create_text(size/2, size/2, text="〰V〰", fill=ORANGE, font=("Arial", int(size*.25), "bold"))
        return canvas
'''
s=s[:start]+new+s[end:]
# use app icon in title strip too
s=s.replace('        tk.Label(self.titlebar, text="●", fg=ORANGE, bg=BG, font=("Arial", 10)).pack(side="left", padx=(12, 5))\n', '        tk.Label(self.titlebar, text="●", fg=ORANGE, bg=BG, font=("Arial", 10)).pack(side="left", padx=(12, 5))\n')
# add theme methods replacing old toggle_theme at bottom
old='''    def toggle_theme(self):
        # Keep the dark visual identity; this control can be expanded into a full light theme.
        messagebox.showinfo("Appearance", "Voxy's dark theme is active.", parent=self)
'''
new='''    def _palette(self):
        if self.light_mode:
            return {"bg": "#F3F3F5", "panel": "#FFFFFF", "sidebar": "#E3E3E6",
                    "text": "#202126", "muted": "#5C5D63", "row": "#E8E8EC",
                    "header": "#D8D9DE", "button": "#C96A45", "entry": "#FFFFFF"}
        return {"bg": BG, "panel": PANEL, "sidebar": SIDEBAR, "text": TEXT,
                "muted": MUTED, "row": "#292B30", "header": "#343438",
                "button": BUTTON, "entry": "#292B30"}

    def _apply_theme_tree(self):
        """Recolor all current widgets; called on every page so light mode persists."""
        pal = self._palette()
        bg_map = {
            "#17191D": pal["bg"], "#202226": pal["panel"], "#3A3A3A": pal["sidebar"],
            "#292B30": pal["row"], "#343438": pal["header"], "#41454D": pal["header"],
            "#D8D8D8": ("#E1E1E5" if self.light_mode else "#D8D8D8"),
            "black": ("#FFFFFF" if self.light_mode else "black"),
        }
        fg_map = {"#F4F0F0": pal["text"], "white": ("#FFFFFF" if not self.light_mode else "#FFFFFF"),
                  "#B8B5B8": pal["muted"], "#17191D": pal["text"]}
        def visit(widget):
            try:
                opts = widget.configure()
                if "background" in opts or "bg" in opts:
                    old = widget.cget("bg")
                    if old in bg_map: widget.configure(bg=bg_map[old])
                if "foreground" in opts or "fg" in opts:
                    old = widget.cget("fg")
                    if old in fg_map: widget.configure(fg=fg_map[old])
                if "insertbackground" in opts:
                    widget.configure(insertbackground=pal["text"])
            except (tk.TclError, KeyError):
                pass
            for child in widget.winfo_children():
                visit(child)
        visit(self)
        # Tk OptionMenu's menu is a separate widget.
        try:
            for widget in self.winfo_children():
                pass
        except tk.TclError:
            pass

    def toggle_theme(self):
        self.light_mode = not self.light_mode
        self.show_page(self.current_page)
'''
if old not in s: raise Exception('toggle old not found')
s=s.replace(old,new)
# Ensure transient screens reapply palette after building, including listening and processing/result
s=s.replace('        tk.Button(inner, text="Back to Home", command=lambda: self.show_page("Home"),\n                  bg=BUTTON, fg="white", bd=0, padx=12, pady=6).pack()\n', '        tk.Button(inner, text="Back to Home", command=lambda: self.show_page("Home"),\n                  bg=BUTTON, fg="white", bd=0, padx=12, pady=6).pack()\n        self.after_idle(self._apply_theme_tree)\n')
s=s.replace('        self.after(650, lambda: self._execute_demo(command))\n', '        self.after_idle(self._apply_theme_tree)\n        self.after(650, lambda: self._execute_demo(command))\n')
s=s.replace('        self.status_message.set("How Can I Help You Today ?")\n', '        self.status_message.set("How Can I Help You Today ?")\n        self.after_idle(self._apply_theme_tree)\n')
p.write_text(s)
