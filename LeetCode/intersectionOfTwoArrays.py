class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        T = {}
        for i in xrange(len(nums1)):
            if not T.has_key(nums1[i]):
                T[nums1[i]] = False
        r = []
        for i in xrange(len(nums2)):
            if T.has_key(nums2[i]):
                T[nums2[i]] = True
        for key in T:
            if T[key] == True:
                r.append(key)
        return r
