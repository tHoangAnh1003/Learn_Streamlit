import matplotlib.pyplot as plt


def get_points():
    points = []
    n = 10
    while n != 0:
        x, y = map(int, input().split())
        points.append((x, y))
        n -= 1
    return points


points = get_points()

if points:
        points.append(points[0])

x, y = zip(*points)

plt.figure()
plt.plot(x, y, marker='o')

plt.title('Polygon Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
