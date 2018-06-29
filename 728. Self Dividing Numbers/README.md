# 728. Self Dividing Numbers

## Solution

一开始做错是因为return True的位置放在了while循环里，这里经常容易出错。
deepcopy是针对对象(比如list)的复制，对于内置类型不需要进行deepcopy。
