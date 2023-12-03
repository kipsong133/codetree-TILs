def solution():
    # input: 50
    n = int(input())

    if n == 1:
        print(1)

    cnt = 0
    temp = n
    # Iteration: 1 ~ n
    for divider in range(1, n + 1):
        if temp =< 1: 
            break

        temp = int(temp / divider) # 50 
        cnt += 1

    print(cnt)

solution()