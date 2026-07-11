class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = "aeiou"
        res = 0
        for i in range(left, right + 1):                    # ← 只遍历 left~right
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:    # ← start and end
                res += 1
        return res
        