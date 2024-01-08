n = int(input()) # 7
# 1 ~ N
# N ~ 1

def print_num(num: int):
    if num == 0:
        return

    print_num(num - 1)
    print(num, end = " ")
    
def print_num2(num: int):
    if num == 0:
        return
    print(num, end = " ")
    print_num2(num - 1)
    


print_num(n)
print()
print_num2(n)