"""
Problem: 88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Pattern: Array Slicing & In-Place Modification

Time Complexity: O((m + n) log(m + n)) - Due to the built-in sort function.
Space Complexity: O(1) extra space - Modifies nums1 in-place.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]= nums1[:m] # removes extra nums other than the limit of m
        nums1.extend(nums2) # extends for nums 2-- kinda add them in nums1
        nums1.sort() # sort everything
        print(nums1)
