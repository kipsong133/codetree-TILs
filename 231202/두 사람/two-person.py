def solution():
    # Input: 20, M 
    a_info = list(input().split(" "))
    # Input: 20, W
    b_info = list(input().split(" "))

    for person in [a_info, b_info]:
        if int(person[0]) >= 19 and person[1] == "M":
            print(1)
            return
    print(0)



solution()