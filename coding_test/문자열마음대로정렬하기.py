#  각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"],2))