#!/usr/bin/python3
"""Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ init"""

        self.validate_h_w("width", size)
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """size getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        self.validate_h_w("width", value)
        self.__size = value

    def __str__(self):
        """str representation of object"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """updates the attributes of obj"""

        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to dictionary"""

        return {'id': self.id, 'x': self.x, 'size': self.__size, 'y': self.y}
