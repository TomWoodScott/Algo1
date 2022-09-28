
'''
Simple example of a linked list

first: Node class

second: LinkedList with method of traversal

third: create a selection of nodes and link them to our LinkedList class

fourth: Set pointers "linking" the nodes
'''




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else: return False

    def delete(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None







family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.insert_new_header("Jim")
#family.traversal()
print(family.search("Bob"))
family.delete()
family.traversal()