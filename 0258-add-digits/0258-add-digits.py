class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10: #两位数以上                    # ← 加这一行：只要还是多位数就继续
            res = 0
            while num>0:
                res+=num%10
                num=num//10
            num = res
        return num
        