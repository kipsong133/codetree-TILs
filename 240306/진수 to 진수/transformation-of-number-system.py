# 입력 받기
a, b = list(map(int, input().split())) # 예시: 8 2
n = int(input(), a) # 11, 입력 받은 숫자를 a 진수로 해석하여 10진수로 변환

# 10진수를 b 진수로 변환하는 함수
def to_base_b(num, base): # 8 진수 -> 2 진수  11(8), 2 
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    digits.reverse()
    return ''.join(digits)

# 결과 출력
print(to_base_b(n, b))