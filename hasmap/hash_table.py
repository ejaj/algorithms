class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_v = 0
        for char in key:
            hash_v += ord(char)
        return hash_v % self.MAX

    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val
    #
    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


ht = HashTable()
# ht.add('march 6', 130)
# print(ht.get('march 6'))
ht['march 9'] = 130
ht['march 1'] = 20
ht['dec 17'] = 20
print(ht['march 9'])
del ht['march 6']
print(ht['march 6'])
