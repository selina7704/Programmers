def solution(rsp):
    game = {'2':'0', '0':'5', '5':'2'}
    return ''.join(game[i] for i in rsp)

'''
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

'''