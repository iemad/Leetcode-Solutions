class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()
        for i in nums:
            if i in unique_values:
                return True
            unique_values.add(i)
        return False
        
