#!/usr/bin/python3
"""module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        self.validate_h_w("width", width)
        self.validate_h_w("height", height)
        self.validate_x_y("x", x)
        self.validate_x_y("y", y)

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        self.validate_h_w("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        self.validate_h_w("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        self.validate_x_y("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        self.validate_x_y("y", value)
        self.__y = value

    def validate_h_w(self, name, value):
        """validates the values of height and width"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_x_y(self, name, value):
        """validate the values of x and y"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """returns the area of rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """string reprisintation of the object"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def display(self):
        """display the rectangle using #"""

        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            print(" " * self.__x, end="")
            for w in range(self.__width):
                print('#', end="")
            print("")

    def update(self, *args, **kwargs):
        """updates the attributes of an objest"""

        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """to dictionary"""

        return {'x': self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}
