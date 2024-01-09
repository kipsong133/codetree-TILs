# sum position number
def sum_pos(n: int) -> int:
    # 탈출조건: n이 10 이하면, 10이하로 나눠도 무의미하다. 해당 값을 리턴하며 재귀를 탈출한다.
    if n < 10:
        return n**2

    # 덧셈방식: 나머지값과 몫을 이용한다
    # 나머지값은 자리수의 값이다. 몫은 다음 자리수를 구하기 위한 값이다.
    # sum_pos(65432) + 1 -> sum_pos(6543) + 2 -> sum_pos(654) + 3 ...
    # 6 + 5 + 4 + 3 + 2 + 1
    return sum_pos(n // 10) + (n % 10)**2


# input
n = int(input()) # 654321
result: int = sum_pos(n)
print(result) # 21