n = int(input()) # 5

# N -> (N - 1) -> (N - 2) ... -> 1
# 1 -> 2 -> ... -> N

def recur(n: int):
    if n < 1: return

    # 5 -> 4 -> 3 -> 2 -> 1
    print(n, end = " ")
    recur(n - 1)
    # 1 -> 2 -> 3 -> 4 -> 5
    print(n, end = " ")

recur(n)