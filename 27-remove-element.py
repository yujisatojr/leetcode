class Solution(object):
    def removeElement(self, nums, val):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.remove(nums[i])
                i -= 1
            else:
                i -= 1

# lessons learned: use remove() instead of pop() to avoid index out of range