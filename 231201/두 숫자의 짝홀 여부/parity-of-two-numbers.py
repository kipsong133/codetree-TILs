def solution():
    # Input: 8, 15
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]

    check_odd(a)
    check_odd(b)
    return

def check_odd(num: int):
    if num % 2 == 0:
        print("even")
    else: 
        print("odd")

solution()