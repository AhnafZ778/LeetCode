## Got it done after a few hiccups here and there 
## but the concept was pretty straight forward it's just janky
## and weird to visualize or I haven't mastered it completely yet
## It has the optimal space and time complexity but it's
## overcomplicated and not that readable so gonna try to revise it
## and make it readable

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        count = 0
      # Finding total length
        while temp != None:
            count += 1
            temp = temp.next
      # Finding middle Node
        temp = head
        count2 = 0
        while count2 < (count//2)-1:
            count2 += 1
            temp = temp.next
        temp1 = temp.next

      # Reversing the right end of the List
        temp.next = None
        prev, curr = None, temp1
        while curr:
            te = curr.next
            curr.next = prev
            prev = curr
            curr = te
        temp = head

      # Basic List merge
        while prev and temp:
            te = temp.next
            temp.next = prev
            temp = temp.next
            prev = prev.next
            temp.next = te
            temp = temp.next
        temp = head
        while temp.next:
            temp = temp.next
        if prev:
            temp.next = prev
        return
