class Solution:
    def getDirectionallyAdjacentCells(
        self,
        i: int,
        j: int,
        n_rows: int,
        n_cols: int,
    ) -> list[tuple[int, int]]:
        """
        Given the cell indices and the total number of rows and columns,
        get the indices of the directionally adjacent cells.
        """
        adjacent = []

        if i > 0:
            adjacent.append((i - 1, j))

        if i < n_rows - 1:
            adjacent.append((i + 1, j))

        if j > 0:
            adjacent.append((i, j - 1))

        if j < n_cols - 1:
            adjacent.append((i, j + 1))

        return adjacent

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        # maintain a grid of the current number of iteration
        # this is used to indicate whether a cell has already been processed
        iterations = [[0] * n_cols for _ in range(n_rows)]
        # current iteration number
        iteration = 0

        while True:
            iteration += 1
            # track whether at least one orange has been made rotten
            changed = False
            # track total number of fresh oranges
            n_fresh = 0

            for i in range(n_rows):
                for j in range(n_cols):
                    # if cell already processed, skip it
                    if iterations[i][j] != iteration - 1:
                        continue

                    iterations[i][j]  = iteration
                    cell_value = grid[i][j]

                    # if cell empty, skip it
                    if cell_value == 0:
                        continue

                    # if cell has fresh orange, increment fresh counter
                    if cell_value == 1:
                        n_fresh += 1
                        continue

                    # if cell rotten, rot directionally adjacent cells
                    if cell_value == 2:
                        for adj_i, adj_j in self.getDirectionallyAdjacentCells(
                            i,
                            j,
                            n_rows,
                            n_cols,
                        ):
                            # if adjacent cell not fresh, no need to rot it
                            if grid[adj_i][adj_j] != 1:
                                continue

                            # if adjacent cell has already been processed
                            # then it contributed to the total fresh count
                            # since we're rotting it now, we decrement fresh count
                            if iterations[adj_i][adj_j] == iteration:
                                n_fresh -= 1

                            # make cell rot
                            grid[adj_i][adj_j] = 2
                            # mark adjacent cell as processed
                            iterations[adj_i][adj_j] = iteration
                            # note at least one cell has been marked rotten
                            changed = True

            if not changed:
                if n_fresh == 0:
                    # if nothing changed in this iteration
                    # and no fresh oranges remain, then we were done
                    # last iteration
                    return iteration - 1

                # if nothing changed in this iteration
                # and there are still fresh oranges
                # then we will never rot all oranges
                return -1

            # if there are no fresh oranges
            # then we are done in this iteration
            if n_fresh == 0:
                return iteration
