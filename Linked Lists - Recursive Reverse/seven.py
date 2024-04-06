class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous