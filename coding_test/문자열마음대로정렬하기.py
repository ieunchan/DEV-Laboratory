#  각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬


def solution(strings, n):
    # 정렬: 첫 번째 기준은 strings[i][n], 두 번째 기준은 전체 문자열(strings[i])
    return sorted(strings, key=lambda x: (x[n], x))
    
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"],2))