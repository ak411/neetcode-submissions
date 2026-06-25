class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        for pointer_1 in range(0,len(s)-1):
            pointer_2 = len(s)-1-pointer_1 
            if s[pointer_1] != s[pointer_2]:
                print(pointer_1)
                return False
        return True
        