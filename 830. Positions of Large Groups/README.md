# 830. Positions of Large Groups

## Solution

按要求算，遍历一遍就行了。

我对答案的`res`进行操作的时候是当当前的字符和`curr`不同的时候，
就忘记了如果到结尾刚好也是一个group的情况，比如`aaa`，没有`S[3]`因此就会得到空列表，
就错了。不是第一次错了，注意。