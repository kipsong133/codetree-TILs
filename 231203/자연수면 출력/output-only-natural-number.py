def solution():
    # input: 2 3
    input_arr = list(map(int, input().split()))
    a = input_arr[0] # 2, -9 =< a =< 9
    b = input_arr[1] # 3, 1 =< b =< 50

    if a < 1:
        print(0)
        return
    
    for _ in range(b):
        print(a, end = '')




solution()