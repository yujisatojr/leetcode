class Solution(object):
    def removeDuplicates(self, nums):
        i = len(nums) - 1
        j = len(nums) - 2
        k = len(nums) - 3

        while k >= 0:
            if nums[i] == nums[j] == nums[k]:
                nums.remove(nums[i])
            i -= 1
            j -= 1
            k -= 1
            
'''
Lessons learned: Start by outlining the steps/process in the comment format to break down the problem

My initial attempt was:
1. Count how many times each number appears in the array
2. If the total count is above 2, reduce it to 2
but I found that simply comparing the 3 items next to each other in the list worked just fine
'''