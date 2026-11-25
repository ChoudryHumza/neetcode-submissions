# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode(0)
        head = node
        l1 = list1
        l2 = list2

        count = 0
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            elif l1.val > l2.val:
                node.next = l2
                node = node.next
                l2 = l2.next
            count += 1
        
        print(count)
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return head.next 