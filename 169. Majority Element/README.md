# 169. Majority Element

## Solution

我的方法的复杂度是`O(n)`，也很好理解，适用于类型的数据，不论能否排序。

最快答案的方法的复杂度是`O(log(n))`，但是仅适用于能排序的数据，很巧妙。

答案的代码是：

```Python
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums)//2]
```