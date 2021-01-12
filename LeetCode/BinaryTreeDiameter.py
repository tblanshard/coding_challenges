# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findDiameter(self, node, diameter):
        if node == None:
            return 0, diameter
        
        leftHeight, diameter = self.findDiameter(node.left, diameter)
        rightHeight, diameter = self.findDiameter(node.right, diameter)
        
        maxDiameter = leftHeight + rightHeight
        
        diameter = max(diameter, maxDiameter)
        
        height = max(leftHeight, rightHeight) + 1
        
        return height, diameter
        
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        height, diameter = self.findDiameter(root, 0)
        return diameter
