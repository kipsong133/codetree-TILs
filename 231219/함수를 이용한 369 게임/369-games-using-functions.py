# input
a, b = tuple(map(int, input().split()))


def has_369(n: int) -> bool:
    num = str(n)
    for i in range(len(num)):
        if num[i] == '3' or num[i] == '6' or num[i] == '9':
            return True
    return False

def is_magic_number(n: int) -> bool:
    if has_369(n):
        return True
    if n % 3 == 0:
        return True
    return False



cnt = 0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt += 1

print(cnt)