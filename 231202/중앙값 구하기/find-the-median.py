def solution():
    input_arr = list(map(int, input().split()))

    minimum = float("inf")
    maximum = float("-inf")

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