class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        triangle = self.pascalhelper(rowIndex+1, 1, triangle)
        return triangle[-1]
  
    def pascalhelper(self, numRows, curr_row, triangle):
        if numRows == 0:
            return triangle
        if len(triangle) >= 1:
            temp_last = triangle[-1]
        else:
            temp_last = []
        new_row = [0] * (curr_row)
        new_row[0] = 1
        new_row[-1] = 1
        for spot in range(1, len(temp_last)):
            new_row[spot] = (temp_last[spot-1] + temp_last[spot])
        triangle.append(new_row)
        return self.pascalhelper(numRows-1,curr_row+1, triangle)