"""
Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or memory
buffer, or transmitted across a network connection link to be reconstructed
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is
no restriction on how your serialization/deserialization algorithm should
work. You just need to ensure that a binary tree can be serialized to a
string and this string can be deserialized to the original tree structure.


# Method 1 - DFS approach
class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("#")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "#":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val),
        if self.right:
            self.right.printTree()

import collections
# Method 2 - BFS approach
class Codec:

    def serialize(self, root):
        queue = collections.deque([root])
        result = ["#"]
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)

    def deserialize(self, data):
        if data == "# #":
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Driver Code
tree = TreeNode(1, TreeNode(2, None, TreeNode(4, None, None)), TreeNode(3, None, TreeNode(7, None, None)))
ser = Codec()
deser = Codec()

print(ser.serialize(tree))
ans = deser.deserialize(ser.serialize(tree))
ans.printTree()

