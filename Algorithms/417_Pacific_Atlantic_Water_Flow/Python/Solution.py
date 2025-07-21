from collections import deque

class Solution:
    def pacific(self, heights: list[list[int]]) -> set[tuple[int, int]]:
        '''
        Find cells from which rain water can flow into the Pacific Ocean.
        '''
        n_rows = len(heights)
        n_cols = len(heights[0])

        # cells that have been visited
        # visited cells are ones from which rain water CAN flow into the Pacific Ocean
        visited = set()
        # queue of upcoming cells
        queue = deque()

        # insert left edges
        for r in range(n_rows):
            visited.add((r, 0))
            queue.append((r, 0))

        # insert top edges
        for c in range(n_cols):
            visited.add((0, c))
            queue.append((0, c))

        while len(queue):
            r, c = queue.popleft()

            # insert top cell if rain water can flow
            if r > 0 and (r - 1, c) not in visited and heights[r - 1][c] >= heights[r][c]:
                visited.add((r - 1, c))
                queue.append((r - 1, c))

            # insert bottom cell if rain water can flow
            if r < n_rows - 1 and (r + 1, c) not in visited and heights[r + 1][c] >= heights[r][c]:
                visited.add((r + 1, c))
                queue.append((r + 1, c))

            # insert left cell if rain water can flow
            if c > 0 and (r, c - 1) not in visited and heights[r][c - 1] >= heights[r][c]:
                visited.add((r, c - 1))
                queue.append((r, c - 1))

            # insert right cell if rain water can flow
            if c < n_cols - 1 and (r, c + 1) not in visited and heights[r][c + 1] >= heights[r][c]:
                visited.add((r, c + 1))
                queue.append((r, c + 1))

        return visited

    def atlantic(self, heights: list[list[int]]) -> set[tuple[int, int]]:
        '''
        Find cells from which rain water can flow into the Atlantic Ocean.
        '''
        n_rows = len(heights)
        n_cols = len(heights[0])

        # cells that have been visited
        # visited cells are ones from which rain water CAN flow into the Atlantic Ocean
        visited = set()
        # queue of upcoming cells
        queue = deque()

        # insert right edges
        for r in range(n_rows):
            visited.add((r, n_cols - 1))
            queue.append((r, n_cols - 1))

        # insert bottom edges
        for c in range(n_cols):
            visited.add((n_rows - 1, c))
            queue.append((n_rows - 1, c))

        while len(queue):
            r, c = queue.popleft()

            # insert top cell if rain water can flow
            if r > 0 and (r - 1, c) not in visited and heights[r - 1][c] >= heights[r][c]:
                visited.add((r - 1, c))
                queue.append((r - 1, c))

            # insert bottom cell if rain water can flow
            if r < n_rows - 1 and (r + 1, c) not in visited and heights[r + 1][c] >= heights[r][c]:
                visited.add((r + 1, c))
                queue.append((r + 1, c))

            # insert left cell if rain water can flow
            if c > 0 and (r, c - 1) not in visited and heights[r][c - 1] >= heights[r][c]:
                visited.add((r, c - 1))
                queue.append((r, c - 1))

            # insert right cell if rain water can flow
            if c < n_cols - 1 and (r, c + 1) not in visited and heights[r][c + 1] >= heights[r][c]:
                visited.add((r, c + 1))
                queue.append((r, c + 1))

        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # get set of cells from which rain water can flow into Pacific Ocean
        pacific_cells = self.pacific(heights)
        # get set of cells from which rain water can flow into Atlantic Ocean
        atlantic_cells = self.atlantic(heights)

        # return the intersection of the two
        return [list(c) for c in pacific_cells & atlantic_cells]
