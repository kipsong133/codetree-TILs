# input
n = int(input()) # 5
arr = list(map(int, input().split())) # [1, 2, 3, 4, 5]

for i in range(n):
    # 0부터 시작하니까, 짝수Index가 홀수번째 데이터임
    if i % 2 == 0: 
        #  arr의 홀수번쨰까지 slicing + sorted
        sorted_arr = sorted(arr[:i + 1]) # slice마지막을 포함하기 위해 "+1"
        # 만약 마지막 5번째면 i == 4, 그러면 중앙값은 index 상으로 2 이다.
        # i // 2 == 2 이므로,
        print(sorted_arr[i // 2], end = " ")