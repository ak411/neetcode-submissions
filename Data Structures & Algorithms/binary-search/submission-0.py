import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while (left<=right):
            mid = math.floor((left + right) / 2)
            print(nums[mid])
            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
                print(left)
                print(right)
            else:
                return mid
            
        return -1
        