class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
persons = []

while True:
    if len(persons) >= n:
        break

    name, height, weight = tuple(input().split())
    persons.append(Person(name, int(height), int(weight)))

persons.sort(key=lambda x: (x.height, -x.weight))

for p in persons:
    print(p.name, p.height, p.weight)