class Solution:
    def safeIndexIsland(self, grid: List[List[str]], row_idx: int, col_idx: int) -> str:
        """
        Safely index island without going out of bounds.
        """
        # if out of bounds, current cell is water
        if row_idx < 0 or row_idx >= len(grid) or col_idx < 0 or col_idx >= len(grid[0]):
            return '0'

        return grid[row_idx][col_idx]

    def findOnes(self, grid: List[List[str]], ones: set[tuple[int, int]], visited: set[tuple[int, int]], row_idx: int, col_idx: int):
        """
        Recursively find ones starting from given cell indices
        and remove those indices from the set of ones.
        """
        # skip if already visited
        if (row_idx, col_idx) in visited:
            return

        # add current cell to visited
        visited.add((row_idx, col_idx))

        # if water, skip cell
        if self.safeIndexIsland(grid, row_idx, col_idx) == '0':
            return

        # if land, remove cell from set of ones if it exists
        ones.discard((row_idx, col_idx))

        # recursively find ones for cell above current cell
        self.findOnes(grid, ones, visited, row_idx - 1, col_idx)
        # recursively find ones for cell below current cell
        self.findOnes(grid, ones, visited, row_idx + 1, col_idx)
        # recursively find ones for cell left of current cell
        self.findOnes(grid, ones, visited, row_idx, col_idx - 1)
        # recursively find ones for cell right of current cell
        self.findOnes(grid, ones, visited, row_idx, col_idx + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # maintain set of land cells
        ones = set()

        # iterate over grid and find ones
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if self.safeIndexIsland(grid, row_idx, col_idx) == '1':
                    ones.add((row_idx, col_idx))

        num_islands = 0
        # iterate until we run out of land
        while len(ones) > 0:
            # recursively find ones starting from current index
            self.findOnes(grid, ones, set(), *next(iter(ones)))
            # increment island count
            num_islands += 1

        return num_islands
