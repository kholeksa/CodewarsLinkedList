def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head