# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #Explain the purpose of dummy porperly
        curr = dummy
        carry = 0
        #9 
        #1
        #So my plan is that I am going to create a new list/or nodes kinda because im changing the values
        #I am adding the first two nodes from both list together and then putting them in the new list and retuning
        #the new list
        #Im creating a new list because I dont want to change the original values
        #So its addition with remainders
        #321+541 = 762 9+9 = 18//10 = 1 while 18%10 = 8  and  but we are carrying out 1 and we put it in next place 
        #how do we add the 1 in the next place I am assuming thats why we do the if else statments
        while l1 or l2 or carry: #this is or? so the carry then becomes the new val in the next iteration, so as long as one is true keep going which is why its carry
            #What I got wrong was the carrying and if statments? idk why they are there
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total//10
            value = total % 10
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None# when we do if statements for here for the next iteration setting ut to none in the problem does that signnify that it = 0?
        return dummy.next
