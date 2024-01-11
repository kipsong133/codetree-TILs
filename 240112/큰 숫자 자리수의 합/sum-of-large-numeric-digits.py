from functools import reduce

mutiple_element = lambda x, y: x * y

def sum_pos(num: int): 
    if num < 10: return num

    pos_num = num % 10
    remainder = int(num // 10)
    return sum_pos(remainder) + pos_num


# input
arr: [int] = list(map(int, input().split())) # [123, 456, 789]
multi_result: int = reduce(mutiple_element, arr)

result: int = sum_pos(multi_result)
print(result)