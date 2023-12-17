n, m = list(map(int, input().split()))

def find_lcm(n: int, m: int) -> int:
    result: list[int] = []
    min_value: int = min(n, m)
    for i in range(2, min_value + 1):
        if i == min_value:
            result.append(n)
            result.append(m)

        if n % i == 0 and m % i == 0:
            n = n // i
            m = m // i 
            result.append(i)
            continue
    
    mutiple_value: int = 1 
    
    for i in result:
        mutiple_value = mutiple_value * i
    return mutiple_value


print(find_lcm(n, m))