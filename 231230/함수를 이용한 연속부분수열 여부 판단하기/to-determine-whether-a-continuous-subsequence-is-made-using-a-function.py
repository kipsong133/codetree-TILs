# inputs
n1_count, n2_count = tuple(map(int, input().split()))

a = list(map(int, input().split())) # [2, 4, 6, 8, 5, 7]
b = list(map(int, input().split())) # [2, 4]

large = a if n1_count > n2_count else b
small = b if n1_count > n2_count else a

def is_same(index: int) -> bool:
    # Iteration: 4 -> 6 -> 8
    for i in range(len(small)):
        if small[i] != large[i + index]:
            return False
    return True


def is_part() -> bool:
    # Iteration: 2 -> 4 -> 6 -> 8
    for i in range(len(large) - len(small) + 1):
        # Check "is same?"
        if is_same(i):
            return True
    return False

if is_part():
    print("Yes")
else:
    print("No")