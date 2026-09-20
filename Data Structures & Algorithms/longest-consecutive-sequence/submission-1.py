class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_seq = 0

        for num in nums:
            nums_set.add(num)

        for num in nums:
            if not num - 1 in nums_set:
                pointer = num
                while pointer + 1 in nums_set:
                    pointer += 1
                max_seq = max(max_seq, pointer - num + 1)

        return max_seq
