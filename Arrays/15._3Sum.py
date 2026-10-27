class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        triplets = [] # our empty array

        if len(nums) < 3: # if there are not even 3 nums then no point of going further
            return triplets

        nums.sort() # we sort them to use two pointer technique later

        for i in range(len(nums) -2): # leaving a spaces for left and right
            if i > 0 and nums[i] == nums[i-1]: # to skip duplicates
                continue

            left = i + 1 # ahead of i
            right = len(nums) -1 # at the last num of array

            while left < right: # until left is smaller than right
                total = nums[i] + nums[left] + nums[right] # check the total

                if total == 0: # if we reach our target append the nums to our empty array
                    triplets.append([nums[i], nums[left], nums[right]])

                    left +=1 # put them ahead
                    right -= 1

                    while left < right and nums[left] == nums[left -1]: # of the next number is same as before go one num ahead again
                        left +=1

                    while right > left and nums[right] == nums[right + 1]: # if the next num is same go back a step
                        right -=1

                elif total > 0:
                    right -=1

                elif total < 0:
                    left +=1 

        return triplets
