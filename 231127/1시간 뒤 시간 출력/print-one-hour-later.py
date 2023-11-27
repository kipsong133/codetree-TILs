input_time = input()
input_time = input_time.split(":")
hour = int(input_time[0]) + 1
minute = input_time[1]
print(f"{hour}:{minute}")