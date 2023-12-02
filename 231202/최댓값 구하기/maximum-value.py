def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    c = input_arr[2]

    maximum = -100
    for num in [a, b, c]:
        if num > maximum:
            maximum = num
    
    print(maximum)

solution()