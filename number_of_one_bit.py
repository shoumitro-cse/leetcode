# Given a positive integer N, print count of set bits in it. 

class Solution:
	def setBits(self, N):
		count = 0
		for binary_digit in str(bin(N).replace("0b", "")):
			if binary_digit == '1':
				count += 1
		return count


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)
		
		
"""

Example 1:

Input:
N = 6
Output:
2
Explanation:
Binary representation is '110' 
So the count of the set bit is 2.

Example 2:

Input:
8
Output:
1
Explanation:
Binary representation is '1000' 
So the count of the set bit is 1.
"""
