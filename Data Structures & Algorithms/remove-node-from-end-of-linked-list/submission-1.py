# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nexti = curr.next
            curr.next = prev
            prev = curr
            curr = nexti

        temp = prev

        if n == 1:
            prev = temp.next
            curr1 = prev
            rev = None

            while curr1:
                nextN = curr1.next
                curr1.next = rev
                rev = curr1
                curr1 = nextN
            return rev

            
        c = None
        for i in range(1,n):
            c = temp
            temp = temp.next

        if temp is not None:
            c.next = temp.next

        curr1 = prev
        rev = None

        while curr1:
            nextN = curr1.next
            curr1.next = rev
            rev = curr1
            curr1 = nextN

        return rev

            

        
            
        