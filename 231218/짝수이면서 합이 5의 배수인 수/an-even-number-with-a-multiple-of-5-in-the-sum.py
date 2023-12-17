def is_magic_num(n: int) -> bool:
    if n % 2 != 0:
        return False
    
    first = n % 10
    second = n // 10

    if (first + second) % 5 != 0:
        return False
    return True

# 2 자리 숫자 n
n = int(input())

if is_magic_num(n):
    print("Yes")
else:
    print("No")