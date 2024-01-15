class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

def print_out(title: str, arr: [Person]):
    print(title)
    for e in arr:
        print(e.name, e.height, e.weight)
        


persons = []

while True:
    if len(persons) >= 5:
        break
    name, height, weight = tuple(input().split())
    persons.append(Person(name, int(height), weight))

persons.sort(key=lambda x: x.name)
print_out("name", persons)
print("")
persons.sort(key=lambda x: -(x.height))
print_out("height", persons)