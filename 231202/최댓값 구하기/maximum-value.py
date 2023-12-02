# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# a와 b를 비교한뒤, a가 b보다 크다면 a와 c를 비교하여 최댓값을 구합니다.
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)

# a와 b를 비교한 결과가 나와있으므로, b와 c만 비교하여 최댓값을 구합니다.
else:
    if b >= c:
        print(b)
    else:
        print(c)