class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        BRUTE FORCE: O(m+n/2)
        """
        
        total = len(nums1) + len(nums2)
        target = total // 2 + 1

        n1, n2 = 0, 0
        prev, curr = 0, 0
        steps = 0
        while True:
            if steps == target:
                if total % 2 == 1:
                    return curr
                else:
                    return (prev + curr) / 2
            
            prev = curr
            
            if n1 < len(nums1) and n2 < len(nums2):
                if nums1[n1] < nums2[n2]:
                    curr = nums1[n1]
                    n1 += 1
                else:
                    curr = nums2[n2]
                    n2 += 1

            elif n1 == len(nums1) and n2 < len(nums2):
                curr = nums2[n2]
                n2 += 1

            elif n1 < len(nums1) and n2 == len(nums2):
                curr = nums1[n1]
                n1 += 1

            steps += 1


