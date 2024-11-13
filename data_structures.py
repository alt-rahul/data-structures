# here we are creating LinkedLists 
class Node():
    def __init__(self, data):
        self.head = data
        self.next = None

class LinkedList():
    def __init__(self, head, tail):
        self.head = None
        self.tail = None
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
    
    def remove_at_begining(self):
        self.head = self.head.next

'''
The following is stacks, remember a stack of books for refernce
'''
class Stack():
    def __init__(self):
        self.top = None

'''
The following is a treeeeeee
remember that in a tree, the left side is taken when the node is smaller than target and right side is taken when node is larger than target
'''

class Tree():
    def __init__(self, data, left_side, right_side):
        self.data = data
        self.left_side = left_side
        self.right_side = right_side

'''
next up, graphs (not graphs as in drawing a line in a graph -- graphs)
'''
class Graph():
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex] = []
    def add_edge(self, vertex, target, weight):
        self.verticies[vertex].append([target, weight])

sample_graph = Graph()

sample_graph.add_vertex('colone')




'''

binary search baby...
'''