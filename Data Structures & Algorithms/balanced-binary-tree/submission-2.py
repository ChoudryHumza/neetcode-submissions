class UnbalancedTree(Exception):
    pass

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                raise UnbalancedTree

            return 1 + max(left, right)

        try:
            dfs(root)
            return True
        except UnbalancedTree:
            return False