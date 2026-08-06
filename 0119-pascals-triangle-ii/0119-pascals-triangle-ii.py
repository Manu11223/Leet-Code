class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        
        for i in range(2, rowIndex + 1):  # build up row by row
            for j in range(i - 1, 0, -1):  # right to left, skip edges (always 1)
                row[j] += row[j - 1]
        
        return row