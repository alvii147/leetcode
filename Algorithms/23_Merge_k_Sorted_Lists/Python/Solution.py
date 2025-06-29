import heapq

class ComparableListNode:
    '''
    Wrapper around ListNode that implements comparison methods.
    '''
    def __init__(self, node: ListNode):
        self.node = node

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{type(self).__name__}({self.node.val})'

    def __eq__(self):
        return self.node.val == other.node.val

    def __eq__(self):
        return self.node.val != other.node.val

    def __lt__(self, other: ListNode) -> bool:
        return self.node.val < other.node.val

    def __gt__(self, other: ListNode) -> bool:
        return self.node.val > other.node.val

    def __le__(self, other: ListNode) -> bool:
        return self.node.val <= other.node.val

    def __ge__(self, other: ListNode) -> bool:
        return self.node.val >= other.node.val

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initialize heap with ListNode instances wrapped in ComparableListNode
        heap = []
        for headNode in lists:
            if headNode is None:
                continue

            heap.append(ComparableListNode(node=headNode))

        heapq.heapify(heap)

        # create a dummy node to avoid handling edge case of assigning a head node on first iteration
        dummyNode = ListNode()
        # pointer of tail node of sorted list
        tail = dummyNode

        # keep merging into sorted list until heap is empty
        while len(heap) > 0:
            # pop node with lowest value from heap
            minCmpNode = heapq.heappop(heap)
            # make tail of sorted list point to node with lowest value
            tail.next = minCmpNode.node
            # advance tail of sorted list to node with lowest value
            tail = tail.next

            if minCmpNode.node.next is not None:
                # if node with lowest value is not terminal node
                # then advance it and push it to heap
                minCmpNode.node = minCmpNode.node.next
                heapq.heappush(heap, minCmpNode)

        return dummyNode.next
