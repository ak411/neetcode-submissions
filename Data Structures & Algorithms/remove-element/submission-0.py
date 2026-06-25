class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        set_nums = []
        for i in nums:
            if i != val:
                set_nums.append(i)
        nums[:len(set_nums)] = set_nums

        return len(set_nums)
        