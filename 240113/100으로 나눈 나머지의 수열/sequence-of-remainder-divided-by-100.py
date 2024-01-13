def recurrence(n: int):
    if n == 1: return 2
    if n == 2: return 4
    return (recurrence(n - 1) * recurrence(n - 2)) % 100
    
N = int(input()) # 5
print(recurrence(N))