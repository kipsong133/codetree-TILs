# class deifinition
class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

# input
n = int(input())
arr = [
    tuple(map(int, input().split())) for _ in range(n)
]

students = [
    Student(e[0], e[1], i+1) for i, e in enumerate(arr)
]

# sort
students.sort(key=lambda x: (x.height, -x.weight))


# ouput
for i, e in enumerate(students):
    print(e.height, e.weight, e.number)