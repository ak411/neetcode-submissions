class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if target - nums[j] == nums[i]:
        #             solution.append(i)
        #             solution.append(j) 
        #             return solution
        inter = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in inter:
                return [inter[complement],i]
            inter[nums[i]] = i
            print(inter)
        
                

            
            
        

        