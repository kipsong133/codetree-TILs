n = int(input())

def count_number(a):
    if a == 1: return 0

    if a % 2 == 0:
        return count_number(a // 2) + 1
    else:
        return count_number(a * 3 + 1) + 1

print(count_number(n))