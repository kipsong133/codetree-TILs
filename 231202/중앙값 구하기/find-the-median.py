def solution():
    input_arr = list(map(int, input().split()))

    minimum = 100
    maximum = -100

    for num in input_arr:
        if num >= maximum:
            maximum = num
            continue
        if num <= minimum:
            minimum = num
        
    input_arr.remove(maximum)
    input_arr.remove(minimum)
    print(input_arr[0])
        

solution()