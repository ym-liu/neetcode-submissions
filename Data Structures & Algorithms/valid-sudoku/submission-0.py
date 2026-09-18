class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = [set() for _ in range(9)]
        row_sets = [set() for _ in range(9)]
        square_sets = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                # only evaluate actual digits 1 - 9
                if not digit.isdigit():
                    continue

                # check if dup in col
                if digit in col_sets[j]:
                    return False
                col_sets[j].add(digit)

                # check if dup in row
                if digit in row_sets[i]:
                    return False
                row_sets[i].add(digit)

                # check if dup in square
                square_index = (i // 3) * 3 + (j // 3)
                if digit in square_sets[square_index]:
                    return False
                square_sets[square_index].add(digit)

        return True
