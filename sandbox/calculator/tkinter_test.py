from tkinter import ttk 
import tkinter as tk

window = tk.Tk()

window.title("tkinter 테스트")
window.geometry("500x500+150+150")
window.resizable(True,True)

label = tk.Label(window, text="라벨")
label.pack()

style = ttk.Style()
style.configure(
    "Custom.TButton", 
    foreground = "white", 
    background = "black",
    )
button = ttk.Button(window, text="ttk button",style="Custom.TButton")
button.pack()

window.mainloop()