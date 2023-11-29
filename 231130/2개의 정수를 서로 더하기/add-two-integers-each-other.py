def solution():
    input_list = list(map(int, input().split(" ")))
    a = input_list[0]
    b = input_list[1]
    
    a += b
    first_answer = a
    b += a
    second_ansewr = b
    print(f"{a} {b}")


solution()