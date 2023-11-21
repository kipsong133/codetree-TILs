input_values: list[str] = input().split()

result: int = 1
for i in input_values:
    result = result * int(i)

print(result)