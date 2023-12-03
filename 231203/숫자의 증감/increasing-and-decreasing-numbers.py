def solution():
    # input: A 9
    input_arr = list(input().split())
    c = input_arr[0] # 'A' or 'D'
    num = int(input_arr[1])

    if c == 'A':
        # Case 1: if c == 'A', print out n, i+=1
        for i in range(1, num+1):
            print(i, end = ' ')
        return
    
    if c == 'D':
        # Case 2: if c == 'B', print out n, i -=1
        for i in range(num, 0, -1):
            print(i, end = ' ')
        return


solution()