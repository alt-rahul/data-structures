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
    def __init__(self, data, left_child, right_child):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

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

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Tree(data)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                    else:
                        current_node = current_node.left_child
                elif new_node.data > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child
                return False
        
    def find_min(self):
        current_node = self.root
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.data

    def in_order(self, current_node):
        if current_node:
            current_node = self.in_order(current_node.left_child)
            print(current_node.data)
            current_node = self.in_order(current_node.right_child)
        return current_node.data

'''
recurssion sort
'''
def binary_search(target_value, list):
    if len(list) ==0:
        return False
    
    while True:
        middle = int(len(list)/2)
        if (target_value == list[middle]):
            return True
        elif (target_value < list[middle]):
            return binary_search(target_value, list[:middle])
        else: 
            return binary_search(target_value, list[middle:])


'''
search algos - DFS - target far away from starting
'''
import queue

# this is for graphs
def depth_first_search(visted_vertexes, graph, current_vertex):
    if current_vertex not in visted_vertexes:
        print(current_vertex)
        visted_vertexes.add(current_vertex)
        for adjacted_vertex in graph[current_vertex]:
            depth_first_search(visted_vertexes, graph, adjacted_vertex)

class dfs_tree():
    def __init__(self, root):
        self.root = root
    
    #in order is first starts from ends nodes, left end node, top node, right end node, repeat.
    def in_order(self, current_node):

        if current_node:
            self.in_order(current_node.left_child)
            print(current_node.data)
            self.in_order(current_node.right_child)

    # pre order is left end node all the way and reverse to right end 
    def pre_order(self, current_node):
        if current_node:
            print(current_node.data)
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_chilld)

    #post order is opposite of pre order but im not gonna be coding that one up


'''
search algos - BFS - target close to from starting
'''


def breadth_first_search(graph, initial_value, target_value ):
    visted_vertexes = []
    bfs_queue = queue.LifoQueue()
    visted_vertexes.append(initial_value)
    bfs_queue.put(initial_value)

    while not bfs_queue.empty():
        currrent_node = bfs_queue.get()
        if currrent_node == target_value:
            return True
        for adjacted_node in graph[currrent_node]:
            if adjacted_node not in visted_vertexes:
                visted_vertexes.append(adjacted_node)
                bfs_queue.put(adjacted_node)


