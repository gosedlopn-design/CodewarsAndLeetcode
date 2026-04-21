from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    
    if node is None:
        return []
    result = []
    q = deque([node])
    current = node
    while q:
        current = q.popleft()
        result.append(current.value)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        
    return result
