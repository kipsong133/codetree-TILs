input_time = input().split(":") # ["5", "45"]
hour = int(input_time[0])
minute = input_time[1]
result = f"{hour + 1}:{minute}"
print(result)