class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        n=len(s)
        for i in range(0, n-1):  # 0~n-2
            left = 0
            right =0
            for j in range(0, i+1):
                if s[j] == '0':
                    left += 1
            for j in range(i+1,n):
                if s[j] == '1':
                    right += 1
            score=left+right
            res = max(res,score)
        return res