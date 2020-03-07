class Circle:

    def __init__(self, radius):
        """
        Constructor to initialise variables

        :param radius:
        """

        self.radius = radius
        self.pi = 3.14

    def area(self):
        """
        Function to calculate area of a circle.

        """
        area = (self.radius ** 2) * self.pi
        return area

    def perimeter(self):
        """
        Function to calculate perimeter of a circle --> DOCSTRINGS
        """
        perimeter = self.radius * 2 * self.pi
        return perimeter

    @staticmethod
    def display(number):
        """
        Function to display calculated area of a circle.

        :param number:
        :return: None
        """
        print("the area of circle is {0:.3f}".format(number))

    @staticmethod
    def display1(number):
        print("the perimeter of circle is {0:.3f}".format(number))


def main():
    radius = int(input("enter radius:"))
    circleObj = Circle(radius)
    area = circleObj.area()
    Circle.display(area)
    perimeter = circleObj.perimeter()
    Circle.display1(perimeter)


if __name__ == "__main__":
    main()