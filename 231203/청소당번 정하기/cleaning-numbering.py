def solution():
    # input: 11
    n = int(input())

    # 교실청소: 2일
    # 복도청소: 3일
    # 화장실청소: 12일
    # 겹칠 시, 화장실 > 복도 > 교실 순으로 우선 청소한다.
    cnt_classroon = 0
    cnt_walkway = 0
    cnt_toliet = 0

    # Interation: 0일 ~ n일까지
    for day in range(1, n+1):
        # 화장실청소가 최우선
        if day % 12 == 0:
            cnt_toliet +=1
            continue
        # 복도청소
        if day % 3 == 0:
            cnt_walkway += 1
            continue

        # 교실청소
        if day % 2 == 0:
            cnt_classroon += 1
            continue

    # 교실청소 횟수와 복도청소 횟수를 출력한다.
    print(f'{cnt_classroon} {cnt_walkway} {cnt_toliet}')


solution()