# pylint: disable=E201


class Location:

    FACES = [
        ( 0, 1, 0),
        ( 0,-1, 0),
        (-1, 0, 0),
        ( 1, 0, 0),
        ( 0, 0, 1),
        ( 0, 0,-1),
    ]

    # Size of sectors used to ease block loading.
    SECTOR_SIZE = 16

    def __init__(self):
        pass

    def cube_vertices(self, x, y, z, n):
        """ Return the vertices of the cube at position x, y, z with size 2*n.

        """
        return [
            x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
            x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
            x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
            x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
            x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
            x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
        ]

    def normalize(self, position):
        """ Accepts `position` of arbitrary precision and returns the block
        containing that position.

        Parameters
        ----------
        position : tuple of len 3

        Returns
        -------
        block_position : tuple of ints of len 3

        """
        x, y, z = position
        x, y, z = (int(round(x)), int(round(y)), int(round(z)))
        return x, y, z

    def sectorize(self, position):
        """ Returns a tuple representing the sector for the given `position`.

        Parameters
        ----------
        position : tuple of len 3

        Returns
        -------
        sector : tuple of len 3

        """
        x, y, z = self.normalize(position)
        x = x // self.SECTOR_SIZE
        y = y // self.SECTOR_SIZE
        z = z // self.SECTOR_SIZE
        return x, 0, z


Location = Location()
