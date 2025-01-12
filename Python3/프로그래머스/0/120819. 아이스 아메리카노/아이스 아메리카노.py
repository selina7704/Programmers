def solution(money):
    num =  money // 5500 
    change = money % 5500 
    return [num, change]