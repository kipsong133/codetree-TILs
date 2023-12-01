def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    maxium = a if a > b else b
    print(maxium)



solution()