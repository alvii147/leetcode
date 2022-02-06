class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # lengths of nums1 & nums2
        n1 = len(nums1)
        n2 = len(nums2)
        # combined lengths of nums1 & nums2
        n = n1 + n2

        # median list
        median = []
        # median indices list
        median_idx = [n // 2]

        # if combined length is even, add n / 2 - 1 to median index
        if n % 2 == 0:
            median_idx = [(n // 2) - 1] + median_idx

        # nums1 & nums2 iterators
        i = 0
        j = 0
        while i < n1 or j < n2:
            # if nums2 length is covered, increment nums1 index
            if j >= n2:
                num = nums1[i]
                i += 1
            # if nums1 length is covered, increment nums2 index
            elif i >= n1:
                num = nums2[j]
                j += 1
            # if nums1 first element is less than nums2 first element, increment nums1 index
            elif nums1[i] < nums2[j]:
                num = nums1[i]
                i += 1
            # else increment nums2 index
            else:
                num = nums2[j]
                j += 1

            # if current combined index is of median index, append value to median list
            if i + j - 1 in median_idx:
                median.append(num)
                median_idx.remove(i + j - 1)

            # if no more median indices are left, break
            if len(median_idx) == 0:
                break

        # set median to average of median list
        median = sum(median)/len(median)

        return median