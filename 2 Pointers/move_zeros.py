# Link to problem: https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
      '''
      Approach:
      a. Use two pointers, i and j.
      b. When the element at i is non-zero, swap with element at j.
      c. Return the modified array.
      '''
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
