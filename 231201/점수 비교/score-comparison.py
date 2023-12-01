def solution():
    # Input: 100 85
    a_scores = list(map(int, input().split(" ")))
    b_scores = list(map(int, input().split(" ")))
    if a_scores[0] > b_scores[0] and a_scores[1] > b_scores[1]:
        print(1)
    else:
        print(0)
    
    

solution()