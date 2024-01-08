# input
n, m = tuple(map(int, input().split())) # 6 4

# input array
arr = [0] + list(map(int, input().split())) 

# number of line: m
# a1 a2 => arr[a1] + arr[a2] => return value

def sum_between_two_index(start: int, end: int) -> int:
    global arr
    cnt: int = 0
    for i in range(start, end + 1):
        cnt += arr[i]
    return cnt

def solution():
    if n + 1 != len(arr):
        return
    
    global m
    for i in range(m): # 4회 순회
        # index 
        a1, a2 = tuple(map(int, input().split())) # 1 2

        result_value: int = sum_between_two_index(a1, a2)
        print(result_value)

solution()