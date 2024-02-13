class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put(key, self.root, value)
    
    def _put(self, key, cur_node, value):
        if cur_node.key < key:
            if cur_node.right is None:
                cur_node.right = TreeNode(key, value)
            else:
                self._put(key, cur_node.right, value)
        elif cur_node.key > key:
            if cur_node.left is None:
                cur_node.left = TreeNode(key, value)
            else:
                self._put(key, cur_node.left, value)
        elif cur_node.key == key:
            cur_node.value = value
            
    def get(self, key) -> TreeNode:
        if self.root:
            target = self._get(key, self.root)
            if target:
                return target
            else:
                return None
        else:
            return None
            
    def _get(self, key, cur_node):
        if cur_node.key < key and cur_node.right:
            return self._get(key, cur_node.right)
        elif cur_node.key > key and cur_node.left:
            return self._get(key, cur_node.left)
        elif cur_node.key == key:
            return cur_node.value

if __name__ == '__main__':
# Create a TreeMap
    tree_map = TreeMap()

# Test putting and getting key-value pairs.
    tree_map.put(3, "A")
    tree_map.put(1, "B")
    tree_map.put(2, "C")
    tree_map.put(4, "D")

    assert tree_map.get(2) == "C"
    assert tree_map.get(1) == "B"
    assert tree_map.get(4) == "D"
# Non-existent key should return None.
    assert tree_map.get(5) is None
  