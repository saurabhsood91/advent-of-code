import sys
from functools import reduce
from math import inf

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


def get_manhattan_distance(point):
    x, y = point
    return abs(x) + abs(y)


def get_closest_point_distance(points):
    min_distance = get_manhattan_distance(points[0])
    closest_point = points[0]
    for point in points:
        distance = get_manhattan_distance(point)
        if distance < min_distance:
            closest_point = point
            min_distance = distance
    return min_distance, point


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
            # we also need to check the y bounds
        x_bounds = [x3, x4]
        x_bounds.sort()
        lower_x, upper_x = x_bounds

        y_bounds = [y1, y2]
        y_bounds.sort()
        lower_y, upper_y = y_bounds

        # y3 should lie between lower_y and upper_y

        if x1 >= lower_x and x1 <= upper_x and y3 >= lower_y and y3 <= upper_y:
            # we have an intersection
            # x has to lie between x3 and x4
            # intersection point would be (x1, y3)
            return (x1, y3)
    elif x3 == x4 and y1 == y2:
        # line a is horizontal
        # line b is vertical
        x_bounds = [x1, x2]
        x_bounds.sort()
        lower_x, upper_x = x_bounds

        y_bounds = [y3, y4]
        y_bounds.sort()
        lower_y, upper_y = y_bounds

        if x3 >= lower_x and x3 <= upper_x and y1 >= lower_y and y1 <= upper_y:
            return (x3, y1)


def get_all_intersections(lines_a, lines_b):
    intersections = []
    for line_a in lines_a:
        for line_b in lines_b:
            pt_a_1, pt_a_2 = line_a
            pt_b_1, pt_b_2 = line_b
            intersection = get_intersection_point(
                pt_a_1, pt_a_2, pt_b_1, pt_b_2)
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


def closest_manhattan_distance(first_wire, second_wire):
    first_wire_coordinates = get_coordinates(first_wire)
    second_wire_coordinates = get_coordinates(second_wire)

    first_lines = get_lines(first_wire_coordinates)
    first_lines.pop(0)
    second_lines = get_lines(second_wire_coordinates)
    second_lines.pop(0)
    intersections = get_all_intersections(first_lines, second_lines)

    min_distance, closest_point = get_closest_point_distance(intersections)
    return min_distance


def distance_point_line(point, line):
    pt_a, pt_b = line
    x1, y1 = pt_a
    x2, y2 = pt_b

    x, y = point

    if x1 == x2:
        if y == y1 and y == y2:
            # vertical
            # we need to check if y is in the bounds
            y_bounds = [y1, y2]
            y_bounds.sort()
            y_lower, y_upper = y_bounds
            if y >= y_lower and y <= y_upper:
                return True, abs(y-y1)
        return False, abs(y1-y2)
    else:
        # y1 == y2
        if x == x1 and x == x2:
            # horizontal
            # we need to check if x is in the bounds
            x_bounds = [x1, x2]
            x_bounds.sort()
            x_lower, x_upper = x_bounds
            if x >= x_lower and x <= x_upper:
                return True, abs(x - x1)
        return False, abs(x1-x2)
    # point is not on line
    # this should not happen


def compute_shortest_distance_to_intersection(first_wire, second_wire):
    first_wire_coordinates = get_coordinates(first_wire)
    second_wire_coordinates = get_coordinates(second_wire)

    first_lines = get_lines(first_wire_coordinates)
    first_lines.pop(0)
    second_lines = get_lines(second_wire_coordinates)
    second_lines.pop(0)
    intersections = get_all_intersections(first_lines, second_lines)

    first_lines = get_lines(first_wire_coordinates)
    second_lines = get_lines(second_wire_coordinates)

    min_distance = inf
    print(intersections)
    for intersection in intersections:
        distance_traveled_by_wire = 0
        for line in first_lines:
            on_line, distance_traveled = distance_point_line(
                intersection, line)

            distance_traveled_by_wire += distance_traveled
            if on_line:
                break
        for line in second_lines:
            on_line, distance_traveled = distance_point_line(
                intersection, line)
            distance_traveled_by_wire += distance_traveled
            if on_line:
                break
        if distance_traveled_by_wire < min_distance:
            min_distance = distance_traveled_by_wire
    return min_distance


def run_tests():
    def test_1():
        first_wire = ['R75', 'D30', 'R83', 'U83',
                      'L12', 'D49', 'R71', 'U7', 'L72']
        second_wire = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
        assert closest_manhattan_distance(first_wire, second_wire) == 159
    test_1()

    def test_2():
        first_wire = ['R8', 'U5', 'L5', 'D3']
        second_wire = ['U7', 'R6', 'D4', 'L4']
        assert closest_manhattan_distance(first_wire, second_wire) == 6
    test_1()

    def test_3():
        first_wire = ['R98', 'U47', 'R26', 'D63', 'R33',
                      'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
        second_wire = ['U98', 'R91', 'D20', 'R16',
                       'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
        assert closest_manhattan_distance(first_wire, second_wire) == 135


def run_tests_part_b():
    # def test_1():
    #     first_wire = ['R75', 'D30', 'R83', 'U83',
    #                   'L12', 'D49', 'R71', 'U7', 'L72']
    #     second_wire = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    #     print(compute_shortest_distance_to_intersection(first_wire, second_wire))
    # test_1()

    def test_2():
        first_wire = ['R8', 'U5', 'L5', 'D3']
        second_wire = ['U7', 'R6', 'D4', 'L4']
        print(compute_shortest_distance_to_intersection(first_wire, second_wire))
    test_2()

    # def test_3():
    #     first_wire = ['R98', 'U47', 'R26', 'D63', 'R33',
    #                   'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    #     second_wire = ['U98', 'R91', 'D20', 'R16',
    #                    'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    #     assert closest_manhattan_distance(first_wire, second_wire) == 135
    # test_3()


if __name__ == '__main__':
    # let's make sure our algorithm still works
    # run_tests()

    run_tests_part_b()

    # f = open('manhattan.txt')
    # first_wire_coordinates, second_wire_coordinates = f.read().splitlines()
    # first_wire = first_wire_coordinates.split(',')
    # second_wire = second_wire_coordinates.split(',')

    # print(closest_manhattan_distance(first_wire, second_wire))

    # f.close()
