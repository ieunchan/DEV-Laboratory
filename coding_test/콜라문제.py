# 이 문제는 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 
# 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산하는 문제입니다.
# 보유 중인 빈 병이 a개 미만이면, 추가적으로 빈 병을 받을 순 없습니다

def solution(a, b, n):
    answer = 0
    while n >= a:
        result, remain = divmod(n,a)
        answer += result * b
        n = result * b + remain
    return answer

print(solution(2,1,20)) # 19

# 빈병 a = 콜라 b병. then 빈병 n개는 콜라 몇병?
# a=2, b=1, n=20 으로 가정 시,
# n / a * b = 10
# n / a * b = 5
# n / a * b = 2, 나머지 1

