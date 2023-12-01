def solution():
    a = int(input())
    input_arr = list(map(int, input().split(" ")))
    b = input_arr[0]
    c = input_arr[1]
    d = input_arr[2]
    e = input_arr[3]

    print(1 if a > b else 0)
    print(1 if a > c else 0)
    print(1 if a > d else 0)
    print(1 if a > e else 0)


solution()