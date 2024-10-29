# 문제

# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 
# 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

# 첫째항 : 등차수열의 가장 처음에 오는 수
# 공차: 등차수열에서 연속된 두 항의 차이. 각 항에서 그 앞 항을 뺀 값

# 등차수열 만들기
# 첫째항 a와 공차 d가 주어지면, 다음과 같이 등차수열을 만들 수 있습니다:
# 첫 번째 항: a
# 두 번째 항: a + d
# 세 번째 항: a + 2d
# 네 번째 항: a + 3d
# n번째 항은 a + (n-1)d로 표현

def solution(a,d,included):
    answer = 0
    for i in range(len(included)):
        current_term = a + (d*i)
        if included[i]:
            answer += current_term
    return answer

#def solution(a,d,included):
#    return sum(a+i*d for i, f in enumerate(included) if f)