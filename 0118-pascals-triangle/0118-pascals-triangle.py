class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # row of length i+1, edges are 1
            for j in range(1, i):  # fill interior elements
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        
        return triangle