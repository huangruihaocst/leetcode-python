# 404. Sum of Left Leaves

## Solution

递归。一般来说判断有没有左右孩子是根据之后会不会出现访问`None`的属性的，
如果不会就不用判断，而是在函数入口判断`node`是不是`None`就行。