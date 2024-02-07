# This solution solves the problem but takes too much time...will retry
class Solution(object):
    def rotate(self, nums, k):
        index = len(nums) - 1

        for i in range(0, k):
            nums.insert(0, nums[index])
            nums.pop(index + 1)
        
        return nums