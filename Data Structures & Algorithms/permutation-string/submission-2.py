class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_dict = defaultdict(int)
        for c in s1:
            s1_dict[c] += 1

        s2_dict = defaultdict(int)
        n1 = len(s1)
        pointer = n1 - 1
        for i in range(0, n1):
            s2_dict[s2[i]] += 1

        for c in s2[n1:]:
            if s1_dict == s2_dict:
                return True

            s2_dict[c] += 1

            start = s2[pointer - n1 + 1]
            s2_dict[start] -= 1
            if not s2_dict[start]:
                s2_dict.pop(start)

            pointer += 1

        return s1_dict == s2_dict
