def solution():
    # Difficulty: eng < math
    # Student A, Student B
    # Condition 1: only comparing whos' math score but they got the same score, print eng score.
    
    a_scores = list(map(int, input().split(" ")))
    b_scores = list(map(int, input().split(" ")))

    if a_scores[0] > b_scores[0]:
        print("A")
        return
    elif a_scores[0] < b_scores[0]:
        print("B")
        return
    
    # Condition 2: they got the same score of math.
    # So have to compare Eng Score.
    if a_scores[1] > b_scores[1]:
        print("A")
    else:
        print("B")





solution()