class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data) + " -> " + str(self.next)

def remove_duplicates(head):
    if head is None:
        return None
    if head.next is None:
        return head

    # set_nodes = set()
    # while head != None:
    #     set_nodes.add(head.data)
    #     head = head.next
    # set_nodes = sorted(set_nodes)
    # set_nodes.append(None)

    # current_node = Node(set_nodes[0])

    # while current_node is not None:
    #     current_node.next = Node(set_nodes[1])
    #     current_node = current_node.next
    #     set_nodes.pop(0)
    # current_node.next = None
    # return current_node
    # new_head = Node(set_nodes[0])
    # current_node = new_head

    # for value in set_nodes[1:]:
    #     current_node.next = Node(value)
    #     current_node = current_node.next

    # return new_head
    unique_values = set()
    dummy = Node(0)
    current = dummy

    while head:
        if head.data not in unique_values:
            unique_values.add(head.data)
            current.next = Node(head.data)
            current = current.next
        head = head.next

    return dummy.next
