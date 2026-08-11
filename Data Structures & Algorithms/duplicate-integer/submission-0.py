class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        di = {}
        for i in range(len(nums)):
            if nums[i] in di:
                return True
            else:
                di[nums[i]] = i
        
        return False