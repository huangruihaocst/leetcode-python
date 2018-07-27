# 744. Find Smallest Letter Greater Than Target

## Solution

注意一下绕回来的情况即可。

快的答案应用了`bisect`库的`bisect`函数，它有两个参数，第一个是一个排好序的列表，
第二个是一个数，返回值为插入这个数应该所应该在的位置。最后为了解决绕回的问题，模列表长度即可。