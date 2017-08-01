class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        T = {}
        for i in xrange(len(nums1)):
            if not T.has_key(nums1[i]):
                T[nums1[i]] = 1
            else:
                T[nums1[i]] += 1
        r = []
        for i in xrange(len(nums2)):
            if T.has_key(nums2[i]) and T[nums2[i]] > 0:
                r.append(nums2[i])
                T[nums2[i]] -= 1
        return r
