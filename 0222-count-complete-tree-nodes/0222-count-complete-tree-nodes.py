# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        def nodeExists(index, depth, node):
            left, right = 0, (1 << (depth - 1)) - 1
            for _ in range(depth - 1):
                mid = (left + right) // 2
                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        depth = getDepth(root)
        if depth == 0:
            return 0
        
        left, right = 0, (1 << (depth - 1)) - 1
        while left <= right:
            mid = (left + right) // 2
            if nodeExists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return (1 << (depth - 1)) - 1 + right + 1