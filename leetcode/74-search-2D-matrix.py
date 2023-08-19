class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Searches for a target value in a sorted 2D matrix.  
        :param matrix: The 2D matrix to search in.
        :param target: The value to search for.
        :return: True if the target is found, False otherwise.
        '''
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) >> 1
            num = matrix[mid // m][mid % m]

            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
