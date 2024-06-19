# Instead of assigning contigous memory, start with a single node (data, pointer to next node)
# keep track of address of starting node (head), traverse from head

class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    # set head to None
    def __init__(self):
        self.head = None        

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return

        cur = self.head
        while (cur.next):
            cur = cur.next
        cur.next = node
        return        

    def search(self, data):
        idx = 0
        cur = self.head
        if cur.data == data:
            return idx        
        while (cur.next):
            idx += 1
            if cur.next.data == data:                
                return idx
            cur = cur.next
        print('not found')
        return -1

    def insertAfter(self, value, data):
        cur = self.head
        while (cur):
            if cur.data == value:
                node = Node(data, cur.next)
                cur.next = node
                return
            cur = cur.next
        print('not found')

    def print_ll(self):
        if self.head == None:
            print('empty linked list')
        cur = self.head
        while(cur):
            print(cur.data)
            cur = cur.next
        

    def delete(self, data):
        pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.search(1))
    print(ll.search(3))
    print(ll.search(4))
    ll.insertAfter(2,4)
    ll.insertAfter(1,5)
    ll.print_ll()


# Big O: Singly Linked List
# insert: O(n) - insert at end (Worst case)
# append: O(n) - always. could be O(1) if we keep track of tail as well
# search by value: O(n) - search last value (Worst case)
# seach by index: O(n) - search last index (Worst case)


    