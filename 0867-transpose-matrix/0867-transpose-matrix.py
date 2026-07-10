class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        newmatrix = [[0]* rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                newmatrix[j][i]=matrix[i][j]
        return newmatrix