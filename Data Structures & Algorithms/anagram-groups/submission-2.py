class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        anagrams = []

        for s in strs:
            freq = 26 * [0]
            for c in s:
                freq[ord("a") - ord(c)] += 1
            strs_dict[tuple(freq)].append(s)

        for l in strs_dict:
            anagrams.append(strs_dict[l])

        return anagrams
