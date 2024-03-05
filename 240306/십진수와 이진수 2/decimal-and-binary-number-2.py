# 변수 선언 및 입력
binary = list(map(int, input()))
length = len(binary)

# 십진수로 변환합니다.
num = 0
for i in range(length):
    num = num * 2 + binary[i]

# 십진수에 17을 곱합니다.
num *= 17

digits = []

# 이진수로 변환합니다.
while True:
    if num < 2:
        digits.append(num)
        break
    digits.append(num % 2)
    num //= 2

for digit in digits[::-1]:
    print(digit, end="")