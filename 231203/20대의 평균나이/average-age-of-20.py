def solution():
    continue_input = True
    age_arr = []

    while continue_input:
        age = int(input())
        
        age_arr.append(age)
        continue_input = (age < 30 and 19 age)

    age_arr.pop()
    avg = sum(age_arr) / len(age_arr)
    print(f'{avg:.02f}')



solution()