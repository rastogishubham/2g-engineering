class Point:
	def ___init__(self, x, y):
		self.coordinate = (x, y)

class Quadilateral:
	def __init__(self, p1, p2, p3, p4):
		self.shape = [p1, p2, p3, p4]

	def getLines(self):
		list_points = self.shape
		list_lines = []
		for i in range(0, 4):
			for j in range(i+1, 4):
				temp_line = Line(list_points[i], list_points[j])
				list_lines.append(temp_line)
		return list_lines

class Line:
	def __init__(self, p1, p2):
		self.line_seg = [p1, p2]

def main():
	p1 = Point(0, 0)
	p2 = Point(0, 10)
	p3 = Point(10, 10)
	p4 = Point(10, 0)

	q1 = Quadilateral(p1, p2, p3, p4)

	list_lines = q1.getLines()

	print list_lines

if __name__ == '__main__':
	main()