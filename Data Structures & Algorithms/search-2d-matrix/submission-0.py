class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1

            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break

        if not (top <= bottom):
            return False
        mid_row = (top + bottom) // 2
        l, r = 0, cols - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True
        return False

        