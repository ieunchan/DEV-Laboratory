# # 반복문 연습
# # 구구단 만들어보기
# def multiplication_table():
#     for i in range(2,10):
#         for j in range(1,10):
#             print(f"{i} x {j}= {i*j}")
#         print()

# multiplication_table()

# # 숫자 합이 100 되면 멈추기
# from random import randint

# def sum_num():
#     total = 0
#     count = 0
#     while total < 100:
#         random = randint(1,20)
#         total += random
#         count += 1
#         print(f"더한 수 : {random}, 총 횟수 : {count}, 결과 : {total}")

# sum_num()

def odd_even():
    
    first = int(input("시작 수 입력 >> "))
    last = int(input("마지막 수 입력 >> "))

    odd = [i for i in range(first, last +1) if i % 2 != 0]
    even = [i for i in range(first, last+1) if i % 2 == 0]
    return (f"홀수 = {odd}\n짝수 = {even}")

print(odd_even())