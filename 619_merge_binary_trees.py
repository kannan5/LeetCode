
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def merge_trees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.merge_trees(t1.left, t2.left)
            root.right = self.merge_trees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

    def print_tree(self, tree):
        print(tree.val)
        if self.tree.left:
            self.print_tree(tree.left)
        if self.tree.right:
            self.print_tree(tree.right)


if __name__ == '__main__':
    t1 = TreeNode(3)
    t1.left = TreeNode(2, 1, 5)
    t1.right = TreeNode(6, 5, 8)
    t2 = TreeNode(6)
    t2.left = TreeNode(3, 2, 5)
    t2.right = TreeNode(8, 7, 9)
    a = Solution()
    a.merge_trees(t1, t2)
    a.print_tree(t2)
