class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_l, row_r = 0,len(matrix)
        col_l, col_r = 0, len(matrix[0])

        while (row_l < row_r - 1):
            mid_row = (row_l + row_r)//2
            if matrix[mid_row][0] <= target:
                row_l = mid_row
            else:
                row_r = mid_row

        while (col_l < col_r-1):
            mid_col = (col_l + col_r)//2
            if matrix[row_l][mid_col] <= target:
                col_l = mid_col
            else:
                col_r = mid_col
        
        return matrix[row_l][col_l] == target

