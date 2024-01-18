class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i = n + m - 1 # nums1 index
        j = n - 1 #nums2 index

        while j >= 0:
            nums1[i] = nums2[j]
            i -= 1
            j -= 1

        nums1.sort()

# lessons learned: replace values if values are already sorted instead of removing/appending