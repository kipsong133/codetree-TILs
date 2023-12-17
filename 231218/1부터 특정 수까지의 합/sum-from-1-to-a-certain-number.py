# input: 1 ~ 23 
n = int(input())

# (1 + 2 + 3 + 4 + ... + 23) // 10
def calculate(n: int) -> int:
    sum_result = 0
    for i in range (1, n + 1):
        sum_result += i
    return int(sum_result // 10)

def print_out(n: int):
    print(n)

result = calculate(n)
print_out(result)