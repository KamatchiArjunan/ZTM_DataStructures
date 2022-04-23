class MyHashMap(object):

    def __init__(self):
        self.buckets = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.buckets.update({key: value})

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for k, v in self.buckets.items():
            if key == k:
                return v
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.buckets.get(key):
            del self.buckets[key]


# Your MyHashMap object will be instantiated and called as such:
# ["MyHashMap","remove","put","put","put","put","put","put","get","put","put"]
# [[],[2],[3,11],[4,13],[15,6],[6,15],[8,8],[11,0],[11],[1,10],[12,14]]
obj = MyHashMap()
print(obj.remove(2))
print(obj.put(3, 11))
print(obj.put(4, 13))
print(obj.put(15, 6))
print(obj.put(6, 15))
print(obj.put(8, 8))
print(obj.put(11, 5))
print(obj.get(11))
print(obj.put(1, 10))
print(obj.put(12, 14))
