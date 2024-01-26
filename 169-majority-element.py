class Solution(object):
    def majorityElement(self, nums):
        result = None
        count = 0

        for num in nums:
            if count == 0:
                result = num
            
            if num == result:
                count += 1
            else:
                count -= 1
        
        return result
    
# Use the Boyer-Moore voting algorithm
# Majority vs plurality