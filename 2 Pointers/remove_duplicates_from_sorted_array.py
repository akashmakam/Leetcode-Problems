Link the problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
      '''
      Approach:
      a. Use two pointers, i and j.
      b. When the element at i is not equal to the element at j, increment j and rewrite the element at j.
      c. Return the value of j, it contains the number of elements that are not duplicates.
      '''
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
