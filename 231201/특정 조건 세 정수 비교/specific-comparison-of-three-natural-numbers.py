def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    c = input_arr[2]

    is_minimum: bool = (a <= b) and (a <= c)
    same_numbers: bool = (a == b == c)

    first_answer = 1 if is_minimum else 0
    second_answer = 1 if same_numbers else 0
    print(f"{first_answer} {second_answer}")

solution()