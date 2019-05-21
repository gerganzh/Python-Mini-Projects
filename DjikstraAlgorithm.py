
import sys
from collections import OrderedDict

class Node:
    def __init__(self, node, weight):
        self.name = node
        self.neighbors = {} #changing neighbours to a dictionary, so it can support dijkstra
        self.weight = int(weight) #adding the weight of the node in the form of an integer

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Node):
                if neighbor.name not in self.neighbors:
                    self.neighbors.update({neighbor.name:self.weight}) #small changes to address the weights, so it can be displayed properly in a dictionary
                    neighbor.neighbors.update({self.name:self.weight})
            else:
                return False

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

def shortest_path_dijkstra(graph, start, target, explored=[], distances={}, predecessors={}):
    if start not in graph:
        return('Start node cannot be found in the graph')
    elif target not in graph:
        return('Target cannot be found in the graph')
    elif start not in graph and target not in graph:
        return('Both nodes do not exist in this graph')
    elif start == target: #when they match in value
        shortest_path = []
        parent_dict = target
        while parent_dict != None:
            shortest_path.append(parent_dict) #append the empty list with values from the parent (predecessors) array
            parent_dict = predecessors.setdefault(parent_dict, None) #creating a default value for the key if it can't be found
        print('The shortest path ' + ' is ' + str(shortest_path) + " The cost is " + str(distances[target]))
    else: #searching
        if not explored:
            distances[start] = 0
        for neighbor in graph[start]: #to visit all adjacent (connected nodes)
            if neighbor not in explored:
                new_distance = distances[start] + graph[start][neighbor]
                if new_distance < distances.setdefault(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = start
        explored.append(start) #keep track of explored nodes
        unexplored = {}
        for k in graph: #do a recursion and replace start node with node with lowest distance
            if k not in explored:
                unexplored[k] = distances.setdefault(k, float('inf'))
        lowest_distance = min(unexplored, key=unexplored.setdefault) #min function for dictionaries
        shortest_path_dijkstra(graph, lowest_distance, target, explored, distances, predecessors) #call the function

########################################## Testing The Code ###########################################################
if __name__ == "__main__":

    A = Node('1', '20') #create instances of class Node
    B = Node('2', '15')
    C = Node('3', '18')
    D = Node('4', '5')
    E = Node('5', '2')

    A.add_neighbors([B, C, E]) #add neighbours (connected nodes)
    B.add_neighbors([A, C])
    C.add_neighbors([B, A, E, D])
    D.add_neighbors([C])
    E.add_neighbors([A, C])

    graph = Graph() #create the graph itself
    graph.add_nodes([A, B, C, D, E])
    #print_list(graph)#print the adjacency list
    dict = print_dict(graph)
    print(shortest_path_dijkstra(dict,'1','3'))
    #bfs(dict,'1')
    #print(isPath(dict,'1','3'))

    """
    Title: Dijkstra Algorithm, how to implement it in Python?
    Author: Gilles Bertrand
    Date: -
    Availability: http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
    """
    """
    Title: Week 7 - Tasks 1 to 3
    Author: Gergan Zhekov (Me)
    Date: 15/11/2017
    Availability: https://github.coventry.ac.uk/zhekovg/210CT---Gergan-Zhekov/blob/master/W7_ALL.py
    """
    
    
    
