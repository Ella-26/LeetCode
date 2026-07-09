# 📘 SQL 常见用法笔记

---

## 一、`OR` 条件 — 满足任意一个就算

```sql
SELECT name        -- ③ 最后，只取 name 这一列
FROM Customer      -- ② 然后，从 Customer 这张表里找
WHERE referee_id != 2 OR referee_id IS NULL;  -- ① 先筛选，留下符合条件的行
```

> 执行顺序：`WHERE` → `FROM` → `SELECT`

---

## 二、等于条件写法

不同数据类型的字段，条件写法不一样：

| 数据类型 | 示例条件 | 写法 |
|----------|----------|------|
| 整数（INT） | `id` 等于 2 | `id = 2` |
| 小数（FLOAT / DECIMAL） | `price` 等于 9.99 | `price = 9.99` |
| 字符串（VARCHAR / CHAR / TEXT） | `name` 等于 'Alice' | `name = 'Alice'` |
| 枚举（ENUM） | `status` 等于 'active' | `status = 'active'` |
| 空值（NULL） | `id` 等于 NULL | `id IS NULL`（注意：不能用 `= NULL`） |
