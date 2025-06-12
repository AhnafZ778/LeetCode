## The solution itself is actually pretty easy, what's difficult is 
## that you need to make a helper function which I didn't understand 
## initially but yeah basically take the pairs in the entire list and 
## merge them continuously until you run out of pairs basically l1 and l2
## merged into l3 and then as i'm traversing 2 indices at a time
## the l1 and l2 will dissapear and only l3 will be there
## and this process will be rinsed and repeated until there's only
## one list left that's when we break out of the loop and return that 
## head only


# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedlists.append(self.mergelist(l1, l2))
            lists = mergedlists
        return lists[0]

    def mergelist(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
