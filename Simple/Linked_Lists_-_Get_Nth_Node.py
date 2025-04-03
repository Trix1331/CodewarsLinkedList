class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node == None:
        raise ValueError("None linked list")
    counter = 0
    while node != None:
        if index < 0:
            raise ValueError("Invalid index value")
        if counter == index:
            return node
        counter += 1
        node = node.next
    raise ValueError("Index out of range")