# Link to problem: https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
      '''
      Approach:
      a. Use two pointers, i and j.
      b. When i != val, rewrite element at j. Move j forward.
      c. Return j value.
      '''
        j = 0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
