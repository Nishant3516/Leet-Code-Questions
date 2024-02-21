# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorderTraversal(root, result)
        return result
    
    def _inorderTraversal(self, node, result):
        if node:
            # Traverse the left subtree
            self._inorderTraversal(node.left, result)
            # Visit the current node
            result.append(node.val)
            # Traverse the right subtree
            self._inorderTraversal(node.right, result)