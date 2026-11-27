# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ##
        count = 0
        val = 0
        def recursion(root):
            nonlocal count, val
            if not root:
                return None
            
            recursion(root.left)
            count += 1
            if count == k:
                val = root.val
            recursion(root.right)

        recursion(root)
        return val
        

