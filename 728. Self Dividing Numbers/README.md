# 728. Self Dividing Numbers

## Solution

一开始做错是因为`return True`的位置放在了`while`循环里，这里经常容易出错。
`deepcopy`是针对对象(比如`list`)的复制，对于内置类型不需要进行`deepcopy`。
