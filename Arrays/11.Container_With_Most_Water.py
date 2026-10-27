class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        res = 0 # our final result
        l, r = 0, len(height) -1

        while l < r: # until left is behind right
            area = (r-l) * min(height[l], height[r]) # formula for area of container
            res = max(res, area) # are the new value of l and r bigger? or the previous one only

            if height[l] < height[r]: # if l is small
                l += 1
            else: # if r is small
                r -=1
                
        return res
