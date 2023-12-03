def solution():
    # input: 3 6 9 12 15
    input_arr = list(int(input()) for _ in range(5))
    
    for num in input_arr:
        if num % 3 != 0:
            print(0)
            return
    print(1)
solution()