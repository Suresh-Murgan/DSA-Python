# 88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m + n - 1  # Index to place next element in nums1
        m -= 1  # Last index of valid elements in nums1
        n -= 1  # Last index of nums2

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
