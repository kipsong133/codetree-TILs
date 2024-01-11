def find_max(arr: [int], big) -> int:
    # 탈출 조건
    if len(arr) == 0: return big
    
    bigger: int = 0
    if arr[0] >= big:
        bigger = arr[0]
    else:
        bigger = big

    return find_max(arr[1:], bigger)
    

def solution():
    # input 
    n = int(input()) # 6
    arr = list(map(int, input().split())) # 1 5 7 9 2 6

    if n != len(arr): return
    if n < 1: return
    if n > 100: return

    max_num = find_max(arr, 0)
    print(max_num)

solution()