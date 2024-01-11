def sum_pos(num: int):
    if num < 10: return num
    return sum_pos(num // 10) + num % 10

# input
a, b, c = tuple(map(int, input().split())) # 123 456 789
print(sum_pos(a * b * c))