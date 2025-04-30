import tkinter as tk

# 디스플레이에 계속 업데이트될 표현식입니다.
expression= ""


# 윈도우창 생성
def create_window():
    window = tk.Tk()
    window.title("BASIC CALCULATOR")
    window.geometry("500x500+150+150")
    window.resizable(True,True) # 윈도우 창 사이즈 조절 (가로, 세로) 가능 여부

    # 동일한 간격으로 4칸의 컬럼 생성
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
    for index, text in enumerate(buttons): # row에 +1을 하는 이유는 0번 row에는 디스플레이가 있어서입니다.
        # '7'의 index = 0, text = '7' 인데 0 // 4 = 0이고 +1 을 해주니깐 1번째 row에 배정됩니다.
        row = (index // 4) + 1 
        # '7'의 index = 0, 0%4 == 0이니깐 0번째 column에 배정됩니다.
        col = index % 4 
        # 람다 함수는 버튼이 눌린 버튼을 press() 함수로 전송합니다.
        button = tk.Button(window, text=text, width=5, height=2, command=lambda t=text: press(t)) 
        # 버튼 행렬 설정, 간격 설정
        button.grid( row=row, column=col, padx=5, pady=5, sticky="nsew")
        
# 디스플레이를 생성하는 함수입니다.
def create_display(window):
    global display_label
    display_label = tk.Label(
        window, text="", 
        font=("Arial",24),
        bg="white", 
        fg="black"
    )
    display_label.grid(
        row=0, 
        column=0, 
        columnspan=4, 
        padx=10, 
        pady=10, 
        sticky="nsew"
    )

def press(value):
    global expression
    print(f"[DEBUG] 버튼 눌림: {value}") # 버튼이 눌리는지 확인용으로 넣어뒀습니다. (터미널 창에서 확인 가능)
    
    if value in ("=","C"): # =, C 버튼이 눌리면 calculate() 로 보냅니다.
        calculate(value)
        expression = "" # 보내고 표현식 초기화
    else:
        expression += str(value) # =, C 버튼이 아니면 눌린 버튼을 표현식에 계속 추가합니다.
        display_label.config(text=expression) # 버튼이 눌릴때마다 화면(label)에 표시

def calculate(value):
    global expression
    try: # eval() 함수는 에러가 많이 발생한다 하여 예외처리가 필수라고 합니다.
        if value == "=": # 눌린 값이 = 이면
            result = eval(expression) # 표현식을 계산하여 result 변수 안에 넣습니다.
            expression = str(result) # 계산된 표현식은 정수 or 실수형이라 문자열로 바꿔서 expression 변수 안에 넣습니다.
            display_label.config(text=expression) # 답을 디스플레이에 띄웁니다.
        elif value == "C": # 누른 버튼이 C이면
            expression = "" # 표현식을 초기화합니다.
            display_label.config(text=expression) # 그리고 디스플레이에 표시합니다.
    except Exception as e: # 만약 다른 값이 오면
        expression = "" # 표현식을 초기화하고
        display_label.config(text=f"ERROR!!: {e}") # 디스플레이에 에러 메시지를 띄웁니다.


        
# 실행
if __name__ == "__main__":
    window = create_window()
    create_display(window)
    create_button(window)
    window.mainloop()
