# input
m1, d1, m2, d2 = tuple(map(int, input().split()))


# calcuate days 1 ~ m 까지
def get_num_of_days(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_cnt = 0

    # 월 먼저 더한다.
    for i in range(1, m):
        day_cnt += days[i]

    # 남은 일을 더한다.
    day_cnt += d
    return day_cnt




total_days = get_num_of_days(m2, d2) - get_num_of_days(m1, d1) + 1
print(total_days)