input_arr = list(map(int, input().split(" ")))
a = input_arr[0]
b = input_arr[1]
c = input_arr[2]

maximum = -100
for num in [a, b, c]:
    if num > maximum:
        maximum = num
# if a > b:
#     if b > c:
#         print(a)
#     elif c > a:
#         print(c)
# else:
#     # b > a
#     if a > c:
#         print(b)
#     else: # c > a
#         if b > c:
#             print(b)    
#         else:
#             print(c)

print(maximum)