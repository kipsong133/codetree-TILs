# input
m1, d1, m2, d2 = tuple(map(int, input().split()))

# get num of day
def get_num_of_day(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt_day = 0
    # month
    for i in range(1, m):
        cnt_day += days[i]

    # day    
    cnt_day += d
    return cnt_day

# output
def solution():
    if m1 < 1 or m2 > 12 or d1 < 1 or d2 >31:
        return
    start = get_num_of_day(m1, d1)
    end = get_num_of_day(m2, d2)
    between: int = end - start
    index: int = between % 7

    mapping_day = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fir",
        5: "Sat",
        6: "Sun"
    }
    
    print(mapping_day[index])

    

solution()