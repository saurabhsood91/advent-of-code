import sys
from functools import reduce

RIGHT = 'R'
LEFT = 'L'
UP = 'U'
DOWN = 'D' 

def get_coordinates(wire):
  base = (0, 0)
  x, y = base

  coordinates = [base]

  for operation in wire:
    direction = operation[0]
    magnitude = int(operation[1:])

    if direction == RIGHT:
      x += magnitude
    elif direction == LEFT:
      x -= magnitude
    elif direction == UP:
      y += magnitude
    elif direction == DOWN:
      y -= magnitude
    else:
      # Need to take a long hard look in the mirror
      sys.exit(-1)
    coordinates.append((x, y))
  return coordinates


def get_intersection_point(point_line_a_1, point_line_a_2, point_line_b_1, point_line_b_2):
  x1, y1 = point_line_a_1
  x2, y2 = point_line_a_2
  x3, y3 = point_line_b_1
  x4, y4 = point_line_b_2

  if x1 == x2 and y3 == y4:
    # line a is vertical
    # line b is horizontal. y3 = y4
    # to intersect, line b has to be horizontal
    # lower, upper = [x3, x4].sort()
    bounds = [x3, x4]
    bounds.sort()
    lower, upper = bounds
    if x1 >= lower and x1 <= upper:
      # we have an intersection
      # x has to lie between x3 and x4
      # intersection point would be (x1, y3)
      return (x1, y3)
  elif x3 == x4 and y1 == y2:
    # line a is horizontal
    # line b is vertical
    bounds = [x1, x2]
    bounds.sort()
    lower, upper = bounds
    if x3 >= lower and x3 <= upper:
      return (x3, y1)

def get_all_intersections(lines_a, lines_b):
  intersections = []
  for line_a in lines_a:
    for line_b in lines_b:
      pt_a_1, pt_a_2 = line_a
      pt_b_1, pt_b_2 = line_b
      intersection = get_intersection_point(pt_a_1, pt_a_2, pt_b_1, pt_b_2)
      if intersection:
        intersections.append(intersection)
  return intersections


def get_lines(coords):
  lines = []
  current = [coords[0]]
  for point in coords[1:]:
    current.append(point)
    if len(current) == 2:
      lines.append(current)
      current = [point]
  return lines


if __name__ == '__main__':
  # open a file
  # f = open('manhattan.txt')
  # directions = f.read().split(',')

  # first_wire = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']

  # second_wire = ['U62','R66','U55','R34','D71','R55','D58','R83']

  first_wire = ['R8','U5','L5','D3']
  second_wire = ['U7','R6','D4','L4']
  # print(get_coordinates(first_wire))
  # print(get_coordinates(second_wire))
  first_wire_coordinates = get_coordinates(first_wire)
  second_wire_coordinates = get_coordinates(second_wire)

  first_lines = get_lines(first_wire_coordinates)
  first_lines.pop(0)
  second_lines = get_lines(second_wire_coordinates)
  second_lines.pop(0)
  print(first_lines)
  print(second_lines)

  print(get_all_intersections(first_lines, second_lines))
  
  # end_first = reduce(manhattan_coordinates, first_wire, (0, 0))
  # end_second =reduce(manhattan_coordinates, second_wire, (0, 0))
  # print(en)


  # f.close()
