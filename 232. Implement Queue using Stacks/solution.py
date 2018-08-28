class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

# Solution 1: One Stack
# class MyQueue:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = Stack()
#
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.stack.push(x)
#
#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         tmp = Stack()
#         while not self.stack.is_empty():
#             tmp.push(self.stack.pop())
#         res = tmp.pop()
#         while not tmp.is_empty():
#             self.stack.push(tmp.pop())
#         return res
#
#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         tmp = Stack()
#         while not self.stack.is_empty():
#             tmp.push(self.stack.pop())
#         res = tmp.peek()
#         while not tmp.is_empty():
#             self.stack.push(tmp.pop())
#         return res
#
#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return self.stack.is_empty()


# Solution 2: Two Stacks
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while not self.out_stack.is_empty():
            self.in_stack.push(self.out_stack.pop())
        self.in_stack.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.in_stack.is_empty() and self.out_stack.is_empty()


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())
