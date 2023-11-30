def solution():
    input_value = int(input())
    if input_value >= 80:
        print("pass")
    else:
        diff = 80 - input_value # 차이만큼 값
        print(f"{diff} more score")

solution()