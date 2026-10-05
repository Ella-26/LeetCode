class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        # w1=ab
        # w2=ac
        # f[1][1] = "a" 变成 "a" 最少几步
        # f[1][2] = "a" 变成 "ac" 最少几步
        # f[2][1] = "ab" 变成 "a" 最少几步
        # f[2][2] = "ab" 变成 "ac" 最少几步
        #         ""   a   ac
        # ""         0   1   2
        # a          1   0   1
        # ab         2   1   ?
        # 初始化行和列，no need compare word1 and word2
        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        return f[n][m]

