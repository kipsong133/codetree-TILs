# input
m1, d1, m2, d2 = tuple(map(int,input().split()))
target_day = input()

# get elapsed date
def get_lapsed_date(m, d):
    # 월 마지막 날짜
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    cnt = 0
    for i in range(1, m):
        cnt += days[i]
    
    cnt += d
    return cnt

def get_day(date: str):
    date_map = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }
    return date_map[date]


# cal num of day
def calcuate_num_of_day():
    between = get_lapsed_date(m2, d2) - get_lapsed_date(m1, d1)
    cnt = 0
    
    rotate = between // 7 
    cnt += rotate

    remain = between % 7

    date_idx = get_day(target_day) # 0 ~ 6
    if remain >= date_idx:
        cnt += 1
    
    return cnt

# ouput
def solution():
    answer = calcuate_num_of_day()
    print(answer)

solution()