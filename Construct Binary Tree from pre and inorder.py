# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## This rattled my brain a bit as I wasn't familiar with in-order and
## pre- order traversal much, but pre-order always has root at 0th index
## while in-order always has left sub tree to the left of the position of the root node 
## and right sub to the right, so we find the root in the in-order array and then we 
## create the left and right subtrees in the similar fashion by shortening the in-order
## and pre-order and passing the right and left sub trees respectively

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1: ])
        return root
