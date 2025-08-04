from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areSubtreesEqual(self, subRoot1: TreeNode | None, subRoot2: TreeNode | None) -> bool:
        """
        Check if two sub trees are equal.
        """
        # if both are null, they are equal
        if subRoot1 is None and subRoot2 is None:
            return True

        # if only one of them is none, they are not equal
        if subRoot1 is None or subRoot2 is None:
            return False

        # if their values are different, they are not equal
        if subRoot1.val != subRoot2.val:
            return False

        # if their left sub trees are not equal, they are not equal
        if not self.areSubtreesEqual(subRoot1.left, subRoot2.left):
            return False

        # if their right sub trees are not equal, they are not equal
        if not self.areSubtreesEqual(subRoot1.right, subRoot2.right):
            return False

        # otherwise, they are equal
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # set up queue of nodes, starting with root
        queue = deque([root])

        while len(queue) > 0:
            # pop from queue
            node = queue.popleft()
            # check if current node is equal to sub tree
            if self.areSubtreesEqual(node, subRoot):
                return True

            # add left and right children to queue if available
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)

        # if queue is exhaused, no equal sub tree was found
        return False
