def solution():
    # Input: 50
    n = int(input())
    cnt = 0

    while True:
        # Condition 1: even number
        if n % 2 == 0:
            n = (n * 3) + 1
        else:
            n = (n * 2) + 2

        cnt += 1 # iterator

        if n > 1000:
            # Termination condition
            break
    print(cnt)

solution()