class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = {}
        for i in nums:
            if i in number_set:
                return True
            number_set[i] = 1
        return False
            
            


        