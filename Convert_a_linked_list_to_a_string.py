def stringify(node):
    result = ''
    if node == None:
        return 'None'
    while node != None:
        result += str(node.data) + ' -> '
        node = node.next
    result += 'None'
    return result