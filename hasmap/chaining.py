class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

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
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


ht = HashTable()

ht['march 6'] = 120
ht['march 6'] = 78
ht['march 8'] = 67
ht['march 9'] = 4
ht['march 17'] = 459
print(ht.arr)
print(ht['march 17'])
