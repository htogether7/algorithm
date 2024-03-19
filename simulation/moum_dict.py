def solution(word):
    answer = 0
    gaps = [781, 156, 31, 6, 1]
    
    indices = {
        "A" : 0,
        "E" : 1,
        "I" : 2,
        "O" : 3,
        "U" : 4
    }
    
    answer += len(word)
    for i in range(len(word)):
        answer += gaps[i] * indices[word[i]]
    
    
    
    
    
    return answer