class Person:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight
    
n = int(input())
persons = []

while True:
    if len(persons) >= n:
        break
    name, height, weight = tuple(input().split())
    persons.append(Person(name, height, weight))

persons.sort(key=lambda x: x.height)

for person in persons:
    print(person.name, person.height, person.weight)