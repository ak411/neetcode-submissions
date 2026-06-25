class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = sorted(set(nums))
        print(len(set_nums))
        nums[:len(set_nums)]= set_nums
        return len(set_nums)