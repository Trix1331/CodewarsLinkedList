class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source:Node, dest:Node) -> Context:
    if source is None:
        raise ValueError("Source linked list is None")
    head = source.data
    source = source.next
    dest_first = Node(head)
    dest_first.next = dest
    return Context(source, dest_first)
