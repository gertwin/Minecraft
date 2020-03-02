

class Inventory:
    """
    Inventory class
    """

    def __init__(self):
        self.GRASS = self.tex_coords((1, 0), (0, 1), (0, 0))
        self.SAND = self.tex_coords((1, 1), (1, 1), (1, 1))
        self.BRICK = self.tex_coords((2, 0), (2, 0), (2, 0))
        self.STONE = self.tex_coords((2, 1), (2, 1), (2, 1))

    def tex_coord(self, x, y, n=4):
        """
        Return the bounding vertices of the texture square.

        """
        m = 1.0 / n
        dx = x * m
        dy = y * m
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

    def tex_coords(self, top, bottom, side):
        """
        Return a list of the texture squares for the top, bottom and side.

        """
        top = self.tex_coord(*top)
        bottom = self.tex_coord(*bottom)
        side = self.tex_coord(*side)
        result = []
        result.extend(top)
        result.extend(bottom)
        result.extend(side * 4)
        return result


Inventory = Inventory()
