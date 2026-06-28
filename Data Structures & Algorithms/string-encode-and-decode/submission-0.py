class Solution:

    def encode(self, strs: List[str]) -> str:
        sol_string = ""
        for string in strs:
            sol_string = sol_string+str(len(string))+"#"+string
        
        return sol_string
    def decode(self, s: str) -> List[str]:
        i=0
        j =0
        print(s)
        sol = []
        while i < len(s):
            hash_idx = s.find("#",i)
            print("i",i)
            print("hash_idx",hash_idx)
            print(s[i:hash_idx])
            length_s = int(s[i:hash_idx])
            plain_string = s[hash_idx+1:hash_idx+length_s+1]
            print(plain_string)
            i = hash_idx+length_s+1
            sol.append(plain_string)
        return sol
