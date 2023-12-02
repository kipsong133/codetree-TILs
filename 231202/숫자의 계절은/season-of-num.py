def solution():
    # Input: 1 (월)
    month = int(input())

    if month < 3:
        print("Winter")
        return
    if month < 6:
        print("Spring")
        return
    if month < 9:
        print("Summer")
        return
    if month < 11:
        print("Fall")
        return
    else:
        print("Winter")
        return


solution()