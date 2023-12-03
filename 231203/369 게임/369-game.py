def solution():
    # input: 12
    n = int(input()) # 12

    # Iteration 1 ~ input+1
    n_index = 1
    while n_index < n+1:
        if is_multiple_3(n_index):
            print(0, end = ' ')
            n_index += 1
            continue

        str_n = str(n_index) # '12'
        if has_369(str_n):
            print(0, end = ' ')
            n_index += 1
            continue
        print(n_index, end = ' ')
        n_index += 1

def is_multiple_3(num: int):
    return num % 3 == 0
    
def has_369(num: str): # '3'
    i = 0
    while i < len(num):
        if num[i] == '3' or num[i] == '6' or num[i] == '9':
            i += 1
            return True
        i += 1
    return False
solution()