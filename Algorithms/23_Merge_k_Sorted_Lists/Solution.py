import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myheap = []
        # add values from head node to list
        for node in lists:
            if node is not None:
                myheap.append(node.val)

        # heapify created list
        heapq.heapify(myheap)

        # for getting return node first time
        first = True
        # previous node
        prevNode = None
        # head of node of sorted linked list
        sortedNode = None
        # loop till heap is empty
        while len(myheap) > 0:
            # pop min value
            minVal = heapq.heappop(myheap)
            # create new node with minimum value
            currentNode = ListNode(val=minVal)
            if first:
                # get return node first time
                sortedNode = currentNode
                first = False

            if prevNode is not None:
                # make previous node point to current node
                prevNode.next = currentNode
            # set current node as previous
            prevNode = currentNode

            # iterate over head nodes of sorted lists
            for nodeIdx in range(len(lists)):
                if lists[nodeIdx] is not None and lists[nodeIdx].val == minVal:
                    # if min value is found, make head point to next element in sorted list
                    lists[nodeIdx] = lists[nodeIdx].next

                    if lists[nodeIdx] is not None:
                        # push new value of node to heap
                        heapq.heappush(myheap, lists[nodeIdx].val)

                    break

        return sortedNode