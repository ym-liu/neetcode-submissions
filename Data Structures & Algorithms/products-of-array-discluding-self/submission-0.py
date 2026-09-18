class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = n * [None]
        suffixes = n * [None]
        products_except_self = n * [None]

        # prefix array
        product = 1
        for i, num in enumerate(nums):
            product *= nums[i]
            prefixes[i] = product

        # suffix array
        product = 1
        for i, num in enumerate(nums[::-1]):
            product *= nums[n - i - 1]
            suffixes[n - i - 1] = product

        # compute product except self using prefix[i-1] * suffix[i+1]
        for i, num in enumerate(nums):
            if i == 0:
                products_except_self[0] = suffixes[1]
            elif i == n - 1:
                products_except_self[n - 1] = prefixes[n - 2]
            else:
                products_except_self[i] = prefixes[i - 1] * suffixes[i + 1]

        return products_except_self
