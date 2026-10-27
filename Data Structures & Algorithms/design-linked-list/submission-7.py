class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head
        i = -1
        while cur != self.tail:
            if i == index:
                return cur.val    
            cur = cur.next
            i+=1
        return -1

            
    def addAtHead(self, val: int) -> None:
        self.node = ListNode(val)
        self.node.prev = self.head
        self.node.next = self.head.next
        self.head.next = self.node
        self.node.next.prev = self.node

    def addAtTail(self, val: int) -> None:
        self.node = ListNode(val)
        self.node.next = self.tail
        self.node.prev = self.tail.prev
        self.tail.prev = self.node
        self.node.prev.next = self.node

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0:
            return 
        
        self.node = ListNode(val)
        cur = self.head
        i = -1
        while cur != self.tail and i < index:
            cur = cur.next
            i+=1

        if i != index:
            return
        
        self.node.prev = cur.prev
        self.node.next = cur
        cur.prev.next = self.node
        cur.prev = self.node


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        i = -1
        while cur != self.tail:
            if i == index:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next
            i+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)