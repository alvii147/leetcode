class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # initialize 2d list matrix
        matrix = [[0] * n for _ in range(n)]
        # i and j are indices of the corner position we start it
        i = 0
        j = 0
        # value to insert into the matrix
        value = 1

        while n > 0:
            # walk from left to right
            for jj in range(j, j + n):
                matrix[i][jj] = value
                value += 1

            # walk from top to bottom
            for ii in range(i + 1, i + n):
                matrix[ii][j + n - 1] = value
                value += 1

            # walk from right to left
            for jj in range(j + n - 2, j - 1, -1):
                matrix[i + n - 1][jj] = value
                value += 1

            # walk from bottom to top
            for ii in range(i + n - 2, i, -1):
                matrix[ii][j] = value
                value += 1

            # advance the starting corner one step diagonally towards bottom right
            i += 1
            j += 1
            # matrix is two sizes smaller now, since we're walked along its border
            n -= 2

        return matrix
