class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            
            # Update global max with path passing through current node
            res[0] = max(res[0], node.val + leftMax + rightMax)
            
            # Return max sum extending to parent
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]