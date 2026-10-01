"""
Problem: 53. Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium
Pattern: Kadane's Algorithm

Intuition:
At each index, decide whether to add the current number to the existing subarray sum
or start a brand-new subarray starting at the current number.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
