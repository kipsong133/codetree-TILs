def solution():
    input_key = input() # str
    result = converFrom(input_key)
    print(result)

def converFrom(key: str):
    dic = {
        "S": "Superior",
        "A": "Excellent",
        "B": "Good",
        "C": "Usually",
        "D": "Effort"
    }
    return dic.get(key, "Failure")

solution()