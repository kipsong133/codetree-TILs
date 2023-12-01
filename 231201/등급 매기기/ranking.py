def solution():
    input_score = int(input())

    # 좁은 범위를 먼저 if condition 으로 사용한다.
    if input_score > 89:
        print("A")
        return
    
    if input_score > 79:
        print("B")
        return

    if input_score > 69:
        print("C")
        return
    
    if input_score > 59:
        print("D")
        return
    
    print("F")
    


solution()