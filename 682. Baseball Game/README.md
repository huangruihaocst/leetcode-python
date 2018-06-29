# 682. Baseball Game

## Solution

完全可以用栈来简单实现，我做得过于复杂了。
当发现`C`时把栈顶弹出即可，不用检查上个`valid`的分数是谁。

此外，`enumerate`是个好东西，可以在遍历`value`的同时遍历`index`。
