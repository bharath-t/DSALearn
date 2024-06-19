# hash table/map - python dictionary
# its a list itself but the trick is with index so search takes 0(1)
# create a hash function which takes in key, returns index. store data at that index. for retrieval, use the same hash which gives index

class HashTable():
    def __init__(self):
        self.len = 20
        base_list = [None for x in range(self.len)]
        self.base_list = base_list

    def get_hash(self, key):
        hash = 0
        for x in key:
            hash += ord(x)
        return hash % self.len

    # https://docs.python.org/3/library/operator.html
    # instead of insert, get_value, del_key change names to standard python operator names (__setitem__, __getitem__, __delitem__)
    # this way, we can use obj[key], del obj[key] instead of obj.get_value(key) - similar to what we do with python lists
    # def insert(self, key, value):
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.base_list[index] = value

    # def get_value(self, key):
    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.base_list[index]

    # this is redundant. we can use setitem and set it to null directly
    # def del_key(self, key):
    def __delitem__(self, key):        
        index = self.get_hash(key)
        self.base_list[index] = None
        
        

if __name__ == '__main__':
    dict = HashTable()
    print(dict.base_list)

    # dict.insert('a',1)
    dict['a'] = 1    
    dict['b'] = 2
    dict['ab'] = 3
    dict['ba'] = 4

    # print(dict.get_value('a'))
    print(dict['a'])

    # notice below print gives 4 instead of 3. because ab, ba return same hash, inserting ba replaced earlier inserted ab.
    # this is called collision
    print(dict['ab'])

    # dict.del_key('b')
    del dict['b']

    print(dict.base_list)


# Big O:
# assuming no collisions
# search : O(1)    
# insert : O(1)