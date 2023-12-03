def solution():
    # input: 85
    n = int(input()) # 85

    # print out score, 85 ~ 100, i += 1
    """
    score >= 90: A
    scroe >= 80: B
    score >= 70: C
    score >= 60: D
    score < 60 : F
    """
    # 1. Iteration
    for i in range(n, 101):
        # 2. Conditional Statement
        if i >= 90:
            print('A', end = ' ')
            continue
        if i >= 80:
            print('B', end = ' ')
            continue
        if i >= 70:
            print('C', end = ' ')
            continue
        if i >= 60:
            print('D', end = ' ')
            continue
        print('F', end = ' ')
        
solution()