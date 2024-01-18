class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        m = 0
        n1 = 0
        n2 = 0
        
        while(n1 < len(nums1) or n2 < len(nums2)):
            val1 = nums1[n1] if n1 < len(nums1) else float('inf')
            val2 = nums2[n2] if n2 < len(nums2) else float('inf')
            if val1 < val2:
                merge.append(val1)
                n1 += 1  
            else:
                merge.append(val2)
                n2 += 1
            
            m += 1
        
        mid = len(merge) // 2
        o_e = len(merge) % 2
        if o_e == 1:
            return merge[mid]
        else:
            even = merge[mid] + merge[mid-1]
            median = even / 2
            return median