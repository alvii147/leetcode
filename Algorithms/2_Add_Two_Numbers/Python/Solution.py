# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # carry digit
        carry_digit = 0
        node1 = l1
        node2 = l2

        # top node variable
        SumNode = None
        # previous node variable
        PreviousNode = None

        # keep looping while nodes are not None or carry digit is non-zero
        while node1 != None or node2 != None or carry_digit != 0:
            node1_val = node1.val if node1 != None else 0
            node2_val = node2.val if node2 != None else 0

            # add carry digit and two nodes
            node_addition = carry_digit + node1_val + node2_val
            # set digit to add
            added_digit = node_addition % 10
            # set carry digit
            carry_digit = node_addition // 10

            # create new node with added digit value
            CurrentNode = ListNode(val=added_digit)

            # if previous node is None, set top node variable to current node
            if PreviousNode == None:
                SumNode = CurrentNode
            # else set previous node to point to current node as next
            else:
                PreviousNode.next = CurrentNode

            # set previous node variable to current node
            PreviousNode = CurrentNode

            # if node is not none, set it to the next node
            if node1 != None:
                node1 = node1.next

            if node2 != None:
                node2 = node2.next

        return SumNode
