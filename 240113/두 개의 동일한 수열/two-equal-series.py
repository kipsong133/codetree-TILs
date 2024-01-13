n = int(input()) # n개의 원소
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort()

def solution():
    for i in range(0, n):
        if arr_a[i] != arr_b[i]:
            print("No")
            return
    print("Yes")

solution()