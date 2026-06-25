class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        string_to_search = t
        for i in s:
            index = string_to_search.find(i)
            print(string_to_search)
            print(index)
            if index == -1:
                return False
            string_to_search = string_to_search[index+1:]
        return True
        