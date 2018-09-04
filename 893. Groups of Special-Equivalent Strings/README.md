# 893. Groups of Special-Equivalent Strings

## Solution

### 方法一

给每个字符串定义hash，使得Special-Equivalent的字符串相等， 不同的不等。
然后用`dict`。（`set`更好）

这种做法不保证没有冲突。

### 方法二

类似于hash，把奇位和偶位分别排序接起来作为hash，这种方法是保证正确的。