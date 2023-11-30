def solution():
    # 2개의 값을 입력받는다.
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]

    # if: a > b = a *b
    # else: int(b / a)
    if a > b:
        print(a * b)
    else:
        quotient = int(b / a)
        print(quotient)
    return

solution()