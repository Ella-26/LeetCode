class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        path = [""] * 2 * n

        def dfs(i, open):
            # open:num of (
            # i: sum of (),->2*n
            # i-open:num of )
            if i == 2 * n:
                ans.append("".join(path))
                # ( Didn't get to n，add (
            if open < n:
                path[i] = "("
                dfs(i + 1, open + 1)
                # ) didn't get to open,add)
            if i - open < open:
                path[i] = ")"
                dfs(i + 1, open)

        dfs(0, 0)
        return ans

