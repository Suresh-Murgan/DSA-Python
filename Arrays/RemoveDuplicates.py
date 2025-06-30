#Two pointer Method
class Solution(object):
    def removeDuplicates(self, nums):
        i=0 #first pointer
        for j in range(1,len(nums)): #2nd Pointer
            if nums[i]!=nums[j]: #condition to find the new unique value 
                i+=1 #incrementing i to place next unique element 
                nums[i]=nums[j]
        return i+1