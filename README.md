# leetcode

## Generate

运行
```bash
$ chmod u+x generate.command
$ ./generate.command
```
可以生成默认的文件结构，包括一个`solution.py`和一个`README.md`。

## 特殊情况总结

1. 空树

```Python
if not root:
```

2. 空字符串

```Python
if not s:
```

3. 空链表

```Python
if not head:
```

4. 空数组

```Python
if not li:
```

5. 在循环的时候如果在循环内更新`res`，有可能在结尾处还需要更新一次，
因为有可能一直到出循环都没有满足`if`条件，但是实际上`res`需要更新了。

```Python
for loop:
    if xxx:
        res = max(...)  # update res
    else:
        xxx
res = max(...)  # update res again
```