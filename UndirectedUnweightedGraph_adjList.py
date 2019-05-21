#Week 7, Task 1

'''
I implemented an unweighted and undirected graph data structure, where the nodes consist of positive integers. I
decided to use adjacency list approach. 
'''

import sys
from collections import OrderedDict

class Node: #creating class node
    def __init__(self, node):
        self.name = node
        self.neighbors = [] #the list will be appended by adjacent (connected) nodes

    def add_neighbors(self, neighbors): #function to add adjacent nodes(neighbours) in the list
        for neighbor in neighbors:
            if isinstance(neighbor, Node): #if the object is an instance of Node
                if neighbor.name not in self.neighbors: #makes sure that there are no duplicate nodes
                    self.neighbors.append(neighbor.name) #appending the neighbors list
                    neighbor.neighbors.append(self.name)
            else:
                return None

class Graph: #creating the Graph class
    def __init__(self):
        self.nodes = {} #dictionary that will contain the nodes

    def add_nodes(self, nodes): #adding nodes to Graph
        for node in nodes:
            if isinstance(node, Node): #checks if the object is an instance of Node
                self.nodes[node.name] = node.neighbors #

    def adjacency_list(self): #used for printing the adjacency list
        adj_list = [str(key) + ":" + str(self.nodes[key]) for key in self.nodes.keys()] #creating the list with dictionary inside
        for a in adj_list: #to print it on a new row
            print(a)

    def adjacency_list_dict(self): #to print a dictionary, with the dictionary of neighbours inside (needed for BFS and isPath)
        return({str(key): self.nodes[key] for key in self.nodes.keys()})

def isPath(graph, v, w, path=[]):
    path += [v]
    if v == w: #if/when the nodes are the same
        print('There is path!')
        return('The path is: ' + str(path))
    elif v not in graph and w not in graph: #if both nodes are not in the graph
        raise TypeError('Both nodes do not exist in this graph. ')
    elif v not in graph:
        raise TypeError ("The start node does not exist in this graph. ")
    elif w not in graph:
        raise TypeError("The end node does not exist in this graph. ")
    for node in graph[v]: #for every node that is connected to the start node
        if node not in path: #if it's not already in path
            newpath = isPath(graph, node, w, path) #call the function again with the new node instead of start node
            return newpath #and return the path
    return ("Can't find path to this node!")

def print_list(graph): #to print the list
    print('The Adjacency List for this unweighted, undirected graph is: ')
    return graph.adjacency_list()

def print_dict(graph): #to print the dictionary
    return(graph.adjacency_list_dict())

def bfs(graph1, start): #BFS Search
    queue = [start] #create the queue
    visited = [] #keep track of the visited nodes
    if start not in graph1:
        raise TypeError('Node not found.')
    while queue: #looping until queue is empty
        node = queue.pop(0) #remove element with index 0 from list and returns it
        visited.append(node) #append the list with node
        neighbours = graph1[node] #get the adjacent nodes
        for neighbour in neighbours: #for each element in neighbours
            queue.append(neighbour) #append the queue with neighbour node
            visited.append(neighbour) #append the visited list with neighbour node
        return bfs_write(visited) #remove the duplicates and retain order

def  bfs_write(lst): #output the traversed nodes to an external txt file
    f = open('file.txt', 'w+')
    f.write(str(list(OrderedDict.fromkeys(lst))))
    f.close()

########################################## Testing The Code ###########################################################
if __name__ == "__main__":

    A = Node('1') #create instances of class Node
    B = Node('2')
    C = Node('3')
    D = Node('4')
    E = Node('5')

    A.add_neighbors([B, C, E]) #add neighbours (connected nodes)
    B.add_neighbors([A, C])
    C.add_neighbors([B, A, E, D])
    D.add_neighbors([C])
    E.add_neighbors([A, C])

    graph = Graph() #create the graph itself
    graph.add_nodes([A, B, C, D, E])
    print_list(graph)#print the adjacency list
    dict = print_dict(graph)
    bfs(dict,'1')
    print(isPath(dict,'1','3'))
