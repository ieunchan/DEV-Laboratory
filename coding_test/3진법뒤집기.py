# level 1
# 자연수 n이 매개변수로 주어집니다. 
# n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    result = ''
    while n > 0:
        n, r = divmod(n, 3)  # n을 3으로 나눈 몫과 나머지
        result += str(r)
    return int(result,3)




print(solution(45))
# print(solution(45)) # 7
# print(solution(125)) # 229