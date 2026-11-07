class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0

        while cur and index <= self.length-1:
            if index == i:
                return cur.val
            cur = cur.next
            i+=1
        return -1



    def addAtHead(self, val: int) -> None:
        cur = self.head
        node = Node(val)
        node.prev = cur
        node.next = cur.next
        cur.next = node
        node.next.prev = node
        self.length +=1


    def addAtTail(self, val: int) -> None:
        cur = self.tail
        node = Node(val)
        node.prev = cur.prev
        node.next = cur
        node.prev.next = node
        node.next.prev = node
        self.length +=1


    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        node = Node(val)
        i = 0
        while cur and index <= self.length:
            if i == index:
                node.prev = cur.prev
                node.next = cur
                node.prev.next = node
                node.next.prev = node
                self.length +=1
            i+=1
            cur = cur.next
                

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        i = 0
        while cur and index <= self.length-1:
            if i == index:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.next = None
                cur.prev = None
                self.length -=1
            i+=1
            cur = cur.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)