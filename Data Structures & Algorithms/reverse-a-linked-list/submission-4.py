# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #We have prev,curr,curr.next, ...
    # 1 -> 2 -> 3 -> null
    # None<- 1 <- 2 <- 3
    # prev None
    #
    # temp = curr.next
    # curr.next = prev // None
    # prev = curr 
    # curr = temp
        prev = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp
        return prev