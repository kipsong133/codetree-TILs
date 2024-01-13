string = input() # "ababccaa"
list_str = list(string)
list_str.sort()

result = "".join(list_str)
print(result)