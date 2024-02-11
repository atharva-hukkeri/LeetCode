class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, low, mid)
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            else:
                self.swap(nums, high, mid)
                high -= 1
                
    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

        