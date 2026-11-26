class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1 # len of elems in arr1
        j = n - 1 # len of elems of arr2
        k = m + n - 1 

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]: # if our elem 1 of nums1 is bigger than nums2 elem
                nums1[k] = nums1[i] # the last postion gets the i
                i -= 1 # goes ahead by 1
                k -= 1
            else:
                nums1[k] = nums2[j] # if j is bigger
                j -= 1
                k -= 1

        # if any leftover elems in j
        while j >= 0:
            nums1[k] = nums2[j]
            j -=1
            k -=1
