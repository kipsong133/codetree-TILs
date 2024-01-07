n, m = tuple(map(int, input().split())) # 5 4
arr = [0] + list(map(int, input().split())) # 서수 표기법이 문제에서 조금 다르게 나와있어서 맞추기 위해 추가
def get_answer():
    global m # 4

    return_value:int = 0
    while m: # m == 1 이 되면 false가 되어서 탈출된다.
        return_value += arr[m]

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1

    return return_value

print(get_answer())