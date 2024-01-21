# input
a, b, c = tuple(map(int, input().split()))


# get num of minute
def get_num_of_min(day, hour, minute):
    cnt_min = 0

    # day
    cnt_min += day * 1440

    # hour
    cnt_min += hour * 60

    # minute remainder
    cnt_min += minute

    return cnt_min


# ouput
start_min = get_num_of_min(11, 11, 11)
end_min = get_num_of_min(a, b, c)
print(end_min - start_min)