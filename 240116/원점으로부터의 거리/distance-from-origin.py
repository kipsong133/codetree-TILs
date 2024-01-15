def get_distance(x: int, y: int) -> int:
    return abs(x - 0) + abs(y - 0)

# input
N = int(input())
points = []
while True:
    if len(points) >= N:
        break
    x, y = map(int, tuple(input().split()))
    distance = get_distance(x, y)
    index = len(points) + 1
    points.append((int(x), int(y), distance, index))

points.sort(key=lambda x: (x[2], x[3]))
for p in points:
    print(p[3])