class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        i = 0
        j = 0
        while i < m:
            while j < n and nums2[j] < nums1[i]:
                arr.append(nums2[j])
                j += 1
            arr.append(nums1[i])
            i += 1
        while j < n:
            arr.append(nums2[j])
            j += 1
        for i in range(m+n):
            nums1[i] = arr[i]
