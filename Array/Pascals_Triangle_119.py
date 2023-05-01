class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex == 2:
            return [1, 2, 1]
        
        # It will create an array whose values are all 1.
        res = [1] * (rowIndex+1) 
        # It will be used to track the previous record
        prev = [1, 2, 1]
        
        for y in range(3, rowIndex+1):
            for x in range(1, y):
                # Applied Pascal's Triangle theorem
                res[x] = prev[x] + prev[x-1] 
            # Updated previous record
            prev = res[:]
        return res
