# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#returning a boolean 
#if there is a cycle there is an index? how many cycles there are any a linked list
#if index == -1 return false
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visitedNode = set()
        #Iterate throught the entire list if the curr.next = -1 return false 
        #so if it starts repeating then u will have to realize it dont work 
        while curr != None:
            if curr in visitedNode:
                return True
            visitedNode.add(curr)
            curr = curr.next
        return False