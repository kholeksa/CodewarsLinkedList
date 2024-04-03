def linked_list_from_string(s):
    node = None
    for i in reversed(s.split(' -> ')):
        if i != 'None':
            node = Node(int(i), node)
    return node