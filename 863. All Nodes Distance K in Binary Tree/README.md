# 863. All Nodes Distance K in Binary Tree

## Solution

### 方法一

先用DFS搜索所有的节点，为每个节点标上它的父节点的位置。
这里我太弱了不知道Python可以动态地为对象添加属性，比如这里的`parent`属性不需要像我写的那样用一个字典表示，而是直接`node.parent = xxx`就行了。
然后从`target`开始用BFS搜索到`target`距离为`K`的节点。其中有一个集合记录搜索过的节点，如果搜索过了就不加入搜索集合。
这里还有不知道的一个点就是，集合的表示是大括号，而不是圆括号。空大括号的类型是`dict`，也即`type({}) == dict`，而加了元素的大括号表示集合了，即`type({1}) == set`。
这里还有一个技巧是，如果对一个元素的不同属性有类似的操作，比如`node.left`，`node.right`和`node.parent`都需要检查它是否存在并且加入队列，可以不用单独写每一个，而是`for x in (node.left, node.right, node.parent):`，后面就都一样了，可以简化代码。
此外，`collections.deque`有时可以代替`list`简化操作，它可以从左或从右加入或者删除元素。

## 方法二

全部采用DFS进行搜索。从根节点开始搜索，用`DFS(node)`表示从`node`节点开始到`target`的距离，而且只能往下走，如果不存在路径则返回`-1`。对于`node`总共有4种情况：
- 如果`node`开始到`target`不存在单向向下的路径，则直接返回`-1`。
- 如果`node`就是`target`，则把`target`的全部深度为`K`的孩子都加入答案列表，并返回`0`。
- 如果不是`target`又存在路径，则存在两种情况：
  - `target`是`node`的左孩子的孩子，且左孩子到`target`的距离为`l`，则`node`到`target`的距离为`l + 1`，如果`l + 1`刚好就是`K`，则把`node.val`加入答案列表，如果不是则把`node.right`的深度为`K - l - 2`的孩子们加入答案列表。
  - `target`是`node`的右孩子的孩子。方法同上。
