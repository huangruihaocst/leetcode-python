# 496. Next Greater Element I

## Solution

可以直接像我做得对每个数都找到在`nums2`中的位置再向后找。复杂度是`O(len(nums1)*len(nums2)/2)`。

答案里有两种方法还比较好。

### 方法一

对`nums2`中的每一个数找它后面比它大的数，然后再对应回`nums1`。复杂度是`O(len(nums2) ^ 2 / 2 + len(nums1))`。

### 方法二

倒着遍历`nums2`，同时维护一个栈，用一个字典记录`nums2`中的每一个数的Next Greater Element。
如果栈顶数比当前数大，则这个数的Next Greater Element就是这个栈顶。同时也要加入这个数入栈。
如果栈顶数比当前数小，则一直弹出栈顶直到找到第一个比当前数大的数，作为这个数的Next Greater Element。
找不到就返回`-1`。

然后对于`nums1`中的元素，因为有字典的存在，找到每一个数的Next Greater Element就只需要`O(1)`了。