def is_magic_number(x: int) -> bool:
    if x % 2 == 0:
        return False

    position: int = len(str(x))
    first: int = int(str(x)[position - 1])
    if first == 5:
        return False

    if x % 3 == 0:
        return False

    if x % 9 != 0:
        return False

    return True


a, b = tuple(map(int, input().split()))

cnt = 0
for i in range(a, b + 1):
    if is_magic_number(i):
        cnt += 1

print(cnt)