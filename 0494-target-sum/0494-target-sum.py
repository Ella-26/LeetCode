class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # 0/1背包，选:放进+号，不选：全部放-
        # f[1]:Compose 1 How many methods
        # -1-1-1=3,target=1,需要+4才对，翻一个-1->+1结果影响2，所以2p
        # -s+2p=target->p=(target+s)/2
        s = sum(nums)

        # target比sum都大or凑不到p
        if abs(target) > s or (s + target) % 2 != 0:
            return 0
        # 所有放+的数字
        p = (s + target) // 2

        f = [0] * (p + 1)
        f[0] = 1  # find sum of 0 has 1 method

        for x in nums:
            for c in range(p, x - 1, -1):
                f[c] += f[c - x]
        return f[p]

