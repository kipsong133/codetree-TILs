def is_multiple_4(n: int) -> bool:
    return n % 4 == 0

def is_mutiple_100(n: int) -> bool:
    return n % 100 == 0

def is_mutiple_400(n: int) -> bool:
    return n % 400 == 0

def solution():
    # input: 2020
    y = int(input())

    if not is_multiple_4(y):
        return False
    # 4's multiple

    if is_mutiple_100(y):
        return False

    # 4 mutiple & not 100 multiple
    if is_mutiple_400(y):
        return False

    # 4 multiple & not 100 multiple & 400 mutiple
    return True

result = solution()
if result:
    print("true")
else:
    print("false")