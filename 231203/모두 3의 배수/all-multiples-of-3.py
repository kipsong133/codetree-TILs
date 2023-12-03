def solution():
    # input: 3 6 9 12 15
    input_arr = list(int(input()) for _ in range(5))
    
    is_multi: bool = True
    for num in input_arr:
        if num % 3 == 0:
            print(1)
            return
    print(0)
solution()