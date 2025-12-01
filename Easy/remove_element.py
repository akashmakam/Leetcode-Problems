// Link to problem: https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        j = 0
        for i in range (n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
