# https://leetcode.com/problems/contains-duplicate/

# best Beats 89.69%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True
        
    
    
    
#Beats 80.18%    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for item in nums:
            if item in hash_set:
                return True
            hash_set.add(item)
        return False
        
        
"""
217. Contains Duplicate
Easy
7.9K
1.1K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
2.4M
Submissions
3.9M
Acceptance Rate
61.4%

"""
