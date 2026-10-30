class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        pivot = -1

      # step 1 is finding pivot
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

      # When we find pivot, we swap its place
        if pivot != -1:
            for j in range(n-1, pivot, -1):
                if nums[j] > nums[pivot]:
                    nums[j], nums[pivot] = nums[pivot], nums[j]
                    break

      # at last we reverse the nums after the pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1
