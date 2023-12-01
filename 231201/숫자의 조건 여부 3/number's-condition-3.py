def solution():
    # Input: 13
    a = int(input())

    if a % 13 == 0 or a % 19 == 0:
        print("True")
    else:
        print("False")



solution()