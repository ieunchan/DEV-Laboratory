import tkinter as tk


def create_window(title: str, width: int, height: int) -> tk.Tk:
    """Create a resizable Tk window with the provided metadata."""
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.resizable(True, True)
    return window