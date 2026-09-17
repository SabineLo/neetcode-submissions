# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Goal: We want to reverse the list instead of it being null -> 1 -> 2 -> 3 -> null
        #In order to do that wwe need two pointers/ BUT WHY? -> explain this we are destroying the connect between the prev curr, and we are switching them
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            #So why are we swapping prev curr? Because we are going down the list and destroying the current links and swapping them to connect to different sections
        return prev

