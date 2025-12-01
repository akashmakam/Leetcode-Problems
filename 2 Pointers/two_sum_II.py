# Link to problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
      '''
      Approach:
      a. Use two pointers, start and end.
      b. Compute the sum of elements at start and end.
      c. If sum = target, return the indices.
      d. Check if sum is greater or smaller than target.
        i. If greater, we have more, we need less. Decrement end.
        ii. If smaller, we need more, we have less. Increment start.
      '''
        start = 0
        end = len(numbers) - 1
        while start <= end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start+1, end+1]
            if s < target:
                start += 1
            elif s > target:
                end -= 1
        return []
