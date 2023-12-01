def solution():
    left = float(input())
    right = float(input())

    if left >= 1.0 and right >= 1.0:
        print("High")
        return

    if left > 0.5 and right >= 0.5:
        print("Middle")
        return
    
    print("Low")
    return


solution()