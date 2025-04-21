#  각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬


def solution(strings, n):
    result = []
    asc = []
    for idx, i in enumerate(strings):
        asc.append(i[n])
        result.append(f"{idx}: {i}")
    return result, asc

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"],2))