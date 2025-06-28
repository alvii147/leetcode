# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        # use Floyd's tortoise and hare method to find mid point
        tortoise = head
        hare = head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next

        # reverse the second half of the list
        prevNode = None
        node = tortoise.next
        tortoise.next = None
        while node is not None:
            nextNode = node.next
            node.next = prevNode
            prevNode, node = node, nextNode

        # merge the first and second halves
        tail = prevNode
        while tail is not None:
            nextHead = head.next
            nextTail = tail.next
            head.next = tail
            tail.next = nextHead
            head, tail = nextHead, nextTail
