class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        length = len(matrix) * len(matrix[0])
        L, R = 0, length - 1
        while L <= R:
            mid = (L+R) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] < target:
                L = mid + 1
            elif matrix[row][col] > target:
                R = mid - 1
            else:
                return True
        return False