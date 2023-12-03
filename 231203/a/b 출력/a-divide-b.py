def solution():
    # input
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]

    # 정수
    print(f"{a//b}.", end = "")

    # 나머지
    a %= b

    # 20자리만큼 순회
    for _ in range(20):
        a *= 10
        print(a//b, end = "")
        a %= b
    
solution()