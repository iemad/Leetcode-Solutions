class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        updated_nums = []

        for i in range(2):
            for j in nums:
                updated_nums.append(j)
                
        return updated_nums
