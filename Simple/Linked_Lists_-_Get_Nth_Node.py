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

linked_list = Node(1, Node(2, Node(3, None)))
test.expect_error("Invalid index value should throw error.", lambda : get_nth(linked_list, 3))
test.expect_error("Invalid index value should throw error.", lambda : get_nth(linked_list, -1))
test.expect_error("Invalid index value should throw error.", lambda : get_nth(linked_list, 100))
test.expect_error("None linked list should throw error.", lambda : get_nth(None, 0))