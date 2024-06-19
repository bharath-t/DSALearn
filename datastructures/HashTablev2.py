# handling collisions.
# Option 1. instead of value, we store list of tuples/list. this way, we can store multiple pairs whose keys return same hash
# note: we need to store key, value both in the list of lists
# while searching, we get index using hash, do linear search
# big o is o(n) - worst case, all keys give same hash, key we are searching is at the last

# Option 2. get index using hash, insert in next available space. we do a cycle ie. if last spot is empty, we go to first.

class HashTablev2():
    def __init__(self):
        self.len = 20
        base_list = [[] for x in range(self.len)]
        self.base_list = base_list

    def get_hash(self, key):
        hash = 0
        for x in key:
            hash += ord(x)
        return hash % self.len

    def __setitem__(self, key, value):
        index = self.get_hash(key)

        # check if key already exists
        sub_list = self.base_list[index]
        for sub_index, element in enumerate(sub_list):
            if element[0] == key:
                self.base_list[index][sub_index] = (key, value)
                return
        # else append    
        self.base_list[index].append((key, value))

    def __getitem__(self, key):
        index = self.get_hash(key)
        sub_list = self.base_list[index]
        for sub_index, element in enumerate(sub_list):
            if element[0] == key:
                return element[1]
        print('element not found')            
        

    def __delitem__(self, key):        
        index = self.get_hash(key)
        self.base_list[index] = None
        
        

if __name__ == '__main__':
    dict = HashTablev2()
    print(dict.base_list)

    # dict.insert('a',1)
    dict['a'] = 1    
    dict['b'] = 2
    dict['ab'] = 3
    dict['ba'] = 4
    dict['a'] = 5

    # print(dict.get_value('a'))
    print(dict['ab'])

    print(dict.base_list)

# Big O:
# with collisions
# search : O(n) - All keys return same hash. so we have to linear search    
# insert : O(n) - All keys return same hash. so we have to linear search    
# if the hash function is good enough to avoid collisions, search, insert, delete will happen in O(1)