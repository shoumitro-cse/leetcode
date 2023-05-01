class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       
        # temp_data = {}
        # for index, ele in enumerate(nums):
        #     if ele in temp_data and abs(index - temp_data[ele]) <= k:
        #         return True
        #     temp_data[ele] = index
        # return False
    
        temp = set()
        for index in range(len(nums)):
            if nums[index] in temp:
                return True
            temp.add(nums[index])
            if index >= k:
                temp.remove(nums[index-k])
        return False
    
    
    
    
"""
219. Contains Duplicate II


Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
