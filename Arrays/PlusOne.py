# 66. Plus One

class Solution(object):
    def plusOne(self, digits):
       n=len(digits)
       while(n>0):
          if digits[n-1]<9:
            digits[n-1]+=1
            return digits
          digits[n-1]=0
          n-=1
       return [1]+[0]*len(digits)
        