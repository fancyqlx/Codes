class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m,n,nums1,nums2 = n,m,nums2,nums1
        if n==0:
            return None
        lower = 0
        upper = m
        return self.binary(nums1,nums2,m,n,lower,upper)

    def binary(self,nums1, nums2, m, n, lower, upper):
        i = (lower + upper)/2
        j = (m+n+1)/2 - i
        if i>0 and j<n and nums1[i-1] > nums2[j]:
            return self.binary(nums1,nums2,m,n,lower,i)
        elif j>0 and i<m and nums2[j-1] > nums1[i]:
            return self.binary(nums1,nums2,m,n,i+1,upper)
        else:
            a = 0
            b = 0
            if i == 0: a = nums2[j-1]
            elif j == 0: a = nums1[i-1]
            else: a = max(nums1[i-1],nums2[j-1])
            if (m+n)%2==1:
                return a
            if i == m: b = nums2[j]
            elif j == n: b = nums1[i]
            else: b = min(nums1[i],nums2[j])
            return (a+b)/2.0


