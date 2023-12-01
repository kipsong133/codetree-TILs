def solution():
    # 2, 3, 11
    input_num = int(input())
    
    if input_num % 2 == 0:
        # 짝수라면
        input_num /= 2
    
    if input_num % 2 == 1:
        # 홀수라면
        input_num += 1
        input_num /= 2
    
    print(int(input_num))


solution()