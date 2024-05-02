def binary_tree_to_dict(tree):
    if isinstance(tree, list):
        operator = tree[1]
        if isinstance(tree[0], int):
            left = binary_tree_to_dict(str(tree[0]))
        else:
            left = binary_tree_to_dict(tree[0])
            
        if isinstance(tree[2], int):
            right = binary_tree_to_dict(str(tree[2]))
        else:
            right = binary_tree_to_dict(tree[2])
        
        return {
            "left": binary_tree_to_dict(left),
            "operator": operator,
            "right": binary_tree_to_dict(right)
        }
    else:
        return tree
# Example usage
binary_tree = [1, "+", [5, "*", 0]]
result = binary_tree_to_dict(binary_tree)
print(result)