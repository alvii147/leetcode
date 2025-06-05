class Solution:
    def spiralOrderBoundary(self, matrix: List[List[int]], i: int, j: int, n: int, m: int) -> List[int]:
        '''
        Given starting positions i, j, iterate n x m matrix in spiral order.
        '''
        order = []

        # walk from left to right
        walked = False
        for jj in range(j, j + n):
            walked = True
            print(matrix[i][jj])
            order.append(matrix[i][jj])

        if not walked:
            return order

        # walk from top to bottom
        walked = False
        for ii in range(i + 1, i + m):
            walked = True
            print(matrix[ii][j + n - 1])
            order.append(matrix[ii][j + n - 1])

        if not walked:
            return order

        # walk from right to left
        walked = False
        for jj in range(j + n - 2, j - 1, -1):
            walked = True
            print(matrix[i + m - 1][jj])
            order.append(matrix[i + m - 1][jj])

        if not walked:
            return order

        # walk from bottom to top
        walked = False
        for ii in range(i + m - 2, i, -1):
            walked = True
            print(matrix[ii][j])
            order.append(matrix[ii][j])

        if not walked:
            return order

        return order

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        i = 0
        j = 0
        n = len(matrix[0])
        m = len(matrix)

        # walk each layer of matrix at a time
        # until the inner matrix has no more elements
        while n > 0 and m > 0:
            order += self.spiralOrderBoundary(matrix, i, j, n, m)
            i += 1
            j += 1
            n -= 2
            m -= 2

        return order
