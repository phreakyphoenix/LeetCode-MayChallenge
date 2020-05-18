
            res.val += l1.val + l2.val
            print (res.val)
            if flag := res.val>9:
                res.val%=10
                
            l1 = l1.next
            l2 = l2.next
            if not (l1 or l2):
                if flag:
                    res.next = ListNode(val = 1)
                return top
            
            if not l1 and l2:
                res.next = ListNode(val = flag+l2.val)
                res.next.next = l2.next
                return top
            elif not l2 and l1:
                res.next = ListNode(val = flag+l1.val)
                res.next.next = l1.next
                break
            
            res.next = ListNode(val = flag)
            res=res.next
        return top