class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head == None:
        raise Exception("Cannot split an empty list")
    if head.next == None:
        raise Exception("Cannot split a list of 1")
    nodes = Context(head, head.next)
    p1 = head
    p2 = head.next
    
    while p2 != None:
        p1.next = p2.next
        p1 = p2.next
        if p1 != None:
            p2.next = p1.next
            p2 = p1.next
        else:
            return nodes
        
    return nodes