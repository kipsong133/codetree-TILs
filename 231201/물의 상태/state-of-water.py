def solution():
    temperature = int(input()) # -13
    if temperature < 0:
        print("ice")
    elif temperature >= 100:
        print("vapor")
    else:
        print("water")



solution()