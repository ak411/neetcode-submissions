class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_lookup = {value: index for index, value in enumerate(nums)}
        # {1:0,3:1,4:2,2:3}
        print(index_lookup)
        for ind,val in enumerate(nums):
            diff = target - val
            print(diff)
            # check if diff is in nums
            index_found = index_lookup.get(diff,-1)
            if index_found > 0 and index_found != ind:
                return [ind,index_lookup.get(diff)]