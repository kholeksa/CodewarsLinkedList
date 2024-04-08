from preloaded import Node

def swap_pairs(head):
    if not(head is None or head.next is None):
        temp = head.next
        head.next = swap_pairs(head.next.next)
        temp.next = head
        return temp
    return head