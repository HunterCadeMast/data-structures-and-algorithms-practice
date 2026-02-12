# Last updated: 2/12/2026, 3:45:34 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index in range(m, m + n):
            nums1[index] = nums2[index - m]
        nums1[:] = Solution.mergeSort(nums1)
        
    def mergeSort(array):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = array[:middle]
        right = array [middle:]
        sortedLeft = Solution.mergeSort(left)
        sortedRight = Solution.mergeSort(right)
        result = []
        i = j = 0
        while i < len(sortedLeft) and j < len(sortedRight):
            if sortedLeft[i] < sortedRight[j]:
                result.append(sortedLeft[i])
                i += 1
            else:
                result.append(sortedRight[j])
                j += 1
        result.extend(sortedLeft[i:])
        result.extend(sortedRight[j:])
        return result