def solution():
    # Input: 12 14
    input_arr = list(map(int, input().split()))
    input_arr.sort()
    a = input_arr[0]
    b = input_arr[1]

    common = set()
    for num in range(1, 1920+1):
        if 1920 % num == 0 and 2880 % num == 0:
            common.add(num)

    # Iteration: a ~ b
    for num in range(a, b + 1):
        # Condition: common divisor 1920 and 2880
        if num in common:
            print(1)
            return
    print(0)

    


solution()