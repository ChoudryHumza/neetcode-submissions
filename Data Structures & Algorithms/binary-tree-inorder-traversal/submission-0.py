# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def recursion(root):
            if not root:
                return root
        
        
            root.left = recursion(root.left)
            inorder.append(root.val)
            root.right = recursion(root.right)
            return root

        recursion(root)
        return inorder
            
