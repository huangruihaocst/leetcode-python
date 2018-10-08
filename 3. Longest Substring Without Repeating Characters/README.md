# 3. Longest Substring Without Repeating Characters

## Solution

用两个指针`left`和`right`分别记录当前字符串的最左和最右，和一个字典来记录当前每个字符出现的位置。
依次挪动右指针，如果没有出现过，则无所谓；如果出现过，且出现的位置在`left`右边，那么把`left`挪到这个位置的右边一个。
过程中时刻更新`res`也即当前最大子串长度。