# inputs
m, d = tuple(map(int, input().split()))

# validate input
def valiate_input(m, d) -> bool:
    # validate: month 
    if m < 1 or m > 12:
        return False
    # validate: day
    if d < 1 or d > 31:
        return False
    return True

def has_date(m: int, d: int) -> bool:
    """
    조건
    - 21년도는 윤년이 있으므로 2/28일이 있음
    - 월마다 30 or 31 인지만 확인하면 된다.
    """
    has_31 = {
        1, 3, 5, 7, 8, 10 ,12
    }
    if d == 31:
        return m in has_31
    return True
        


    return True

def solution():
    if not valiate_input(m, d):
        print("No")
        return

    if has_date(m, d):
        print("Yes")
    else:
        print("No")

    return

solution()