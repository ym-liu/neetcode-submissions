class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanum = "".join(c for c in s if c.isalnum()).lower()
        n = len(s_alphanum)
        return s_alphanum[:n//2] == s_alphanum[n//2+n%2::][::-1]
        # n = len(s_alphanum)

        # for i in range(n // 2):
        #     if s_alphanum[i] != s_alphanum[-i - 1]:
        #         return False

        # return True
