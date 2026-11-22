class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row1 = len(matrix)
        col1 = len(matrix[0])
        l, r = 0, (row1*col1)-1

        while l <= r:
            mid = (l+r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if target < matrix[row][col]:
                r = mid-1
            elif target > matrix[row][col]:
                l = mid+1
            elif target == matrix[row][col]:
                return True
        return False
            