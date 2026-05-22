COLORS = {
  "primary": "#0F8BCB",
  "primary_dark": "#0A6FA3",
  "sidebar": "#EAF6FF",
  "background": "#F8FCFF",
  "text": "#1F3A5F",
  "muted": "#607D9A",
  "white": "#FFFFFF",
}

APP_STYLE = f"""
QMainWindow {{
  background-color: {COLORS["background"]};
}}

QPushButton {{
  border: none;
  border-radius: 10px;
  padding: 10px;
  font-size: 15px;
}}

QLabel {{
  color: {COLORS["text"]};
}}
"""