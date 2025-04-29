import tkinter as tk



def create_window():

    window = tk.Tk()
    window.title("tkinter 테스트")
    window.geometry("500x500+150+150")
    window.resizable(True,True)
    return window

def create_button(window):

    for i in range(1,10):
        button = tk.Button(window, text=f"{i}")
        button.pack()

if __name__ == "__main__":
    window = create_window()
    create_button(window)
    window.mainloop()
