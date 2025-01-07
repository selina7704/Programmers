def solution(my_string):
    answer = []
    for i in my_string:
        if i in ['a','e','i','o','u']:
            continue
        else:
            answer.append(i)
    return ''.join(answer)

# def solution(my_string):
#     vowels = "aeiou"  
#     result = ''.join(char for char in my_string if char not in vowels)  # 모음을 제외한 문자들만 선택합니다.
#     return result