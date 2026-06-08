class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []


def minimax(node, is_max):
    # Leaf node
    if not node.children:
        return node.val

    scores = [minimax(child, not is_max) for child in node.children]

    if is_max:
        return max(scores)
    else:
        return min(scores)


# Build a sample game tree
root = TreeNode(0, [
    TreeNode(0, [TreeNode(3), TreeNode(5)]),
    TreeNode(0, [TreeNode(2), TreeNode(9)]),
    TreeNode(0, [TreeNode(12), TreeNode(5)])
])

best = minimax(root, True)

print("Best value for MAX player:", best)
