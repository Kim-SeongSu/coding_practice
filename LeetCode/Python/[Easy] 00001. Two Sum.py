class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]