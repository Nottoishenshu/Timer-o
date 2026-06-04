"""
Opens Timer'o as a small desktop window using the website in index.html.
Run: python main.py
Or open index.html directly in any browser — no Python needed.
"""
import os
import sys

import webview


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    html_path = resource_path("index.html")
    window = webview.create_window(
        "Timer'o",
        html_path,
        width=480,
        height=680,
        resizable=True,
    )
    webview.start()
