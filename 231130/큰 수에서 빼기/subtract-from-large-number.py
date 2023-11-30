def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    is_a_bigger = a > b
    if (is_a_bigger):
        print(a - b)
        return
    print(b - a)
    

solution()