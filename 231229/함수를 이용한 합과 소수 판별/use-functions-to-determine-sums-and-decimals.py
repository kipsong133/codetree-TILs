a,b = tuple(map(int, input().split()))
cnt = 0

def sum_position(num: int) -> int:
    temp = []
    while num != 0:
        temp.append(num % 10)
        num = num // 10
    return sum(temp)

def unique_num(num: int):
  return all(num % i != 0 for i in range(2, num)) 

def recursive(a: int, b: int):
  global cnt
  if a > b:
      return
  sum_result = sum_position(a)
  if sum_result % 2 == 0 and unique_num(a):
    cnt += 1
  a += 1
  recursive(a, b)

def solution():
    recursive(a, b)
    print(cnt)

solution()