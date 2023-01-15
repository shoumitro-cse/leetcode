class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_length = len(nums)
        result = [1] * num_length
        
        prefix = 1
        for i in range(0, num_length):
            # suffix_result = [1,2,6,24]
            result[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        # reverse index list
        for i in range(num_length-1, -1, -1):
            # prefix_result = [24, 24, 12, 4]
            # result = [24(1*24), 12(1*12), 8(2*4), 6(6*1)]
            result[i] *= suffix
            suffix *= nums[i]
        return result

        # nums = [1,2,3,4]
        # suffix_result = [1,2,6,24]
        # prefix_result = [24, 24, 12, 4]
        # result = [24(1*24), 12(1*12), 8(2*4), 6(6*1)]







"""

238. Product of Array Except Self
Medium
15.9K
882
Companies
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
