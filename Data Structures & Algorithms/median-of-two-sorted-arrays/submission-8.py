class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Optimal: Slash into half for two list.
        If num1_L[-1] < num2_R[0] and num2_L[-1] < num1_R[0]: YOU FIND IT
        """
        #[1,2] L1|R1
        #[3] L2|R2

        #Edge Case nums1=[2], nums2=[] >> 避免 cut2 被亂塞超過數字，讓小的當 num1
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp


        total = len(nums1) + len(nums2)
        target = (total + 1) // 2   #不是 total/2 + 1 !

        n1l, n1r = 0, len(nums1) #0-2
        while True:
            cut1 = (n1l + n1r) // 2 #1
            cut2 = target - cut1 #1
            
            L1 = nums1[cut1 - 1] if cut1 >= 1 else float("-inf")
            R1 = nums1[cut1] if cut1 <= len(nums1) - 1 else float("inf")
            L2 = nums2[cut2 - 1] if cut2 >= 1 else float("-inf")
            R2 = nums2[cut2] if cut2 <= len(nums2) - 1 else float("inf")

            if L1 > R2:
                n1r = cut1 - 1
            
            elif L2 > R1:
                n1l = cut1 + 1
            
            else: # L1 < R2 and L2 < R1
                if total % 2 == 1:
                    return max(L1,L2)
                else:
                    return (max(L1,L2) + min(R1,R2)) / 2

        