def solution():
    input_list = list(map(int, input().split(" ")))
    a = input_list[0]
    b = input_list[1]
    temp_01 = a + b
    temp_02 = a - b
    result = temp_01 / temp_02
    print(f"{result:.02f}")


solution()