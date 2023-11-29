def solution():
    input_values = list(map(int, input().split(" ")))
    a = input_values[0]
    b = input_values[1]
    multiple = a * b
    divide = int(a / b)
    print(f"{a} * {b} = {multiple}")
    print(f"{a} / {b} = {divide}")


solution()