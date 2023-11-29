def solution():
    input_list = list(map(int, input().split(" ")))
    a = input_list[0]
    b = input_list[1]
    quotient = int(a / b)
    remainder = a % b
    print(f"{quotient}...{remainder}")



solution()