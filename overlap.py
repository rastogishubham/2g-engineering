#!/usr/bin/env python2.7


'''
This is a program to check if two 4 sided shapes intersect or not

Correct input should be given in the format shown below:

p2                 p3
o-----------------o
|                 |
|                 |
|                 |
|                 |
|                 |
o-----------------o
p1                p4

input order should be p1, p2, p3, p4

This or any order where the adjacent point comes next should be used,
since the code doesn't check for diagonals vs edges, that is a complex
problem, which can vary depending on the kind of shape the points will
represent.

Edges are drawn by taking p1-p2, p2-p3, p3-p4, p4-p1, therefore an order
of entry that causes diagonals to be drawn will not yeild the desired result

The code can find the overlap between any kind of 4-sided shapes, provided
the order in which the points are entered do not violate the rules of entry

The algorithm checks if one point of a Quadilateral is inside the other Quadilateral.
It does so, by drawing a line from a point to the right most x coordinate. If the Point
is inside the Quadilateral, it will have an odd number of intersections with edges of the Quadilateral,
therefore, the Quadilateral's will be overlapped
'''

class Quadilateral:
	def __init__(self, list_points):
		self.shape = list_points

	def getLines(self):
		list_points = self.shape
		list_lines = []
		for i in range(0, 4):
			next = (i+1) % 4
			temp_line = Line(list_points[i], list_points[next])
			list_lines.append(temp_line)
		return list_lines

	def printQuad(self):
		for point in self.shape:
			point.printPoint()
		print '\n'

	def getRightMostPoint(self):
		return max(self.shape[0].X, self.shape[1].X, self.shape[2].X, self.shape[3].X)


class Line:
	def __init__(self, p1, p2):
		self.line_seg = [p1, p2]

	def printLine(self):
		for point in self.line_seg:
			point.printPoint()
		print '\n'
	# Given three colinear points p, q, r, the function checks if
	# point q lies on line segment 'pr'
	def onSegment(self, p, q, r):
		if q.X <= max(p.X, r.X) and q.X >= min(p.X, r.X) and q.Y <= max(p.Y, r.Y) and q.Y >= min(p.Y, r.Y):
			return True
		return False
	# To find orientation of ordered triplet (p, q, r).
	# The function returns following values
	# 0 --> p, q and r are colinear
	# 1 --> Clockwise
	# 2 --> Counterclockwise
	def orientation(self, p, q, r):
		value = (q.Y - p.Y) * (r.X - q.X) - (q.X - p.X) * (r.Y - q.Y)

		if value == 0:
			return 0
		elif value > 0:
			return 1
		else:
			return 2

	# The function that returns true if line segment 'p1q1'
	# and 'p2q2' intersect.
	def doesIntersect(self, line):
		orient_1 = self.orientation(self.line_seg[0], self.line_seg[1], line.line_seg[0])
		orient_2 = self.orientation(self.line_seg[0], self.line_seg[1], line.line_seg[1])
		orient_3 = self.orientation(line.line_seg[0], line.line_seg[1], self.line_seg[0])
		orient_4 = self.orientation(line.line_seg[0], line.line_seg[1], self.line_seg[1])

		if orient_1 != orient_2 and orient_3 != orient_4:
			return True
		# p1, q1 and p2 are colinear and p2 lies on segment p1q1
		if orient_1 == 0 and self.onSegment(self.line_seg[0], line.line_seg[0], self.line_seg[1]):
			return True
		# p1, q1 and p2 are colinear and q2 lies on segment p1q1
		elif orient_2 == 0 and self.onSegment(self.line_seg[0], line.line_seg[1], self.line_seg[1]):
			return True
		# p2, q2 and p1 are colinear and p1 lies on segment p2q2
		elif orient_3 == 0 and self.onSegment(line.line_seg[0], self.line_seg[0], line.line_seg[1]):
			return True
		# p2, q2 and q1 are colinear and q1 lies on segment p2q2
		elif orient_4 == 0 and self.onSegment(line.line_seg[0], self.line_seg[1], line.line_seg[1]):
			return True
		else:
			return False


class Point:
	def __init__(self, x, y):
		self.X = x
		self.Y = y

	def printPoint(self):
		print '({} , {})'.format(self.X, self.Y)



