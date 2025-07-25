# 278. First Bad Version (BS Method)
class Solution(object):
    def firstBadVersion(self, n):
        low=0
        high=n
        while(low<high):
            mid=(low+high)/2
            if isBadVersion(mid):
                high=mid
            else:
                low=mid+1
        return low
        