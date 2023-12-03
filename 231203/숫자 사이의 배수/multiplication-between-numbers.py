def solution():
    # input: 4 21
    input_arr = list(map(int, input().split()))
    a =  input_arr[0]
    b =  input_arr[1]
    
    sum_val = 0
    cnt = 0
    avg = 0

    # Iteration: a ~ b
    for num in range(a, b + 1):
        if num % 5 == 0 or num % 7 == 0:
           sum_val += num
           cnt += 1
    
    avg =  sum_val / cnt

    print(f'{sum_val} {avg:.01f}')



solution()