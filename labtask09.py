
# Q1: Write a function to check if a binary tree is a BST using only traversals.


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def is_bst(root, prev=[None]):
    if not root:
        return True

    if not is_bst(root.left, prev):
        return False

    if prev[0] is not None and root.val <= prev[0].val:
        return False

    prev[0] = root

    return is_bst(root.right, prev)


# Q2: Implement a function to convert a sorted array into a balanced BST.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])

    return root

# Q3: Implement a function to create a complete binary tree from a given array.


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def array_to_complete_binary_tree(arr):
    n = len(arr)
    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while i < n:
        current = queue.pop(0)

        left_val = arr[i]
        i += 1
        if left_val is not None:
            current.left = TreeNode(left_val)
            queue.append(current.left)

        if i < n:
            right_val = arr[i]
            i += 1
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)

    return root


#  Q4: Write a function to perform a level order traversal of a binary tree.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def level_order_traversal(root):
    result = []
    if not root:
        return result

    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


# Q5: Create a function to construct an expression tree from a given postfix expression.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def construct_expression_tree(postfix):
    stack = []

    for char in postfix:
        if char.isalnum():
            stack.append(TreeNode(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            root = TreeNode(char)
            root.left = operand1
            root.right = operand2
            stack.append(root)

    return stack[0]
