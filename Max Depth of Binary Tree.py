## Holy shit I'm absolutely cracked at binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        return max(l,r)
