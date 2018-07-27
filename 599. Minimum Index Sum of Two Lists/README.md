# 599. Minimum Index Sum of Two Lists

## Solution

就是用`dict`能比较方便地检查值对应的`index`。

最快的答案在更新最小值的同时把等于最小值的饭店名称也求出来了，比较简洁。
具体做法是一开始设一个下标和的可能的最大值为当前下标和的最小值，然后当检查到某下标和的时候，
如果下标和比这个最小值要小，则结果列表`res`变为这个饭店的单元素列表；如果等于，
则把该饭店名称加入饭店名称列表。