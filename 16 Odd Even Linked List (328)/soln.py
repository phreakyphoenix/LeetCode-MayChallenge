# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
         # Corner case  
        if (head == None):  
            return None
        
        # Initialize first nodes of  
        # even and odd lists  
        odd = head  
        even = head.next
        # Remember the first node of even list so  
        # that we can connect the even list at the  
        # end of odd list.  
        evenFirst = even  
        
        while 1:  
              
            # If there are no more nodes,  
            # then connect first node of even  
            # list to the last node of odd list  
            if (odd is None or even is None or even.next is None:  
                odd.next = evenFirst  
                break
            
            # Connecting odd nodes  
            odd.next = even.next
            odd = even.next
            
            # If there are NO more even nodes  
            # after current odd.  
            if (odd.next == None):  
                even.next = None
                odd.next = evenFirst  
                break
            
            #Connecting even nodes  
            even.next = odd.next
            even = odd.next
        return head 