class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        for i in s:
            if i in s_set:
                s_set[i] = s_set[i]+1;
            else:
                s_set[i] = 1
        for i in t:
            if i in t_set:
                t_set[i] = t_set[i]+1
            else:
                t_set[i] = 1
        
        if s_set == t_set:
            print(s_set)
            print(t_set)
            return True
        return False
            
            