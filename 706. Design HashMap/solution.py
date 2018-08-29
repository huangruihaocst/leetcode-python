PRIME = 72707


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.big_list = list()
        for pos in range(PRIME):
            self.big_list.append(list())

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        pos = key % PRIME
        found = False
        for pair in self.big_list[pos]:
            if pair[0] == key:
                found = True
                pair[1] = value
        if not found:
            self.big_list[pos].append([key, value])

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        pos = key % PRIME
        for pair in self.big_list[pos]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        pos = key % PRIME
        for i, pair in enumerate(self.big_list[pos]):
            if pair[0] == key:
                del self.big_list[pos][i]
                break


if __name__ == '__main__':
    # Your MyHashMap object will be instantiated and called as such:
    obj = MyHashMap()
    obj.put(1, 1)
    obj.remove(1)
    print(obj.get(1))
