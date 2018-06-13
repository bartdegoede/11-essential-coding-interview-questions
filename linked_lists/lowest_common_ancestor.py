class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # Overriding the equality operator.
    # This will be used for testing your solution.
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False


def path_to_x(node, x):
    if node is None:
        return
    if node.value == x:
        return [node]

    l = path_to_x(node.left, x)
    if l:
        l.insert(0,node)
        return l
    r = path_to_x(node.right, x)
    if r:
        r.insert(0, node)
        return r

def lca(root, j, k):
    j_path = path_to_x(root, j)
    k_path = path_to_x(root, k)
    if j_path and k_path:
        i = 0
        while i < len(j_path) and i < len(k_path) and j_path[i] == k_path[i]:
            i += 1
        return j_path[i-1].value


# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
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


if __name__ == '__main__':
    # {0: [1, 2]} means that 0's left child is 1, and its right
    # child is 2.
    mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
    head1 = create_tree(mapping1, 0)
    # This tree is:
    # head1 = 0
    #        / \
    #       1   2
    #      /\   /\
    #     3  4 5  6


    mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
    head2 = create_tree(mapping2, 5)
    # This tree is:
    #  head2 = 5
    #        /   \
    #       1     4
    #      /\    / \
    #     3  8  9  2
    #    /\
    #   6  7


    assert(lca(head1, 1, 5) == 0)
    assert(lca(head1, 3, 1) == 1)
    assert(lca(head1, 1, 4) == 1)
    assert(lca(head1, 0, 5) == 0)
    assert(lca(head2, 4, 7) == 5)
    assert(lca(head2, 3, 3) == 3)
    assert(lca(head2, 8, 7) == 1)
    assert(lca(head2, 3, 0) == None)
