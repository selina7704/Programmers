def solution(myString, pat):
    # answer = []
    # for i in myString:
    #     if i == 'A':
    #         answer.append('B')
    #     elif i == 'B':
    #         answer.append('A')
    # answer = ''.join(answer)
    # return 1 if pat in answer else 0

    answer = ''.join('A' if i == 'B' else 'B' for i in myString)
    return 1 if pat in answer else 0