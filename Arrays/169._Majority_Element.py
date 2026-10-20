class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        repeat = {} # our dictionary

        for i in nums:
            if i in repeat:
                repeat[i] = repeat[i] + 1 # if num already in repeat add 1 more 
            else:
                repeat[i] = 1 # add the new num

        return max(repeat, key=repeat.get) # get me the max repeated num
