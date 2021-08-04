"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

Solution: O(N) Time and O(Height) Space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def get_sum(root, ans, target, res):
            if root is None:
                return res
            
            # Appending the root value to arr
            ans.append(root.val)
            
            # If root is leaf node, print the path
            if root.left is None and root.right is None:
                if sum(ans) == target:
                    #print(ans, target)
                    res.append(list(ans))
                    
            
            # Recur on the LST
            get_sum(root.left, ans, target, res)
            # Recur on the RST
            get_sum(root.right, ans, target, res)
            
            # Pop off the last element, as we are changing the subtrees
            ans.pop()
            
         
        res = []
        get_sum(root, [], targetSum, res)
        return res
        
