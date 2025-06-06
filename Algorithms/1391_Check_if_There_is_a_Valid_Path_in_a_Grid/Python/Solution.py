# dictionary of streets and sets of directions they can go to
STREET_DIRECTIONS = {
    1: {'L', 'R'},
    2: {'U', 'D'},
    3: {'D', 'L'},
    4: {'D', 'R'},
    5: {'U', 'L'},
    6: {'U', 'R'},
}

# dictionary of directions and their configurations
# configuration includes a function to determine the next cell coordinates
# and the opposite direction
DIRECTIONS_CONFIG = {
    'U': {
        'NEXT': lambda i, j: (i - 1, j),
        'OPPOSITE': 'D',
    },
    'D': {
        'NEXT': lambda i, j: (i + 1, j),
        'OPPOSITE': 'U',
    },
    'L': {
        'NEXT': lambda i, j: (i, j - 1),
        'OPPOSITE': 'R',
    },
    'R': {
        'NEXT': lambda i, j: (i, j + 1),
        'OPPOSITE': 'L',
    }
}

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # set of cells already visited
        visited = set()
        # queue of cells to visit
        queue = [(0, 0)]
        # number of rows and columns in the grid
        gridRows, gridCols = len(grid), len(grid[0])
        # target cell, i.e. bottom right corner
        target = (len(grid) - 1, len(grid[0]) - 1)

        while len(queue) > 0:
            i, j = queue.pop(0)

            # if at target, there does exist a valid path
            if (i, j) == target:
                return True

            for direction in STREET_DIRECTIONS[grid[i][j]]:
                direction_config = DIRECTIONS_CONFIG[direction]
                nextI, nextJ = direction_config['NEXT'](i, j)

                # avoid going out of bounds
                if (nextI < 0 or nextI >= gridRows or nextJ < 0 or nextJ >= gridCols):
                    continue

                # avoid revisiting visited cells
                if (nextI, nextJ) in visited:
                    continue

                # avoid visiting cells that don't connect properly
                if direction_config['OPPOSITE'] not in STREET_DIRECTIONS[grid[nextI][nextJ]]:
                    continue

                # mark next cell as visited
                visited.add((nextI, nextJ))
                # add next cell in the queue to be visited
                queue.append((nextI, nextJ))

        # if we exit loop, we have exhausted all paths, meaning no valid path exists
        return False
