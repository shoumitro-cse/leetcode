
# Beats 93.40%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] 
        curr_sum = 0
        for item in nums:
            if curr_sum < 0: 
                curr_sum = 0
            curr_sum += item 
            max_sum  = max(max_sum, curr_sum)
        return max_sum


# print maximum array with largest sum
class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0] 
        curr_sum = 0
        max_arr = [nums[0]]
        curr_arr = []
        for item in nums:
            if curr_sum < 0:
                curr_sum = 0 
                curr_arr = []
            else:
                curr_arr.append(item)
            curr_sum += item
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_arr = curr_arr[:]
        return max_sum, max_arr


nums = [-1]        
nums = [-2,1,-3,4,-1,2,1,-5,4]
largest_sum, largest_arr = Solution().maxSubArray(nums)
print(largest_sum, '\n', largest_arr)



"""
53. Maximum Subarray
Medium
27.4K
1.2K
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
