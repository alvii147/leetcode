from io import StringIO

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    A binary tree node is serialized as follows:

    [NODE VALUE]l[LEFT NODE]r[RIGHT NODE]

    If the left and right nodes are empty, they are represented as empty strings.

    For example, the following binary tree:

        1
       /  \
      2    3
     /    / \
    4    5   6

    is serialized as follows:

    1l2l4lrrr3l5lrr6lr
    """
    def serialize_helper(self, node: TreeNode | None, stream: StringIO):
        """
        Serialize given node and its children nodes into given string IO stream.
        """
        if node is None:
            return

        # serialize current node
        stream.write(str(node.val))

        # serialize left node
        stream.write('l')
        if node.left is not None:
            self.serialize_helper(node.left, stream)

        # serialize right node
        stream.write('r')
        if node.right is not None:
            self.serialize_helper(node.right, stream)

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # create string IO stream for efficient string building
        stream = StringIO()
        # serialize root node
        self.serialize_helper(root, stream)

        return stream.getvalue()

    def deserialize_helper(self, data: str, idx: int) -> tuple[TreeNode | None, int]:
        """
        Deserialize given string starting from given index,
        return the deserialized node and the ending index.
        """
        l_idx = -1
        r_idx = -1

        # find locations of first 'l' and 'r' directives
        for i in range(idx, len(data)):
            if l_idx == -1 and data[i] == 'l':
                l_idx = i

            if r_idx == -1 and data[i] == 'r':
                r_idx = i

            if l_idx >= 0 and r_idx >= 0:
                break

        # if no 'l' is found, or if 'r' appears first
        # then the current node is an empty string
        # meaning it's an empty node
        if l_idx == -1 or r_idx < l_idx:
            return None, idx

        # parse value of current node
        node = TreeNode(int(data[idx:l_idx]))

        # deserialize left node
        idx = l_idx + 1
        node.left, idx = self.deserialize_helper(data, idx)

        # deserialize right node
        idx += 1
        node.right, idx = self.deserialize_helper(data, idx)

        return node, idx

    def deserialize(self, data) -> TreeNode | None:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root, _ = self.deserialize_helper(data, 0)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
