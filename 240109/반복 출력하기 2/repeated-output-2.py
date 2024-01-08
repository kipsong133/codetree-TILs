def print_out(n: int):
    if n == 0:
        return
    print_out(n - 1)
    print("HelloWorld")


n = int(input())
print_out(n)