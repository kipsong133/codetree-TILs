N, i = input().split() # N개, i 번째
arr = [0] + list(map(int, input().split())) # [1, 2, 1]
arr.sort()
print(arr[int(i)])