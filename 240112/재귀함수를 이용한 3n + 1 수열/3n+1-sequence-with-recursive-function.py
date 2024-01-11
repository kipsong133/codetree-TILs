cnt = 0

def solution(num: int):
    global cnt
    if num <= 1: return cnt
    cnt += 1
    if num % 2 == 0:
        return solution(int(num / 2))
    else:
        return solution(num * 3 + 1)

# input
n = int(input()) # 3
print(solution(n))