import math

# representations of the four sides of the matrix
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

class Solution:
    def get_cell_idx(
        self,
        matrix: List[List[int]],
        side: int,
        layer: int,
        offset: int,
    ) -> tuple[int, int]:
        """
        Get the cell indices at the given side, layer, and offset.

        The side is one of TOP, RIGHT, BOTTOM, LEFT.
        The layer is the layer of the matrix.
        The offset is the number of steps to walk in the given side and layer.

        For example, consider the following matrix:

        1   2   3   4   5
        6   7   8   9   10
        11  12  13  14  15
        16  17  18  19  20
        21  22  23  24  25

        In this matrix:
        * from the TOP side at layer 0 and offset 0 lies the number 1
        * from the TOP side at layer 0 and offset 1 lies the number 2
        * from the TOP side at layer 1 and offset 0 lies the number 7
        * from the TOP side at layer 2 and offset 1 lies the number 8
        * from the RIGHT side at layer 1 and offset 1 lies the number 14
        """
        n = len(matrix)

        if layer < 0 or layer > math.ceil(n / 2):
            raise ValueError('Invalid layer')

        if offset < 0 or offset >= n - (layer * 2):
            raise ValueError('Invalid offset', offset, n, layer)

        if side == TOP:
            return layer, layer + offset
        elif side == RIGHT:
            return layer + offset, n - layer - 1
        elif side == BOTTOM:
            return n - layer - 1, n - layer - 1 - offset
        elif side == LEFT:
            return n - layer - offset - 1, layer
        else:
            raise ValueError('Invalid side')

    def get_cell(
        self,
        matrix: List[List[int]],
        side: int,
        layer: int,
        offset: int,
    ) -> int:
        """
        Get the cell value at the given side, layer, and offset.
        """
        i, j = self.get_cell_idx(matrix, side, layer, offset)

        return matrix[i][j]

    def set_cell(
        self,
        matrix: List[List[int]],
        side: int,
        layer: int,
        offset: int,
        value: int,
    ) -> int:
        """
        Set the cell value at the given side, layer, and offset,
        and return the previous cell value.
        """
        i, j = self.get_cell_idx(matrix, side, layer, offset)
        old_value = matrix[i][j]
        matrix[i][j] = value

        return old_value

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # iterate over each layer in the matrix
        # note that when n is odd, we can skip the last layer, as it is just one value
        for layer in range(n // 2):
            # iterate over each offset value
            for offset in range(n - (layer * 2) - 1):
                # start with the value of the left side
                value = self.get_cell(matrix, LEFT, layer, offset)
                # iterate over each side and set the value to the previous value
                for side in range(4):
                    value = self.set_cell(matrix, side, layer, offset, value)
