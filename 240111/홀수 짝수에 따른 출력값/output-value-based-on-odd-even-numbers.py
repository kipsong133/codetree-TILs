def f(n: int) -> int:
    global is_odd

    if n < 1: return -1
    if is_odd:
        # 짝수
        if n == 2: return 2    
    else:
        # 홀수
        if n == 1: return 1
    return n + f(n - 2)
    

# input
N = int(input())
is_odd: bool = (N % 2 == 0)
result = f(N)
print(result)