def isInside(q1, q2, rightMost):
	list_line_seg = q1.getLines()
	count = 0
	for p in q2.shape:
		new_line = Line(p, Point(rightMost, p.Y))
		for temp_line in list_line_seg:
			if temp_line.doesIntersect(new_line):
				count += 1
	if count % 2 == 0:
		return False
	else:
		return True

def doesOverlap(q1, q2):
	rightMost = max(q1.getRightMostPoint() + 1, q2.getRightMostPoint() + 1)
	if isInside(q1, q2, rightMost) or isInside(q2, q1, rightMost):
		return True
	else:
		return False

def getPoints(num):
	list_points = []
	for i in range(0, 4):
		suffix = ''
		if i == 0:
			suffix = 'st'
		elif i == 1:
			suffix = 'nd'
		elif i == 2:
			suffix = 'rd'
		else:
			suffix = 'th'
		x = float(raw_input('Enter {}'.format(i+1) + suffix + ' x coordinate for shape #{}: '.format(num)))
		y = float(raw_input('Enter {}'.format(i+1) + suffix + ' y coordinate for shape #{}: '.format(num)))
		temp_point = Point(x, y)
		list_points.append(temp_point)
	return list_points

def main():

	#Test case 1: One shape inside another
	print '\nTest case 1: One shape inside another:'
	p1 = Point(0, 0)
	p2 = Point(0, 10)
	p3 = Point(10, 10)
	p4 = Point(10, 0)
	q1 = Quadilateral([p1, p2, p3, p4])

	print 'Quadilateral 1:'

	q1.printQuad()

	p5 = Point(1, 1)
	p6 = Point(1, 5)
	p7 = Point(5, 5)
	p8 = Point(5, 1)
	q2 = Quadilateral([p5, p6, p7, p8])

	print 'Quadilateral 2'

	q2.printQuad()

	print 'Does Q1 overlap with Q2?'
	print doesOverlap(q1, q2)

	#Test case 2: One shape touching the other
	print '\nTest case 2: One shape touching the other:'
	p1 = Point(0, 0)
	p2 = Point(0, 10)
	p3 = Point(10, 10)
	p4 = Point(10, 0)
	q1 = Quadilateral([p1, p2, p3, p4])

	print 'Quadilateral 1:'

	q1.printQuad()

	p5 = Point(10, 7)
	p6 = Point(10, 15)
	p7 = Point(15, 15)
	p8 = Point(15, 10)
	q2 = Quadilateral([p5, p6, p7, p8])

	print 'Quadilateral 2:'

	q2.printQuad()

	print 'Does Q1 overlap with Q2?'
	print doesOverlap(q1, q2)

	#Test case 3: One shape overlapping the other
	print '\nTest case 3: One shape overlapping the other:'
	p1 = Point(0, 0)
	p2 = Point(0, 10)
	p3 = Point(10, 10)
	p4 = Point(10, 0)
	q1 = Quadilateral([p1, p2, p3, p4])

	print 'Quadilateral 1:'

	q1.printQuad()

	p5 = Point(5, 7)
	p6 = Point(5, 15)
	p7 = Point(15, 15)
	p8 = Point(15, 7)
	q2 = Quadilateral([p5, p6, p7, p8])

	print 'Quadilateral 2:'

	q2.printQuad()

	print 'Does Q1 overlap with Q2?'
	print doesOverlap(q1, q2)

	#Test case 4: Shapes not overlapping at all
	print '\n#Test case 4: Shapes not overlapping at all:'
	p1 = Point(0, 0)
	p2 = Point(10, 0)
	p3 = Point(10, 10)
	p4 = Point(0, 10)
	q1 = Quadilateral([p1, p2, p3, p4])

	print 'Quadilateral 1:'

	q1.printQuad()

	p5 = Point(15, 15)
	p6 = Point(25, 15)
	p7 = Point(25, 25)
	p8 = Point(15, 25)
	q2 = Quadilateral([p5, p6, p7, p8])

	print 'Quadilateral 2:'

	q2.printQuad()

	print 'Does Q1 overlap with Q2?'
	print doesOverlap(q1, q2)

	print '\n\nEnd of sample testcases'

	print '\nCustom test case begins\n'

	q1 = Quadilateral(getPoints(1))
	q2 = Quadilateral(getPoints(2))

	overlap = doesOverlap(q1, q2)

	if overlap:
		print 'The two Quadilaterals overlap'
	else:
		print 'The two Quadilaterals do not overlap'



if __name__ == '__main__':
	main()
