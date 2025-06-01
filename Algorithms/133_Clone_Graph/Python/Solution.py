"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def __init__(self):
        # dictionary mapping node value to already cloned nodes
        self.clonedNodes = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # if node has already been cloned, return it
        if node.val in self.clonedNodes:
            return self.clonedNodes[node.val]

        # clone current node without neighbors
        # we'll add neighbors later
        clonedNode = Node(val=node.val)
        # store cloned node so we don't clone it again
        self.clonedNodes[clonedNode.val] = clonedNode

        # iterate over neighbors, clone recursively, and add to current node's neighbors
        for neighbor in node.neighbors:
            clonedNode.neighbors.append(self.cloneGraph(neighbor))

        return clonedNode
