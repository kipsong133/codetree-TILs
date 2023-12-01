def solution():
    input_cash = int(input()) # 2,500
    result = choose_item(input_cash)
    print(result)

def choose_item(cash: int):
    if cash >= 3000:
        return "book"
    if cash >= 1000:
        return "mask"
    if  cash >= 500:
        return "pen"
    return "no"

solution()