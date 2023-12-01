def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]

    print(1 if a >= b else 0)
    print(1 if a > b else 0)
    print(1 if b >= a else 0)
    print(1 if b > a else 0)

solution()