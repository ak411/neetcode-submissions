class Solution:
    def has_duplicates(self,my_list):
        my_list = [x for x in my_list if x != "."]
        return len(my_list) != len(set(my_list))

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row_idx in range(len(board)):
            if self.has_duplicates(board[row_idx]):
                return False
        

        for col_idx in range(len(board[0])):
            column = [row[col_idx] for row in board]
            if self.has_duplicates(column):
                return False
        
        
        for row_idx in range(0,len(board),3):
            for col_idx in range(0,len(board),3):
                square = []
                for i in range(0,3):
                    for j in range(0,3):
                        square.append(board[row_idx+i][col_idx+j])
           
                if self.has_duplicates(square):
                    return False
                

            #     print(board[row_idx][col_idx])
        return True
        
    