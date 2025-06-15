# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Here we need a helper valid function to check the values of the left and right
## subtrees, we know in a BST the left subtree can not have any
## value bigger than root while right can't have any less.
## normally checking both sides won't check these cases so we need to 
## pass left boundaries and right boundaries into a helper function
## and update it according to which subtree we're heading to in order
## to make sure the BST is valid

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            elif not (left < node.val and node.val < right):
                return False
            
            return (valid(node.left, left, node.val) and 
            valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
