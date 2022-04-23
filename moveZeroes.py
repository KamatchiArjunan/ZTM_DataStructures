'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(nums)
        n = len(nums)
        i,j = 0,0
        while(i < n):
          if nums[j] == 0:
            del nums[j]
            nums.append(0)
            i += 1
            continue
          j += 1
          i += 1
        print(nums)
            
numArray = [0,1,0,3,12]
obj = Solution()
obj.moveZeroes(numArray)
