# 矩阵转置笔记

## 关键点

创建二维列表时，因为转置导致行列互换，**尺寸也随之改变**：

```
原矩阵：2 × 3
转置后：3 × 2
```

```python
# 正常创建 m×n 矩阵
matrix = [[0] * cols for _ in range(rows)]

# 转置后：行列互换，rows → cols
new_matrix = [[0] * rows for _ in range(cols)]
```