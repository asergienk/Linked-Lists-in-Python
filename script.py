class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):

        curr = self.head

        if curr and curr.data==key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr and curr.data!=key:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None



llist = LinkedList()
llist.append("a")
llist.append("b")
llist.append("c")
llist.prepend("d")
llist.delete_node("c")
llist.insert_after_node(llist.head.next, "e")
llist.print_list()      
