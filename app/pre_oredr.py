def preorder_traversal(root):
    result = []
    if root:
        result.append(root.value)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result
