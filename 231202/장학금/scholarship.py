def solution():
    # Input: [82, 95]
    score_arr = list(map(int, input().split(" ")))
    mid = score_arr[0]
    fin = score_arr[1]

    # Condition 1: Midterm Exam got more than 90 score
    if mid < 90 and fin < 90:
        print(0)
        return

    # Condition 2: Final Exame got more than 90 score
    if fin >= 95:
        print(100000)
        return
    if fin >= 90:
        print(50000)
        return    

solution()