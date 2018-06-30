# 575. Distribute Candies

## Solution

完全没想可以用`set`简化这么多，注意`set`的使用。
此外，对字典按照`value`排序的方法
```python
sorted(d.items(), key=lambda kv: kv[1])
```
。
