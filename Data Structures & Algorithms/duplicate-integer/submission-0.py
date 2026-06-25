class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        new_set = set(nums)
        if len(nums)!= len(new_set):
            return True
        return False
        
         