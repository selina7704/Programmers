def solution(array):
    max_number = max(array)
    index = array.index(max_number)
    return [max_number, index]