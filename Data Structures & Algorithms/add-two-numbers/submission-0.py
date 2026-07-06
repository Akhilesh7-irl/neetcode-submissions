# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        cur1 = l1
        cur2 = l2

        tab1 = []
        tab2 =[]

        while cur1 :
            tab1.append(cur1.val)
            
            cur1 = cur1.next
            
        while  cur2:
            
            tab2.append(cur2.val)
            
            cur2 = cur2.next

        n1 = 0
        n2 = 0
        for i in range(len(tab1)):
            n1 += tab1[i]*(10 ** i)
        for i in range(len(tab2)):
            n2 += tab2[i]*(10 ** i)
        
        n = n1+n2
        
       
        n = str(n)
        n = list(n)

        prev = None

        for num in n:
            node = ListNode(int(num))
            node.next = prev
            prev = node

        return prev

            

        

        


