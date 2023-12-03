def solution():
    # input
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    n = input_arr[1]
    
    # (a += n) * n
    for _ in range(n): # iterate n
        a += n
        print(a)

solution()