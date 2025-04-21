#     s	                result
# "one4seveneight"	     1478
# "23four5six7"	         234567
# "2three45sixseven"	 234567
# "123"	                 123

def solution(s):
    num_word = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    result = ''
    tmp = ''
    for char in s:
        if char.isdigit():
            result += char
            print(result)
        else:
            tmp += char
            if tmp in num_word:
                result += str(num_word[tmp])
                tmp = ''
    return int(result)




print(solution("one4seveneight"))
print(solution("1234"))
