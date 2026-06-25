class Solution:
    def isValid(self, s: str) -> bool:
        square_bracket = deque()
        
        for val in s: 
            print(square_bracket)
            if val == '[' :
                square_bracket.append("[")
            if val == ']':
                if len(square_bracket)==0 or not square_bracket[-1]=="[":
                    return False
                else:
                    square_bracket.pop()
            if val == '(':
                square_bracket.append("(")
            if val == ')':
                if len(square_bracket)==0 or not square_bracket[-1]=="(":
                    return False
                if len(square_bracket) == 0:
                    return False
                else:
                    square_bracket.pop()
            if val == '{':
                square_bracket.append("{")
            if val == '}':
                if len(square_bracket)==0 or not square_bracket[-1]=="{":
                    return False
                if len(square_bracket)==0:
                    return False
                else:
                    square_bracket.pop()
            
        if len(square_bracket)==0:
            return True
        return False

                

        