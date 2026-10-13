class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # if not rotated, or rotated n times
        if nums[left] <= nums[right]:
            return nums[left]

        # binary search for min
        while left <= right:
            mid = (left + right) // 2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
