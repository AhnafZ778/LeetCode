# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## It's better to use iterative method of solving here 
## other than recursive because it's much simpler since
## in BST we only need to go right or left depending on 
## if the root node val is greater or lesser than both 
## provided node and if it's greater or lesser than only one
## in that case that is the required Ancestor Node

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root =root.left
            else:
                return root
