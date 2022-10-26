class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        reversed_x = int(str_x[::-1])
        if reversed_x not in range(-2**31,  2**31-1):  
            return 0 
        return reversed_x if x > 0 else (reversed_x * -1)



"""
7. Reverse Integer
Medium
8.8K
10.9K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
Accepted
2.3M
Submissions
8.5M
Acceptance Rate
27.2%
Seen this question in a real interview before?
1/4
Yes
No
Related Topics
"""
