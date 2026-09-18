class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_arr_dict = {}

        for s in strs:
            s = s.lower()
            freq_arr = 26 * [0]
            for c in s:
                index = ord(c) - ord("a")
                freq_arr[index] += 1
            freq_arr = tuple(freq_arr)

            if freq_arr in freq_arr_dict:
                freq_arr_dict[freq_arr].append(s)
            else:
                freq_arr_dict[freq_arr] = [s]

        return list(freq_arr_dict.values())
