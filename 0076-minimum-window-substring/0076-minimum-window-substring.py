class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        cnt_s = Counter()  # tem substring record
        cnt_t = Counter(t)
        # right-left=len(s)+1 initial window larger than s
        ans_left, ans_right = -1, len(s)
        left = 0

        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:  # s contains t
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left : ans_right + 1]

