MAX_DIGIT = 30

# 입력 받기
a, b = list(map(int, input().split())) # 예시: 8 2
n = input() # 11, 입력 받은 숫자를 a 진수로 해석하여 10진수로 변환

digits = []

# 10진수로 변환한다.
num = 0 # 10진수
for ch in n:
    # 지금까지 저장된 값에 8을 곱한다.
    # 이유는 왼쪽에서 오른쪽으로 이동중이므로
    # 만약 이렇게 하지 않으면, `reverse()`를 사용해서 곱해야한다.
    num = num * a + int(ch)

# b진수로 변환한다.
while True:
    if num < b:
        digits.append(num)
        break
    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end="")