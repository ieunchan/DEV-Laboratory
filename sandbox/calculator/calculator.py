import tkinter as tk


expression= ""


# 윈도우창 생성
def create_window():

    window = tk.Tk()
    window.title("tkinter 테스트")
    window.geometry("500x500+150+150")
    window.resizable(True,True)
    return window

# 버튼 생성
def create_button(window):
    for i in range(1, 10):
        row = (i - 1) // 3   # 행 계산
        col = (i - 1) % 3    # 열 계산
        button = tk.Button(window, text=str(i), width=5, height=2)
        button.grid(row=row, column=col, padx=5, pady=5)
        
    
# 실행
if __name__ == "__main__":
    window = create_window()
    create_button(window)
    window.mainloop()
