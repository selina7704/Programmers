
def solution(n): 
    count = 0
    for a in range(1, int(n**0.5)+1):
        if n % a == 0: # 약수 n을 a로 나누었을 때 나머지가 0이면
            b = n//a # b는 n을 a로 나눈 몫 (a x b = n) == (b = n//a)
            if a != b:
                count += 2
            else:
                count += 1
    return count