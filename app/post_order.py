def postorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
    traverse(root)
    return result

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
