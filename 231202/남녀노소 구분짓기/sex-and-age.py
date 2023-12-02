def solution():
    # MAN, BOY: 0 / WOMAN, GIRL: 1 / 
    # 19 > == adult

    # 0
    # 23
    sex = int(input())
    age = int(input())

    if sex == 0:
        # MAN , BOY
        if 19 <= age:
            print("MAN")
        else:
            print("BOY")
    else:
        # WOMAN, GIRL
        if 19 <= age:
            print("WOMAN")
        else:
            print("GIRL")



solution()