import itertools

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        merged = list(itertools.chain.from_iterable(grid)) # merging our matrix in one list
        n = len(merged)
        missing = list(set(range(1, n + 1)) - set(merged)) # finding missing number by subtracting the real list num with expected list

        seen = set() # empty right now
        duplicate = -1

        for i in merged:
            if i in seen: 
                duplicate = i # getting our duplicate num
            else:
                seen.add(i)

        return [duplicate, missing[0]]
