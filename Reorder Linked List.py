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
## Okay so I could use a fast and slow pointer to find middle as well
## intitially I was unable to figure why but basically as long as the 
## loop continues the fast pointer covers twice as much ground as the slow
## does, so by the time slow will reach the middle the fast will have reached 
## the end and that's a clean way of finding it in one go instead of having to 
## rely on count like I did

## Also the merge segment can be done with a singular while loop 
## as I am considering the second half of the linked list to be 
## bigger than the first half which means I have to travel the second half only

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp1 = slow.next
        slow.next = None
        prev, curr = None, temp1
        while curr:
            te = curr.next
            curr.next = prev
            prev = curr
            curr = te
        temp = head
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
