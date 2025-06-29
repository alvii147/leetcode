# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to avoid handling edge case of assigning a head node on first iteration
        dummyNode = ListNode()
        # pointer of tail node of sorted list
        tail = dummyNode

        while list1 is not None and list2 is not None:
            # take lower value from heads of two lists
            # connect tail to head of that list
            # advance head of that list
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # advance tail of sorted list
            tail = tail.next

        # if either list is exhausted, connect the other list to tail
        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1

        # return the head, i.e. what the dummy node is pointing to
        return dummyNode.next
