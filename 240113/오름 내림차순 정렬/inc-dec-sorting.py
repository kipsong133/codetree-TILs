# input
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 오름차순
for elem in arr:
    print(elem, end = " ")

print()

# 내림차순
arr.sort(reverse = True)
for elem in arr:
    print(elem, end = " ")