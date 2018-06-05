class Node(object):
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __repr__(self):
        return str(self.value)


def nth_from_last(head, n):
    if head is None:
        return

    current_node = head
    stack = [current_node]
    while current_node.child:
        current_node = current_node.child
        stack.append(current_node)

    if n > len(stack):
        return
    return stack[len(stack) - n]


def nth_from_last_pointer(head, n):
    p1 = head
    p2 = head
    for _ in range(n):
        if p2 is None:
            return
        p2 = p2.child

    while p2 is not None:
        p1 = p1.child
        p2 = p2.child

    return p1


if __name__ == '__main__':
    current = Node(1)
    for i in range(2, 8):
        current = Node(i, current)
    head = current
    # head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

    current2 = Node(4)
    for i in range(3, 0, -1):
        current2 = Node(i, current2)
    head2 = current2
    # head2 = 1 -> 2 -> 3 -> 4 -> (None)

    assert(nth_from_last(head, 1).value == 1)
    assert(nth_from_last(head, 5).value == 5)
    assert(nth_from_last(head2, 2).value == 3)
    assert(nth_from_last(head2, 4).value == 1)
    assert(nth_from_last(head2, 5) == None)
    assert(nth_from_last(None, 1) == None)

    assert(nth_from_last_pointer(head, 1).value == 1)
    assert(nth_from_last_pointer(head, 5).value == 5)
    assert(nth_from_last_pointer(head2, 2).value == 3)
    assert(nth_from_last_pointer(head2, 4).value == 1)
    assert(nth_from_last_pointer(head2, 5) == None)
    assert(nth_from_last_pointer(None, 1) == None)
