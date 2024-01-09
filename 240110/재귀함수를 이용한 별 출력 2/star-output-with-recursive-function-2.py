def print_star(n: int):
    # 탈출조건
    if n == 0: 
        return
    
    # 5 -> 4 -> 3 -> 2-> 1
    print("* " * n)
    print_star(n - 1)

    # 1 -> 2 -> 3 -> 4 -> 5
    print("* " * n)

# input
n = int(input()) # 5
print_star(n)