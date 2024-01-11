#!/usr/bin/python3
"""the module contains the class MyInt"""


class MyInt(int):
    """My int class"""

    def __init__(self, nt):
        """init"""

        self.nt = nt
        super().__init__()

    def __eq__(self, other):
        """str"""

        if self.nt == other.nt:
            return False
        return True

    def __ne__(self, other):
        """not equal"""

        if self.nt != other.nt:
            return True
        return False
