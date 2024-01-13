N = int(input()) # (N / 2)개
arr = list(map(int, input().split()))
arr.sort()

group_sum = 0
group_max = 0

for i in range(N): # 0, 1
    group_sum = arr[i] + arr[2*N -1 - i]
    if group_sum > group_max:
       group_max = group_sum

print(group_max)