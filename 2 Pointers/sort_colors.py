# Link to problem: https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
      '''
      Approach:
      a. Maintain 3 pointers, low, mod and high.
      b. If element at mid is 0, swap with start and move low and mid forward.
      c. If element at mid is 1, move mid forward.
      d. Else, swap elements at mid and high.
      '''
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
