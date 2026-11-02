class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key = lambda i: i[0]) # sort by the first nums in lists
        output = [intervals[0]] # out first elem: [1,3]

        for start, end in intervals[1:]: # starts from [2,6]
            lastoutput = output[-1][1] # takes output 3 from our output var

            if start <= lastoutput: # compares 2 from intervals[1:] and 3 from output[-1][1]
                output[-1][1] = max(lastoutput, end) # last output is max(3, 6)
            else:
                output.append([start, end]) # no overlap, so add it as a new separate interval.

        return output
