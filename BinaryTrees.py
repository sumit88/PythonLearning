class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getTempHieght(self, root, currentHieght):
        if root is None:
            return currentHieght
        else:
            leftIncrement = currentHieght + 1 if (root.left is not None) else currentHieght
            rightIncrement = currentHieght + 1 if (root.right is not None) else currentHieght
            return max(self.getTempHieght(root.left, leftIncrement),
                       self.getTempHieght(root.right, rightIncrement))

    def getHeight(self, root):
        return self.getTempHieght(root, 0)


# Write your code here

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
