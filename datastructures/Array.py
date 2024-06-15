class Array(): 
    def __init__(self, data = None):
        if data is None:
            self.size = 2 #starting with size 2
            self.data = [None] * self.size 
            self.len = 0
        else:
            self.data = data
            self.len = self.get_len()
            self.size = self.len

    def get_len(self):
        if self.data is None:
            return 0

        len = 0
        for x in self.data:
            if x is not None:
                len += 1
            else:
                break
        return len

    def append(self, value):        
        if self.len < self.size:
            self.data[self.len] = value
            self.len += 1        
        else:
            self.resize()
            self.append(value)

    def resize(self):
        new_size = 2 * self.size
        new_array = [None] * new_size
        for i in range(0,self.size):
            new_array[i] = self.data[i]
        self.data = new_array
        self.size = new_size

    def insert(self, index, value): #assuming index in within 2 times the size of array. (doubling for every resize)
        if index < 0:
            print('invalid index')
            return        
        if self.len == self.size:
            self.resize()        
        if index >= self.len and index < self.size:
            self.data[index] = value
        else: 
            for i in range(self.len-1, index-1, -1):
                self.data[i+1] = self.data[i]
            self.data[index] = value        
        self.len+= 1

    def search(self, value):
        for i in range(self.len):
            if self.data[i] == value:
                return i
        print('value not found')
        return -1


    def deletebyIndex(self, index):
        if index >= 0 and index < self.len:
            del_value = self.data[index]
            for i in range(index, self.len):
                self.data[i] = self.data[i+1]
            self.len -= 1
            print(f'deleted {del_value} ')

        else:
            print('invalid index')


    def deletebyValue(self, value):
        index = self.search(value)
        if index == -1:
            return
        self.deletebyIndex(index)

    def print(self):
        a = []
        for i in range(self.len):
            a.append(self.data[i])
        print(a)
        


    

if __name__ == '__main__':
    l2 = Array([1,2,3,4])
    l2.print()

    l1 = Array()
    l1.append(1)
    l1.append(2)
    l1.append(3)    
    l1.print()

    print(l1.search(3))
    print(l1.search(4))

    l1.insert(3, 4)
    l1.insert(1, 9)
    l1.print()

    l1.deletebyIndex(2)
    l1.print()

    l1.deletebyValue(4)
    l1.deletebyValue(10)
    l1.print()


# Big O
# append : O(1)
# insert : O(n) -> worst case is insert at beginning
# search by index : O(1)
# search by value : O(n)
# del by index : O(n) -> worst case is delete at beginning
# del by value : O(n) -> worst case is delete at beginning/ending

