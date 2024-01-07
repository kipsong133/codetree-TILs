# n개의 원소 m의 공백
n, m = tuple(map(int, input().split())) # 5 4
arr = list(map(int, input().split())) # [5, 4, 3, 2, 1]

def calculateElements(num: int) -> int:
    cnt = 0
    while num != 1:
        cnt += num
        if num % 2 == 0:
            num /= 2
        else:
           num -= 1
    return cnt

def solution():
    # validation
    if (m > n):
        return
    
    input_num: int = arr[m]
    result: int = calculateElements(input_num)
    print(result)

solution()