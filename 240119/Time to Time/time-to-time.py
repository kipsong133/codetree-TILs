# input
a, b, c, d = tuple(map(int, input().split()))

def calculate_time(a,b, elapsed_time):
    global c
    global d

    # 리턴 조건
    if a == c and b == d:
        return elapsed_time
    
    if b == 60:
        a += 1
        b = 0
    
    return calculate_time(a, b+1, elapsed_time + 1)
    
print(calculate_time(a, b, 0))