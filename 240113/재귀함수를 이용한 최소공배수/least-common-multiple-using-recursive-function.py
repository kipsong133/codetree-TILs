def lcm(a, b):
	gcd = 1
	for i in range(1, min(a,b) + 1):
		if a % i == 0 and b % i == 0:
			gcd = i
	return a * b // gcd


def lcm_all(index: int):
	if index == 0: return arr[index]
	return lcm(lcm_all(index - 1), arr[index])

n = int(input())
arr = list(map(int, input().split()))
print(lcm_all(5))