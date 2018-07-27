# 873. Length of Longest Fibonacci Subsequence

## Solution

### 方法一

这种方法我自己也想出来一半，但是错过的关键，也即暴力算法。

很明显斐波那契数列只要知道了其中的任意连续两项数列就确定了，
因此可以遍历头两项的全部可能然后找到每种情况下的最大长度。我的做法就是每次往后找到合适的就继续，
找不到就返回，但是这样的复杂度太高了，可以不用每次都往后找，因此可以用`set`。
之前不知道的是`set`是用`hash`实现的，和`dict`类似，检查一个元素是否属于`set`的复杂度只有`O(1)`。
其实当然也能用`dict`来实现，只是不够优雅，然而这我都没想到...

在实现的时候我把`S = set(A)`写在了函数`max_length(m, n)`的内部，导致每次调用的时候都得重新计算一遍`S`,
这样会超时，放到外面就能过了。

### 方法二

方法二是动态规划。

定义斐波那契数列的节点的概念，它由两个数组的下标`(i, j)`组成，意味着数列中连续两项的下标。
比如斐波那契子序列`A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13`就可以写成连续的节点序列
`(1, 2) <-> (2, 4) <-> (4, 7) <-> (7, 10)`。

我们定义一个`longest`，`longest[i][j]`表示以下标为`i`和`j`的两项作为最后两项的子序列的最大长度。
因此，如果`longest[j][k] = longest[i][j] + 1`，就要求`A[k] = A[i] + A[j]`。
我们从前往后计算`longest`，当循环到`longest[j][k]`的时候，检查一下`A[i] = A[k] - A[j]`
是否在数组里，并且是否`i < j`，因为有情况`j`很接近`0`而`k`比较大，这种情况下就会出现`j < i < k`，
显然是不符合我们的期待的。

在实现的时候我还遇到一个坑。一开始我没有用`defaultdict`这个内键函数，而是建了一个二维数组`[[2] * len(A)] * len(A)`。
然而在修改其中的一项的时候，二维数组中的其他一维数组的对应项也会发生改变，
比如`[[2, 2], [2, 2]]`会因为第一个一维数组的第一个数改成`3`而变成`[[3, 2], [3, 2]]`。
这是因为每个一维数组都是一个一维数组的引用，而不是复制，在改变任意一个数组的时候，引用的数组发生改变，导致所有数组都改变。

因此可以使用`defaultdict`，它可以返回一个类似`dict`的对象，也即给`key`返回`value`。
它需要一个`default_factory`参数，它指定对于任意的输入，默认的输出是什么，参数类型是函数对象。