def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    traverse(root)
    return result
