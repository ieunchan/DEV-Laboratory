# 반복문 연습
# 구구단 만들어보기
def multiplication_table():
    for i in range(2,10):
        for j in range(1,10):
            print(f"{i} x {j}= {i*j}")
        print()

multiplication_table()