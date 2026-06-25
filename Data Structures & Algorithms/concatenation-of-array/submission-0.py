class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_2=[]
        nums_2[1:len(nums)] = nums
        nums_2[len(nums):]=nums
        return nums_2
        