#!/usr/bin/python3

class Solution:
   def strStr(self, source, target):
       if source is None or target is None:
           return -1
       
       for i in range(len(source) - len(target) + 1):
           for j in range(len(target)):
               if source[i + j] != target[j]:
                   break
           else:
               return i
       return -1

s = "abcdefg"
t = "bsced"

ss = Solution()
print ss.strStr(s, t)
