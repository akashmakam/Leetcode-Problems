# Link to problem: https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        '''
        Approach:
        a. Use two pointers, start and end.
        b. Swap the values at start and end of array until start = end.
        c. Return the resultant array.
        '''
        start = 0
        end = len(s) - 1
        while start <= end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        return s
