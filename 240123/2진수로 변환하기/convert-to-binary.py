# input
n = int(input())

# get digit
def get_digit(num: int) -> int:
    digit = []
    while True:
        if num <= 1:
            digit.append(num)
            break
        digit.append(num % 2)
        num //= 2
    return digit

digits: [int] = get_digit(n)

for digit in digits[::-1]:
    print(digit, end="")