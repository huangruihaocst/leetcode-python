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
因为有可能一直到出循环都没有满足`if`条件，但是实际上`res`需要更新了

```Python
for loop:
    if xxx:
        res = max(...)  # update res
    else:
        xxx
res = max(...)  # update res again
```

6. 树只有根节点一个节点

```Python
if not root.left and not root.right:
```

7. 动态规划的时候问到初始值，可能造成`IndexError`

```Python
if n == 1:  # prevent IndexError
    xxx
dp = [...]
dp[1] = xxx
dp[2] = xxx
# transformation equation
```

8. 负数和零

```Python
if n <= 0:
```

## 注意事项总结

1. 注意返回的数据类型，比如`1`和`'1'`不同，`1`和`1.0`不同。

2. 动态规划的时候，如果只跟前固定数目的项有关，则可以不用数组而只用固定数目的变量存储。
比如`d[i] = d[i - 1] + d[i - 2]`，则可以只用两个变量存储。