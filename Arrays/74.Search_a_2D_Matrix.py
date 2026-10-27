class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        rows, col = len(matrix), len(matrix[0])
        left, right = 0, rows * col -1

        while left <= right:
            middle = (left + right) // 2
            value = matrix[middle // col][middle % col]

            if value == target:
                return True

            elif value > target:
                right = middle -1

            else:
                left = middle + 1

        return False

