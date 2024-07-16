class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for item in range(1, len(nums)):
            if nums[item] == nums[i]:
                continue
            i += 1
            nums[i] = nums[item]
        return i+1
