class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sofar = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_sofar:
                return [nums_sofar[diff], i]
            nums_sofar[num] = i
        return None
