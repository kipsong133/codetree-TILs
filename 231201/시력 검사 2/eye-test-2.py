def solution():
    eye_index = float(input()) # 1.3

    if eye_index >= 1.0:
        print("High")
    elif eye_index >= 0.5:
        print("Middle")
    else:
        print("Low")
    return

solution()