"""
Problem: 3. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Pattern: Sliding Window + Hash Set

Intuition:
Maintain a dynamic window using two pointers (left and right). Use a hash set to keep track
of characters inside the current window. If a duplicate character appears, shrink the window
from the left until all characters in the window are unique again.

Time Complexity: O(N) - Each character is processed at most twice (once by right, once by left).
Space Complexity: O(K) - K is the number of unique characters in the string.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set() # our empty set
        left = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in char_set: # until r value in set
                char_set.remove(s[left]) # remove it from set
                left += 1 # increase left index to right

            char_set.add(s[r]) # if r not same in set add it to the set
            max_length = max(max_length, len(char_set)) # keep record of which is max, initially it will be char_set, then as numbers get removed from the set the max will be max_length

        return max_length
