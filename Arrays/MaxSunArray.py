#53. Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        maxSum = curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum
