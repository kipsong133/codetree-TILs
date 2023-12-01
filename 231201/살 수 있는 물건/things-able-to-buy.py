def solution():
    # input: 3000원
    input_cash = int(input())
    
    # 0 ~ 999
    if input_cash < 1000:
        print("no")
        return

    # 3000 ~ 
    if input_cash >= 3000:
        print("book")
        return

    # 1000 ~ 2999
    print("mask")
    

solution()