# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first node in group 1
        group_head_1 = None
        # first node in group 2
        group_head_2 = None

        # current node
        curr_node = head
        # previous node
        prev_node = None

        # if k is 1, return unmodified list
        if k == 1:
            return head

        i = 0
        while curr_node is not None:
            # if at the end of first group, set new head to current node
            if i == k - 1:
                new_head = curr_node

            # if at the start of new group
            if i % k == 0:
                # shift over group heads with current node
                group_head_1 = group_head_2
                group_head_2 = curr_node

                # set current node to point to None, update current and previous nodes
                next_node = curr_node.next
                curr_node.next = None
                prev_node = curr_node
                curr_node = next_node
            else:
                # if at the end of group
                if i % k == k - 1:
                    # make group 1 head point to current node
                    if group_head_1 is not None:
                        group_head_1.next = curr_node

                # reverse nodes, update current and previous nodes
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node

            i += 1

        # if last elements have been reversed
        if i % k != 0:
            # current node
            curr_node = prev_node
            # previous node
            prev_node = None

            j = 0
            while j < i % k:
                # reverse nodes, update current and previous nodes
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node

                j += 1

            # make group 1 head point to previous node
            group_head_1.next = prev_node

        return new_head