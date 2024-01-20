# input
m1, d1, m2, d2 = tuple(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# simulating
# m1.d1 -> m2.d2
# elapsed_day = 0
def count_days(m1, d1, m2, d2, elapsed_day): 
    if m1 == m2 and d1 == d2:
        return elapsed_day
    
    if d1 > num_of_days[m1]:
        m1 += 1
        d1 = 0

    return count_days(m1, d1+1, m2, d2, elapsed_day+1)
    

# output
print(count_days(m1, d1, m2, d2, 1))