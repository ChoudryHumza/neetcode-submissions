class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next =  None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        cur = self.head.next

        if index < self.length:
            for i in range(index+1):
                if i == index:
                    return cur.val
                cur = cur.next
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.prev = self.head
        node.next = self.head.next
        node.prev.next = node
        node.next.prev = node
        self.length+=1
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node
        self.length +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        cur = self.head.next
        for i in range(index+1):
            if index == 0:
                self.addAtHead(val)
                break
            elif index == self.length:
                self.addAtTail(val)
                break
            elif i == index:
                node.prev = cur.prev
                node.next = cur
                node.prev.next = node
                node.next.prev = node
                self.length+=1
                break
            cur = cur.next
            


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        if index < self.length:
            for i in range(index+1):
                if i == index:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur.next = None
                    cur.prev = None
                    self.length-=1
                    break
                cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)