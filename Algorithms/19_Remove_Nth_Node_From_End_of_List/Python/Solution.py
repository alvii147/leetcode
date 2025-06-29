# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Find the nth node from the end of the linked list.
        '''
        # start with the head and advance n - 1 times
        node = head
        for i in range(n - 1):
            node = node.next
            if node is None:
                return None

        # now keep advancing till the end while maintaining another node pointer from the head
        # once the right node pointer reaches the end, the left node pointer will reach the nth node
        nthNode = head
        while node.next is not None:
            node = node.next
            nthNode = nthNode.next

        return nthNode

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the node to the left of the nth node from the end
        nPlusOnethNode = self.findNthFromEnd(head, n + 1)
        # if node not found, this means n is the number of linked list elements
        # so we can just remove the head
        if nPlusOnethNode is None:
            return head.next

        # otherwise, skip the nth node
        nPlusOnethNode.next = nPlusOnethNode.next.next

        return head
