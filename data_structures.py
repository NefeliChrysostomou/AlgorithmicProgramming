# Singly Linked List Node
class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Doubly Linked List Node
class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __iter__(self):
        # much easier to trasverse the list using a generator
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.count
    
    def __getitem__(self, index):
        """Retrieve an item by index, returns None if out of bounds."""
        if 0 <= index < self.count:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data
        return None

    def add(self, item):
        new_node = SinglyListNode(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def get_by_attribute(self, attribute_name, value):
        current = self.head
        while current:
            if hasattr(current.data, attribute_name) and getattr(current.data, attribute_name) == value:
                return current.data
            current = current.next
        return None

    def remove_by_attribute(self, attribute_name, value):
        if not self.head:
            return False  # Empty list
        
        # Check the head node first
        if hasattr(self.head.data, attribute_name) and getattr(self.head.data, attribute_name) == value:
            self.head = self.head.next
            self.count -= 1
            if not self.head:
                self.tail = None  # If the list is now empty
            return True
        
        # Traverse the list to find the node to remove
        current = self.head
        while current and current.next:
            if hasattr(current.next.data, attribute_name) and getattr(current.next.data, attribute_name) == value:
                current.next = current.next.next
                self.count -= 1
                if not current.next:  # If we removed the tail
                    self.tail = current
                return True
            current = current.next
        
        return False  # Node with the specified attribute and value not found

    def get_all(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

    def get_size(self):
        return self.count

# Doubly Linked List
class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def add(self, item):
        new_node = DoublyListNode(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def remove_by_attribute(self, attribute_name, value):
        if not self.head:
            return False
        if hasattr(self.head.data, attribute_name) and getattr(self.head.data, attribute_name) == value:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.count -= 1
            return True
        current = self.head
        while current:
            if hasattr(current.data, attribute_name) and getattr(current.data, attribute_name) == value:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.count -= 1
                return True
            current = current.next
        return False

    def get_reverse(self):
        items = []
        current = self.tail
        while current:
            items.append(current.data)
            current = current.prev
        return items


# Trees


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Regular Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_generator(self, node=None):
        if node is None:
            node = self.root  # Start at root if first call
        yield node.data
        if node.left:
            yield from self.preorder_generator(node.left)
        if node.right:
            yield from self.preorder_generator(node.right)

    def inorder_generator(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            yield from self.inorder_generator(node.left)
        yield node.data
        if node.right:
            yield from self.inorder_generator(node.right)

    def postorder_generator(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            yield from self.postorder_generator(node.left)
        if node.right:
            yield from self.postorder_generator(node.right)
        yield node.data

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if current.left is None:
            current.left = TreeNode(data)
        elif current.right is None:
            current.right = TreeNode(data)
        else:
            # You can choose how to insert when both left and right are filled
            self._insert(current.left, data)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            if node.left:
                self.inorder(node.left)
            print(node.data, end=" ")
            if node.right:
                self.inorder(node.right)

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            print(node.data, end=" ")
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.data, end=" ")

# Binary Search Tree (BST) (no self-balancing)
class BST(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left:
                self._insert(current.left, data)
            else:
                current.left = TreeNode(data)
        elif data > current.data:
            if current.right:
                self._insert(current.right, data)
            else:
                current.right = TreeNode(data)

    def search(self, target):
        return self._search(self.root, target)

    def _search(self, node, target):
        if not node:
            return None  # Not found
        if node.data == target:
            return node
        elif node.data > target:
            return self._search(node.left, target)
        else:
            return self._search(node.right, target)

# Dynamic Array

class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.array = [None] * initial_capacity # imitating a static, non-resizable c-style array (python does not have these)
        self.size = 0
        self.capacity = initial_capacity

    def __iter__(self):
        for i in range(self.size):
            yield self.get(i)

    def __len__(self):
        return self.get_size()
    
    def __getitem__(self, index):
        """Retrieve an item by index, returns None if out of bounds."""
        for i in range(self.size):
            if i == index:
                return self.array[i]

    def add(self, item):
        """Add an item to the array. Resizes if needed."""
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
        
        self.array[self.size] = item
        self.size += 1

    def _resize(self, new_capacity):
        """Resize the internal array to the new capacity."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def get(self, index):
        """Retrieve an item by index, returns None if out of bounds."""
        if 0 <= index < self.size:
            return self.array[index]
        return None

    def remove(self, item):
        """Remove the item from the array and shift elements."""
        for i in range(self.size):
            if self.array[i] == item:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]

                self.array[self.size - 1] = None
                self.size -= 1

                # Resize if too empty
                if self.size < self.capacity // 4 and self.capacity > 10:
                    self._resize(self.capacity // 2)

                return True
        return False

    def get_size(self):
        """Return the number of elements in the array."""
        return self.size

    def get_all(self):
        """Return a list of all non-None elements in the array."""
        return [self.array[i] for i in range(self.size) if self.array[i]]

    def __str__(self):
        """Return a string representation of the array."""
        return str([self.array[i] for i in range(self.size)])
