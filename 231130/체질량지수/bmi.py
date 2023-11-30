def solution():
    # 키, 몸무게
    input_arr = list(map(int, input().split(" ")))

    height = input_arr[0]
    weight = input_arr[1]

    bmi_inddx = int((weight / (height * height)) * 100 * 100)
    print(bmi_inddx)
    if bmi_inddx >= 25:
        print("Obesity")
    


solution()