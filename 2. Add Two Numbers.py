# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ls =  ListNode(-1)
        
        l3 = ls
        curr_sum = 0
        
        while l1 is not None or l2 is not None:
           
            if l1 is not None:
                curr_sum += l1.val
                l1 = l1.next
            
            if l2 is not None:
                curr_sum += l2.val
                l2 = l2.next
                
            digit = curr_sum % 10
            l3.next = ListNode(digit)
            l3 = l3.next
            curr_sum //= 10
            
        if curr_sum != 0:
            digit = curr_sum
            l3.next = ListNode(digit)
        
        lr = ls.next
        ls = None

        return lr
        
