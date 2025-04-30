import tkinter as tk


expression= ""


# 윈도우창 생성
def create_window():
    window = tk.Tk()
    window.title("tkinter 테스트")
    window.geometry("500x500+150+150")
    window.resizable(True,True)
    # Configure the three columns to expand equally
    for i in range(4):
        window.columnconfigure(i, weight=1)
    return window

# 버튼 생성
def create_button(window):
    buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+',
    ' ', 'C', ' ', '%',
    ]
    for index, text in enumerate(buttons):
        row = (index // 4) + 1  # buttons start from row 1
        col = index % 4
        button = tk.Button(window, text=text, width=5, height=2)
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
    
def create_display(window):
    global display_label
    display_label = tk.Label(window, text="입력창", font=("Arial",24),bg="white")
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
# 실행
if __name__ == "__main__":
    window = create_window()
    create_display(window)
    create_button(window)
    window.mainloop()
