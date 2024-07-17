class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        empty_dict = {}

        for _index, _number in enumerate(nums):
            diff = target - _number

            if diff in empty_dict:
                return [empty_dict[diff], _index]
            empty_dict[_number] = _index
