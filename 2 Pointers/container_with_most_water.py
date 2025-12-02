# Link to problem: https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
      '''
      Approach:
      a. Maintain two pointers, start and end.
      b. Compute the width, which is the difference between start and end positions of height array.
      c. Calculate the area, which is the product of the difference and the minimum of element at start and end.
      d. Update the largest area if computed area is greater than current largest.
      e. Return largest area.
      '''
        start = 0
        end = len(height) - 1
        largest = 0
        while start <= end:
            diff = end - start
            area = diff * min(height[start],height[end])
            if area > largest:
                largest = area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return largest
