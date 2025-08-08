# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_tree(self, node: Optional[TreeNode]):
        """
        Traverse tree under given node using in-order traversal.
        This is a generator function.
        """
        # if node is None, nothing to traverse
        if node is None:
            return

        # recursively traverse left children
        for val in self.traverse_tree(node.left):
            yield val

        # yield current node's value
        yield node.val

        # recursively traverse right children
        for val in self.traverse_tree(node.right):
            yield val

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse tree to get elements in order
        # and return the kth smallest element
        for i, val in enumerate(self.traverse_tree(root)):
            if i + 1 == k:
                return val
