def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]

    first_answer = 1 if a < b else 0
    second_answer = 1 if a == b else 0
    print(f"{first_answer} {second_answer}")

solution()