def ascend(i: int):
    if i == n - 1: 
        print(arr[i], end = " ")
        return arr[i]
    print(arr[i], end = " ")
    return ascend(i + 1)

def descend(i: int):
    if i == 0:
        print(arr[0], end = " ")
        return arr[0]

    print(arr[i], end = " ")
    return descend(i - 1)

# input
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ascend(0)
print()
descend(n - 1)