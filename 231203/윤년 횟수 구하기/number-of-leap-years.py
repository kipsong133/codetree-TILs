def solution():
    # input: 100
    # meanings: 100 년
    n = int(input())

    cnt = 0
    # Iteration: 1년부터 n년
    for year in range(1, n+1):
        if is_leap_year(year):
            cnt += 1
    print(cnt)

def is_leap_year(year: int):
    if year % 4 !=0:
        return False
    
    # mutiple of 4
    if year % 100 == 0 and year % 400 != 0:
        # Exception Condition
        return False
    return True

solution()