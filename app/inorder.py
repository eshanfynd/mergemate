def inorder_traversal(root):
    def traverse(node, result):
        if node:
            traverse(node.left, result)
            result.append(node.value)
            traverse(node.right, result)
    result = []
    traverse(root, result)
    return result
