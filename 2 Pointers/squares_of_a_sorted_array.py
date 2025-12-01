# Link to problem: https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
      '''
      Approach:
      a. Use two pointers, start and end.
      b. Create a new array to store result.
      c. Compare the absolute value of the two ends of the array, append the square of the greatest number to the new array.
      d. Return the new array.
      '''
        start = 0
        end = len(nums) - 1
        res = [0] * len(nums)
        idx = end

        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                res[idx] = nums[start] * nums[start]
                start += 1
            else:
                res[idx] = nums[end] * nums[end]
                end -= 1
            idx -= 1
        return res
