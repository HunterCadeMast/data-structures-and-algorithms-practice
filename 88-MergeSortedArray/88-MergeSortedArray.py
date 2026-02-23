# Last updated: 2/23/2026, 5:58:07 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        nums1_length = m - 1
7        nums2_length = n - 1
8        right = m + n - 1
9        while nums2_length >= 0:
10            if nums1_length >= 0 and nums1[nums1_length] > nums2[nums2_length]:
11                nums1[right] = nums1[nums1_length]
12                nums1_length -= 1
13            else:
14                nums1[right] = nums2[nums2_length]
15                nums2_length -= 1
16            right -= 1