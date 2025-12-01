# Link to problem: https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
      '''
      Approach:
      a. Use two pointers, start and end.
      b. Swap when elements at both pointers are vowels only.
      c. If elements are not vowels at pointers, move till a vowel is found.
      d. Return the updated string.
      '''
        vowels = "aeiouAEIOU"
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] not in vowels:
                start += 1
                continue
            if s[end] not in vowels:
                end -= 1
                continue
            
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        return "".join(s)
