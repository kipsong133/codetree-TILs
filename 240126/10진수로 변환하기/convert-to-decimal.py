# input
n_str = input()
n_int_arr = [int(digit) for digit in n_str]

num = 0
for i in range(len(n_int_arr)):
    num = num * 2 + n_int_arr[i]

print(num)