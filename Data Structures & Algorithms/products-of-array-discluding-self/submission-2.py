class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_left = nums[0]
        product_right = nums[n - 1]
        answer = n * [1]

        for i in range(1, n - 1):
            answer[i] *= product_left
            answer[-i - 1] *= product_right

            product_left *= nums[i]
            product_right *= nums[-i - 1]
        
        answer[0] = product_right
        answer[n-1] = product_left

        return answer
