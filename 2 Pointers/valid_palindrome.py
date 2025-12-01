# Link to problem: https://leetcode.com/problems/valid-palindrome

import re

class Solution(object):
    def isPalindrome(self, s):
        '''
        Approach:
        a. Remove non-alphanumeric characters from given string.
          i. Remove using re library.
          ii. Remove using isalnum() method.
        b. Convert string to lowercase.
        c. Check if the string is a palindrome or not.
          i. Compare reversed string with original string (s == s[::-1] method)
          ii. Use two pointers, start and end.
        '''
        # a. Remove non-alphanumeric characters from given string. 
        # Using re library
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        # or
        # Using isalnum() method
        # s = "".join(c for c in s if c.isalnum())

        # b. Convert string to lowercase.
        s = s.lower()

        # c. Check if the string is a palindrome or not.
        return s == s[::-1]
        # or
        # start = 0
        # end = len(s) - 1
        # while start <= end:
            # if s[start] != s[end]:
                # return False
            # start += 1
            # end -= 1
        # return True   
        
        
