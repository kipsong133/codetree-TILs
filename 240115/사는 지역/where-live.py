class Address:
	def __init__(self, name, address, region):
		self.name = name
		self.address = address
		self.region = region

	def __lt__(self, other):
		return self.name < other.name

cnt = int(input())
persons: [Address] = []
while True:
    if len(persons) >= cnt:
        break
    name, address, region = tuple(input().split())
    persons.append(Address(name, address, region))

persons.sort()
target = persons[-1]
print(f"name {target.name}")
print(f"addr {target.address}")
print(f"city {target.region}")