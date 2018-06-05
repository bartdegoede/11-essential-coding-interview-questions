class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


def is_bst(node, lower_limit=None, upper_limit=None):
    if lower_limit is not None and node.value < lower_limit:
        return False
    if upper_limit is not None and node.value > upper_limit:
        return False

    is_left_bst = True
    is_right_bst = True
    if node.left:
        is_left_bst = is_bst(node.left, lower_limit=lower_limit, upper_limit=node.value)
    if is_left_bst and node.right:
        is_right_bst = is_bst(node.right, lower_limit=node.value, upper_limit=upper_limit)

    return is_left_bst and is_right_bst


if __name__ == '__main__':
    mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
    mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
    mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
    mapping4 = {3: [1, 5], 1: [0, 4]}

    head1 = create_tree(mapping1, 0)
    head2 = create_tree(mapping2, 3)
    head3 = create_tree(mapping3, 3)
    head4 = create_tree(mapping4, 3)

    assert(is_bst(head1) == False)
    assert(is_bst(head2) == False)
    assert(is_bst(head3) == True)
    assert(is_bst(head4) == False)
