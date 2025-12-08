from utils import create_window


window = create_window(title='지뢰찾기', width=500, height=500)
window.mainloop()

def create_grid(window):
    for i in range(10):
        window.rowconfigure(i, weight=1)
    for j in range(10):
        window.columnconfigure(j, weight=1)
    return window

create_grid(window)
window.mainloop()