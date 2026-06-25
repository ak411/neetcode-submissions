class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = arr
        for i in range(len(arr)-1):
            max_array = arr[i+1:]
            new_arr[i] = max(max_array)
        new_arr[len(arr)-1] = -1
        return new_arr