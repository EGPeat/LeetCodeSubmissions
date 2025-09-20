class Solution:
    #def cankill(self, chess, x, y):

    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(index):
            nonlocal solved
            nonlocal n
            nonlocal counter
            nonlocal counter2
            
            if index == n:
                return 
            row_idx = index
            for digit in range(n):
                counter += 1
                col_idx = digit
                #print(row_idx, col_idx, n - row_idx + col_idx - 1)
                #for r in chess:
                    #print(r)
                #print("row_idx, col_idx, row_used[row_idx], col_used[col_idx], topleft_diag[row_idx + col_idx], topright_diag[n - row_idx + col_idx - 1]")
                #print(row_idx, col_idx, row_used[row_idx], col_used[col_idx], topleft_diag[row_idx + col_idx], topright_diag[n - row_idx + col_idx - 1])
                #print("####################################")
                if (not row_used[row_idx] and 
                    not col_used[col_idx] and 
                    not topleft_diag[row_idx + col_idx] and
                    not topright_diag[n - row_idx + col_idx - 1]):
                    counter2 += 1
                    #both left_diag and right diag need a -1
                    row_used[row_idx]= True
                    col_used[col_idx] = True
                    topleft_diag[row_idx + col_idx] = True
                    topright_diag[n - row_idx + col_idx - 1] = True
                    
                    chess[row_idx][col_idx] = "Q"
                    backtrack(index + 1)
                    #if solved:
                    #    return
                    if sum(row_used) == n and sum(col_used) == n:
                        temp2 = []
                        for row in chess:
                            tmp = "".join(row)
                            temp2.append(tmp)
                        if temp2 not in self.temp_output:
                            self.temp_output.append(temp2)
                        #print("spot2", self.temp_output)

                    chess[row_idx][col_idx] = "."
                    row_used[row_idx]= False
                    col_used[col_idx] = False
                    topleft_diag[row_idx + col_idx] = False
                    topright_diag[n - row_idx + col_idx - 1] = False
        
        chess = [["." for _ in range(n)] for _ in range(n)]
        row_used = [False for _ in range(n)]
        col_used = [False for _ in range(n)]
        topleft_diag = [False for _ in range((2 * n)-1)]
        topright_diag = [False for _ in range((2 * n)-1)]

        self.temp_output = []
        empty_cells = []
        solved = False
        counter = 0
        counter2 = 0
        backtrack(0)
        #print(self.temp_output)
        #print(counter, counter2)
        return self.temp_output