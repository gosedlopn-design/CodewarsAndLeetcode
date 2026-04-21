# Pre-order traversal
def pre_order(node):
    result = []
    if node is None:
        return result
    stack = [node]
    current = node
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        
    return result

# In-order traversal
def in_order(node):
    result = []
    if node is None:
        return result
    stack = []
    current = node
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.data)
            current = current.right
    return result

# Post-order traversal
def post_order(node):
    result = []
    if node is None:
        return result
    stack = [node]
    current = node
    while stack:
        current = stack.pop()
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
        
        result.append(current.data)
        
    return result[::-1]

