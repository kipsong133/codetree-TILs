def solution():
    # input().split()으로 입력 값을 공백으로 분리한 뒤, map 함수를 사용해 각 값을 int로 변환하여 리스트로 만듭니다.
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    c = input_arr[2]

    # -100보다 큰 값이 필요하므로 최대값을 찾기 위해 초기 값을 아주 작은 수로 설정하는 것이 좋습니다.
    maximum = -float('inf')
    for num in [a, b, c]:
        if num > maximum:
            maximum = num
    
    print(maximum)

solution()