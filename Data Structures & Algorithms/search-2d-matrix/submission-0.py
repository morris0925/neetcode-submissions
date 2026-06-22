class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mRow = ((l+r) // 2) // n
            mColumn = ((l+r) // 2) % n

            if matrix[mRow][mColumn] < target:
                l = (l+r) // 2 + 1
            elif matrix[mRow][mColumn] == target:
                return True
            else:
                r = (l+r) // 2 - 1
        return False
