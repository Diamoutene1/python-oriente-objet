import math

class Range:
    def __init__(self, value_1=float, value_2=float):
        self.__lower = min(value_1, value_2)
        self.__upper = max(value_1, value_2)

    def get_lower(self):
        return self.__lower

    def get_upper(self):
        return self.__upper

    def to_str(self):
        return f"[{self.__lower}, {self.__upper}]"

    def get_middle(self):
        return (self.__lower + self.__upper) / 2

    def get_size(self):
        return self.__upper - self.__lower

    def get_union(self, Other):
        return Range(min(self.__lower, Other.get_lower()), max(self.__upper, Other.get_upper()))

    def has_intersection(self, Other):
        return (self.__upper >= Other.get_upper() and self.__lower >= Other.get_lower()) or \
               (self.__upper <= Other.get_upper() and self.__lower <= Other.get_lower())

class Point:
    def __init__(self, x=float, y=float):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_to_str(self):
        return f"({self.__x}, {self.__y})"  # Fix the typo here

    def translation(self, dx=float, dy=float):
        self.__x += dx
        self.__y += dy

    def get_distance(self, Other):
        return math.sqrt(abs(self.__x - Other.get_x())**2 + abs(self.__y - Other.get_y())**2)

class Segment:
    def __init__(self, p1, p2):
        self.__point1 = p1
        self.__point2 = p2

    def get_point1(self):
        return self.__point1

    def get_point2(self):
        return self.__point2

    def to_str(self):
        return f"[{self.__point1.get_to_str()}; {self.__point2.get_to_str()}]"

    def translation(self, dx=float, dy=float):
        self.__point1.translation(dx, dy)
        self.__point2.translation(dx, dy)

    def get_length(self):
        return self.__point1.get_distance(self.__point2)

    def get_projection_x(self):
        # Implement the projection_x method here
        # You might want to create a new Point object with the x-coordinate of point1 and y-coordinate of point2
        return Point(self.__point1.get_x(), self.__point2.get_y())

    def get_middle(self):
        # Implement the get_middle method here
        return Point((self.__point1.get_x() + self.__point2.get_x()) / 2, (self.__point1.get_y() + self.__point2.get_y()) / 2)

if __name__ == "__main__":
    range_test_1, range_test_2 = Range(18.2, 5), Range(10, 20)

    print(range_test_1.has_intersection(range_test_2))

    point_test_1, point_test_2 = Point(0, 2), Point(-1, 1)
    segment_test = Segment(point_test_1, point_test_2)

    print(segment_test.to_str())
    segment_test.translation(2, 1)
    print(segment_test.to_str())
    print(segment_test.get_length() == 2**0.5)
    print(segment_test.get_projection_x().get_to_str())
    print(segment_test.get_middle().get_to_str())
