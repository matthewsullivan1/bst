from asyncio.proactor_events import _ProactorBasePipeTransport


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        '''Number of Nodes in the Tree'''
        self._size = 0
    
    def size(self):
        return self._size

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            self._size += 1
        else:
            self._insert(key, self.root)
            self._size += 1

    
    def _insert(self, key, cur_node):
        if cur_node.value.__lt__(key) or cur_node.value == key:
            if cur_node.right is None:
                cur_node.right = TreeNode(key)
            else:
                self._insert(key, cur_node.right)
        elif cur_node.value.__gt__(key):
            if cur_node.left is None:
                cur_node.left = TreeNode(key)
            else:
                self._insert(key, cur_node.left)
            
    def search(self, key) -> TreeNode:
        if self.root:
            target = self._search(key, self.root)
            if target:
                return target
            else:
                return None
        else:
            return None
            
    def _search(self, data, cur_node):
        if cur_node.value.__lt__(data) and cur_node.right:
            return self._search(data, cur_node.right)
        elif cur_node.value.__gt__(data) and cur_node.left:
            return self._search(data, cur_node.left)
        elif cur_node.value.__eq__(data):
            return cur_node

    def preorder_traversal(self):
        self._preorder(self.root)
    def _preorder(self, node): #preorder helper
        if node:
            print(str(node.value))
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder_traversal(self):
        self._inorder(self.root)
    def _inorder(self,node): #inorder helper
        if node:
            self._inorder(node.left)
            print(str(node.value))
            self._inorder(node.right)

    def postorder_traversal(self):
        self._postorder(self.root)
    def _postorder(self, node): #postorder helper
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.value))

    def getHeight(self):
        return self._getHeight(self.root) 
    
    def _getHeight(self, node): #getHeight helper
        if node is None:
            return 0
        else:
            lst = self._getHeight(node.left)
            rst = self._getHeight(node.right)
            return max(lst, rst) + 1
        
    def level_order_traversal(self) -> list:
        return self._level_order_traversal(self.root)

    def _level_order_traversal(self, root):
        max_height = self._getHeight(root)
        result = []

        for i in range(1, max_height + 1):
            self.getCurrentLevel(root, i, result)
        return result

    def getCurrentLevel(self, root, level, result):
        if root is None:
            return
        if level == 1:
            #print(root.value)
            result.append(root.value)
        elif level > 1 :
            self.getCurrentLevel(root.left , level-1, result)
            self.getCurrentLevel(root.right , level-1, result)

if __name__ == '__main__':
    # Initialize BST.
    bst = BinarySearchTree()

# Test inserting nodes
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

# Test size method.
    assert bst.size() == 7
    assert bst.search(1) == None

# Test inserting additional nodes.
    bst.insert(1)
    bst.insert(6)

    assert bst.size() == 9
    assert bst.search(1).value == 1

# Finally, also test by inserting duplicate values.

# Test level order traversal with duplicates.
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(6)
    bst.insert(1)
    bst.insert(6)

# Test level order traversal.
    assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]




