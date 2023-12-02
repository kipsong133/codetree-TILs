def solution():
    input_arr = list(map(int, input().split(" ")))

    maximum = -100
    for num in input_arr:
        if num > maximum:
            maximum = num
    
    print(maximum)

solution()