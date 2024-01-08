n = int(input())

def print_star(n: int):
    if n == 0:
        return
    print_star(n - 1)
    print("*" * n)

print_star(n)