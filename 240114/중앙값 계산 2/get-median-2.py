# input
n = int(input()) # 5
arr = list(map(int, input().split())) # [1, 2, 3, 4, 5]

result: [int] = []
temp: [int] = []
for i in range(0, len(arr)):
    temp.append(arr[i]) # 1, 2, 3
    if (i+1) % 2 == 1:
        temp.sort()
        mid_index = int(len(temp) / 2)
        result.append(str(temp[mid_index]))

solution = " ".join(result)
print(solution)