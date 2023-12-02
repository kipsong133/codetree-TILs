def solution():
    # Input: 15
    n = int(input())

    if (n % 2 == 1 and n % 3 == 0):
        print("true")
        return

    if (n % 2 == 0  and n % 5 == 0):
        print("true")
        return
    print("false")
    
solution()