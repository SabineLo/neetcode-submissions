# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head #I understand now go as faar right as possible with the index if I reach end of list
        #We use left one to keep the count and delete the corresponding one
        #For example in Ex 2: we have [1,2] n =2 it would have been 1 getting deleted
        while n > 0: #shouldnt be taht should be while n <1but then it will keep going
            n-=1
            right = right.next #how does this work?
        
        while right:
            left = left.next
            right = right.next #still a bit confused need to watch the vid explaination

        left.next = left.next.next #fixing the aftermath reconnecting it

        return dummy.next
        
