# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            count = 0
            temp = head
            while temp != None:
                count += 1
                temp = temp.next
            temp = head
            remove_index = count - n
            if remove_index == 0:
                return head.next
            curr = head
            for i in range(count-1):
                if i + 1 == remove_index:
                    curr.next = curr.next.next
                    break
                curr = curr.next
            return head
