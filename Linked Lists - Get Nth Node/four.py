def get_nth(node, index):
    counter = 0
    
    if not node.data:
        return ValueError
    elif index < 0:
        raise IndexError
        
    while node != None:
        if counter == index:
            return node
        node = node.next
        counter += 1
    raise ValueError