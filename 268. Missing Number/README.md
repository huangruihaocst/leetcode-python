# 268. Missing Number

## Solution

好想的方法就是理论和减去实际和，差就是缺的数。

还有一个精妙的方法是用异或。设一个初始值`res`是`nums`的长度`n`，这个数理论上也会出现在`nums`中。
然后遍历`nums`，每次`res`都异或上下标`i`，再异或上值`nums[i]`。
因为相同值异或结果为`0`，任何数异或`0`都是数本身，这些数里有`2n`个两两相等，
有一个不同，就是缺的数，实际来源是数组下标。
其Java代码如下：
```Java
public int missingNumber(int[] nums) { //xor
    int res = nums.length;
    for(int i=0; i<nums.length; i++){
        res ^= i;
        res ^= nums[i];
    }
    return res;
}
```