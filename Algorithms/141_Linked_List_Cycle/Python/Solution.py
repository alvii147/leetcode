# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if there are no elements in the linked list, there is no cycle
        if head is None:
            return False

        # tortoise is the slow pointer
        tortoise = head
        # hare is the fast pointer
        hare = head.next

        # if we ever reach the tail, break loop as there is no cycle
        while tortoise is not None and hare is not None and hare.next is not None:
            # if tortoise and hare meet, there is a cycle
            if tortoise == hare or tortoise == hare.next:
                return True

            # advance tortoise and hare pointers
            hare = hare.next.next
            tortoise = tortoise.next

        return False
