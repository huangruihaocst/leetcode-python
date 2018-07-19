# 796. Rotate String

## Solution

注意`A`或者`B`是空串的情况。

答案的方法比较巧妙。只需`B in A + A and len(A) == len(B)`，完全没想到。