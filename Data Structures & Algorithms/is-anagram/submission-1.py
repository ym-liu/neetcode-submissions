class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = defaultdict(int)

        for c in s:
            char_freq[c] += 1

        for d in t:
            if not d in char_freq:
                return False

            char_freq[d] -= 1
            if char_freq[d] == 0:
                char_freq.pop(d)

        return not char_freq
