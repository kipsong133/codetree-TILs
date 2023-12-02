def solution():
    # hasSymtom: "Y" / "N"
    # Input: temper
    # "Y", 37 <= temper, "A"
    # "N", 37 <= temper, "B"
    # "Y", temper < 37, "C"
    # "D"

    # Y, 38
    a = list(input().split(" "))
    b = list(input().split(" "))
    c = list(input().split(" "))

    # Two A -> "E"
    # else " N"
    
    a_count = 0
    for person in [a, b, c]:
        if person[0] == "Y":
            if int(person[1]) >=37:
                a_count += 1
                if (a_count == 2):
                    print("E")
                    return
    print("N")

solution()