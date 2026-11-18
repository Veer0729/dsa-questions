class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        res = [] # to save our result
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # getting every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top +=1

            # getting every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -=1

            if not (left < right and top < bottom):
                break

            # now as we are on right we go from right to left
            for i in range(right - 1, left -1, -1): # -1 is for reverse order
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # from bottom to top in left corner
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left +=1
        
        return res

