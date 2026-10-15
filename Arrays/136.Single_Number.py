"""
Problem: 136. Single Number
Link: https://leetcode.com/problems/single-number/
Difficulty: Easy
Pattern: Bit Manipulation (XOR) / Hash Map
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique = {}

        for num in nums:
            if num not in unique:
                unique[num]= 1
            else:
                unique[num] += 1

        return min(unique, key=unique.get)
