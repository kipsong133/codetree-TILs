class Number:
    def __init__(self, number, index):
        self.number = number
        self.index = index

n = int(input())
arr = list(map(int,input().split()))
numbers = [
    Number(num, idx) for idx, num in enumerate(arr)
]

answer = [0 for _ in range(n)]

numbers.sort(key=lambda x: (x.number, x.index))

for idx, num in enumerate(numbers):
    answer[num.index] = idx + 1

for e in answer:
    print(e, end = " ")