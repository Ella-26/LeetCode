写法 1：固定次数循环 ⭐ 最常用
```
for i in range(n):          # i = 0, 1, 2, ..., n-1
    # 要重复做的事
```
写法 2：指定范围
```
for i in range(开始, 结束):  # i = 开始 ... 结束-1
    for i in range(1, 5):   # i = 1, 2, 3, 4
```
写法 3：指定步长
```
for i in range(开始, 结束, 步长):
    for i in range(0, 10, 2):  # i = 0, 2, 4, 6, 8
```
写法4:遍历数组
```
nums = [10, 20, 30]
for num in nums:             # num = 10, 20, 30
    print(num)
#← num 是循环变量，每一轮自动拿列表里的下一个值
#0    ← 第一轮 num = nums[0] = 0
#2    ← 第二轮 num = nums[1] = 2
```