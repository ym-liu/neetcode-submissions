class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = set()

        for num in nums:
            if num in nums_dict:
                return True
            nums_dict.add(num)

        return False
