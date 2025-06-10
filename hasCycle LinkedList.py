## First attempt, even though it passes every test case somehow it's wrong 
## logically speaking because my code works on the assumption that no Node
## will have a repeating value which can be wrong in alot of cases.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d1 = {}
        temp = head
        index = -1
        while temp != None:
            d1[temp.val] = d1.get(temp.val, 0) + 1
            if d1[temp.val] > 1:
                index = 1
                break
            temp = temp.next
        if index == 1:
            return True
        else:
            return False
## Okay now the problem is very easily solvable if I use a hashset instead of a dictionary
## to solve it and store the address of the node instead of value in the set
## however it, though runs in the ideal time it takes up O(n) space due to having a 
## set

## Now, there's an incredibly fascinating and fun approach/algorithm to solve this problem
## basically it's called the turtoise and hare algorithm and what this means is we're gonna
## have to pointers in the linked list which slowly traverse the linked list and quickly
## traverses respectively and what the idea is as the loop continues the hare which is moving
## one step faster than the turtoise will eventually catch up to it and when it does we terminate
## the loop, you can see the code and understand how it works, it's quite fun to visualize xD

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
