class Solution:
    def search_word(
        self,
        board: List[List[str]],
        word: str,
        visited: set[tuple[int, int]],
        word_idx: int,
        cell: tuple[int, int],
    ) -> bool:
        """
        Recursively search for remaining word from given cell.
        """
        # skip cell if visited
        if cell in visited:
            return False

        row_idx, col_idx = cell

        # skip if cell is out of bounds
        if row_idx < 0 or row_idx >= len(board) or col_idx < 0 or col_idx >= len(board[0]):
            return False

        # skip if cell does not have our desired letter
        if board[row_idx][col_idx] != word[word_idx]:
            return False

        # if we are at the last index, we have found our word
        if word_idx == len(word) - 1:
            return True

        foundWord = False
        # add cell to set of visited cells
        visited.add(cell)

        for next_cell in [
            (row_idx - 1, col_idx), # top cell
            (row_idx + 1, col_idx), # bottom cell
            (row_idx, col_idx - 1), # left cell
            (row_idx, col_idx + 1), # right cell
        ]:
            foundWord = self.search_word(board, word, visited, word_idx + 1, next_cell)
            if foundWord:
                break

        # remove cell from set of visited cells
        visited.remove(cell)

        return foundWord

    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate over each cell in board and attempt to search for the word from there
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                if self.search_word(board, word, set(), 0, (row_idx, col_idx)):
                    return True

        return False
