class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        pt = [[1], [1, 1]]

        for i in range(2, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = pt[i-1][j-1] + pt[i-1][j]
            pt.append(row)

        return pt