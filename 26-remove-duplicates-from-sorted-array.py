class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        j = len(nums) - 1
        for k in range(0, len(nums) - 1):
            if i<= j:
                if i <= j and nums[i-1] == nums[i]:
                    nums.remove(nums[i])
                    j -= 1
                    i -= 1
            i += 1

# lessons learned: compare numbers next to each other (i-1 and i) in array. Be mindful of the case like [1, 1]