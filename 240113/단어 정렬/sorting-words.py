# input
n = int(input()) # 7
arr: [str] = []
while True:
    if len(arr) == n: break
    arr.append(input())

arr.sort()

def print_out(i: int):
    if i == 0: 
        print(arr[0])
        return
    print_out(i - 1)
    print(arr[i])
    return

print_out(n-1)