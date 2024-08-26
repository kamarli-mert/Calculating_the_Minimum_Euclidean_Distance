import math

def euclideanDistance(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

points = []
while len(points) <= 1:
    input_str = input("Enter a point (x, y) or 'q' to exit: ")
    if input_str.lower() == 'q':
        break
    try:
        x, y = map(int, input_str.strip('()').split(','))
        points.append((x, y))
    except ValueError:
        print("Invalid entry. Please enter a point in (x, y) format.")

if len(points) == 2:
  distance = euclideanDistance(points[0], points[1])
  print("Minimum distance between two points:", distance)