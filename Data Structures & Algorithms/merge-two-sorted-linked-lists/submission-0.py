# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Dummy node avoids the egde case of an empty list, so the purpsoe of this is like a dictionary when thee is nothing in it cant add a value/struggles to call a value
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Goal: Create a new linked list
        dummy = node = ListNode()
        #Iterate through the list1 and list2 to ensure that they are not empty
        while list1 and list2: #While they are not empty I think check the rest
            if list1.val < list2.val:
                node.next = list1 #make sure to put the node in that spot since header and node is in same place
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2 # because if either list1 or 2 becomes empty first then the while loop ends but sometimes still other elemetbs to add
        #so then it will add the rest of them to the next node.
        return dummy.next # returns dummy.next because dummy doesnt point to anythinf

        
        #return dummy.next because it is empty
