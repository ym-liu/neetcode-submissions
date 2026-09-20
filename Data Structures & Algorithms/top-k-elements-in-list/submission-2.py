class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqs = defaultdict(int)
        buckets = [[] for _ in range(n + 1)]
        answer = []

        # build freqs dict
        for num in nums:
            freqs[num] += 1

        # build buckets
        for num in freqs:
            buckets[freqs[num]].append(num)

        # get top k most freq
        for i in range(n, 0, -1):
            if len(answer) == k:
                return answer
            answer.extend(buckets[i])

        return answer
