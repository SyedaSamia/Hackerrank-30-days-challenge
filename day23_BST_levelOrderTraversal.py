class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root:
            q = []
            q.append(root)
            while(len(q)>0):
                print(q[0].data,end = ' ')
                tempNode = q.pop(0)
                if tempNode.left:
                    q.append(tempNode.left)
                if tempNode.right:
                    q.append(tempNode.right)
        else:
            return 0
        #Write your code here
if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    myTree.levelOrder(root)