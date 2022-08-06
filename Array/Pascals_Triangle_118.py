class Solution:
    # 75 ms	
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows >= 1:
            res.append([1])
        if numRows >= 2:
            res.append([1, 1])
        if numRows >= 3:
            res.append([1, 2, 1])
        if numRows >= 4:
            for row in range(4, numRows+1):
                prev = res[-1]
                ans_row = [1] * row
                for index in range(1, len(prev)):
                    ans_row[index] = prev[index] + prev[index-1]
                res.append(ans_row)
        return res
    
        
class Solution:
    # 47 ms	
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(numRows):
            temp_row = [] # for one row
            for col in range(row+1):
                if col == 0 or col == row:
                    temp_row.append(1) # for first an last column value
                else:
                    temp_row.append(res[row-1][col] + res[row-1][col-1])
            res.append(temp_row)
        return res
    
        
        
"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

"""
Add
