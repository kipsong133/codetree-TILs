def solution():
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]
    
    for i in range(a, b+1):
        if i % 2 == 1:
            print(i, end = " ")

solution()