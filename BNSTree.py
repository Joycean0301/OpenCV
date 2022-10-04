class BSTNode:
    def __init__(self,key = None):
        self.key = key
        self.left = None
        self.right = None       
    def isEmpty(self):
        return (self.key is None and self.left is None and self.right is None) 
    def clear(self):
        self.key = None
        self.left = None
        self.right = None
    def search(self,x):
        if self.isEmpty():
            return False
        else:
            if self.key == x:
                return True
            elif self.key > x:
                if self.left is None:
                    return False
                else:
                    return self.left.search(x)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.search(x)
    def insert(self,x):
        if self.isEmpty():
            self.key = x
        else:
            if self.key == x:
                return None
            elif self.key > x:
                if self.left is None:
                    self.left = BSTNode(x)
                else:
                    return self.left.insert(x)
            else:
                if self.right is None:
                    self.right = BSTNode(x)
                else:
                    return self.right.insert(x)
    
    def breadth_first_traversal(self):
        queue = [self]
        rs = []
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.key,end = ' ')
            rs.append(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()
        return rs
        
    def preorder(self):
        print(self.key,end = ' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key,end =' ')
        if self.right is not None:
            self.right.inorder()
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.key,end = ' ')
    def delete(self,x):
        if self.key > x:
            if self.left is not None:
                self.left = self.left.delete(x)
        elif self.key < x:
            if self.right is not None:
                self.right = self.right.delete(x)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                node_min = self.right.min()
                self.key = node_min.key
                self.right = self.right.delete(node_min.key)
        return self
    
    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()
    def max(self):
        if self.right is None:
            return self
        else:
            return self.right.max()
    def list_of_tree(self):
        ls_breadth = [self]
        ls_new = [self]
        while True:
            ls_check = []
            for i in ls_new:
                if i.left is not None:
                    ls_check.append(i.left)
                if i.right is not None:
                    ls_check.append(i.right)
            ls_new = ls_check
            ls_breadth = ls_breadth + ls_check
            if len(ls_check)==0:
                break
        return ls_breadth
    def sum(self):
        ls_breadth = self.list_of_tree()
        ls_value = [i.key for i in ls_breadth]
        return sum(ls_value)
    def avg(self):
        ls_breadth = self.list_of_tree()
        ls_value = [i.key for i in ls_breadth]
        return sum(ls_value)/len(ls_value)
    def count(self):
        return len(self.list_of_tree())
    def height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.height() + 1
        elif self.right is None:
            return self.left.height() + 1
        else:
            return max(self.left.height(),self.right.height()) + 1
        
    def isAVL(self):
        ls_tree = self.list_of_tree()[-1::-1]
        for i in ls_tree:
            if i.left is None and i.right is None:
                continue
            elif i.left is None:
                if i.right.height() > 1:
                    return False
            elif i.right is None:
                if i.left.height() > 1:
                    return False
            else:
                if (i.left.height() - i.right.height() > 1) or (i.left.height() - i.right.height() < -1):
                    return False
        return True
    
    
        

if __name__ == '__main__':
    print('Create a tree with first node')
    tree = BSTNode(4)
    print('first key of root node:',tree.key)
    print('tree is Empty? ',tree.isEmpty())
    
    print('Clear tree')
    tree.clear()
    print('After clearing tree')
    print('tree is Empty? ',tree.isEmpty())
    
    ls = [7,2,10,1,5,8,9,3,6,4,7,11]
    print('insert',ls,'into tree')
    for i in ls:
        tree.insert(i)

    print('7 in the tree?',tree.search(7))
    print('13 in the tree?',tree.search(13))
    
    print('tree in breadth-first traverse:',end = ' ')
    tree.breadth_first_traversal()
    print()

    print('tree in preorder:',end = ' ')
    tree.preorder()
    print()
    
    print('tree in inorder:',end = ' ')
    tree.inorder()
    print()
    
    print('tree in postorder:',end = ' ')
    tree.postorder()
    print()
    
    print('The number of nodes in the tree:',tree.count())
    
    print('node with minimum value',tree.min().key,'in the tree is',tree.min())
    print('node with maximum value',tree.max().key,'in the tree is',tree.max())
    
    print('sum of all values in the tree:',tree.sum())
    print('the average of all values in the tree:',tree.avg())
    
    #a = int(input('delete element:'))
    print('delete 5 in tree')
    tree.delete(5)
    print('tree inorder after deleting:',end = ' ')
    tree.inorder()
    print()
    
    print('The height of the tree:',tree.height())
    print('Tree is AVL?', tree.isAVL())
    
    tree1 = BSTNode()
    ls1 = [1,2,4,3,5,1.5,-1,-2]
    for i in ls1:
        tree1.insert(i)
    print('Tree1 is AVL?', tree1.isAVL())
    
    
    