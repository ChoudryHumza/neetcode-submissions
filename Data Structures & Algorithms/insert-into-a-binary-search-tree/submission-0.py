# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        return self.recursion(root, val)

    def recursion(self, root, val):
        node = TreeNode(val)
        R = root
        if not root:
            root = node
            return root
        else:

            while True:
                if val < R.val:
                    if R.left == None:
                        R.left = node
                        return root
                    else:
                        R = R.left
                elif val > R.val:
                    if R.right == None:
                        R.right = node
                        return root
                    else:
                        R = R.right
            
            


