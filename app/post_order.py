def postorder_traversal(root):
    def traverse(node):
        if node is None:
            return []
        return traverse(node.left) + traverse(node.right) + [node.value]
    return traverse(root)

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
