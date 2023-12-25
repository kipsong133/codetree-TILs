def add(x: int, y: int) -> int:
    return x + y

def substract(x: int, y: int) -> int:
    return x - y

def mutiple(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> int:
    return int(x / y)

def validation(num: int) -> bool:
    return type(num) is int


def solution(): 
    # input
    x, operator, y = list(input().split())
    x = int(x)
    y = int(y)

    # validation
    if not validation(x):
        return
    if not validation(y):
        return
    
    result: int = 0
    match operator:
        case "*":
            result = mutiple(x, y)
        case "/":
            result = divide(x, y)
        case "+":
            result = add(x, y)
        case "-":
            result = substract(x, y)
    
    print(f"{x} {operator} {y} = {result}")




solution()