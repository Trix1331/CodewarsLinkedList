class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
    def __repr__(self):
        return f"Node{self.data, self.next}"

def linked_list_from_string(s):
    lst = s.split(" -> ")[:-1]
    node = None
    while lst:
        node = Node(int(lst.pop()), node)
    return node

head = Node(1, Node(2, Node(3)))
linked_list_from_string("1 -> 2 -> 3 -> None")