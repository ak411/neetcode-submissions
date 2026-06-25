class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        max_val = -1
        for i in range (n-1,-1,-1):
            ans[i] = max_val
            max_val = max(max_val,arr[i])
        return ans
            
            