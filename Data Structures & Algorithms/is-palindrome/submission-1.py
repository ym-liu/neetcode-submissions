class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanum = "".join(c for c in s if c.isalnum()).lower()
        if s_alphanum == s_alphanum[::-1]:
            return True
        return False
        # n = len(s_alphanum)

        # for i in range(n // 2):
        #     if s_alphanum[i] != s_alphanum[-i - 1]:
        #         return False

        # return True
