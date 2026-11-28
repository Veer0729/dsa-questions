class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        for i in range(len(digits) -1, -1, -1):
            # first [-1]: start from the back of the array
            # middle [-1]: we have to cover the entire loop, even the 0th index so -1
            # last [-1]: loop over every element

            if digits[i] < 9: # if any elem is less than 9
                digits[i] += 1 # we only have to increment it by 1 and return
                return digits
            else:
                digits[i] = 0 # but if it's 9 then wewill turn it into 0
        
        return [1] + digits # if we got to this retun it means all the elems were 9 so at last we put a 1 as the 1st elem and return
