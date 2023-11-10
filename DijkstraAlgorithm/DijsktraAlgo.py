from collections import defaultdict
from datetime import datetime
ct = datetime.now()

formatted_time = ct.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Time: {formatted_time}")

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.traffic_level = defaultdict(list)


    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance, traffic_level, road_congestion):
        self.edges[fromNode].append([toNode, traffic_level, road_congestion])
        self.distances[(fromNode, toNode)] = distance 

def Dijkstra(graph, initial, target):
    visited = {initial: 0}
    visited_factors = {initial: 0}
    path = defaultdict(list) 
    traffic = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node  

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        if minNode == target:
            break

        for edge in graph.edges[minNode]:
            road_factors = edge[1] + edge[2]
            weight = currentWeight + graph.distances[(minNode, edge[0])] 
            if edge[0] not in visited or weight < visited[edge[0]]:
                visited[edge[0]] = weight
                path[edge[0]] = [minNode, edge[1], edge[2]] 

    return visited, path

# Creating coordinates and network for start_node, target_node, distance, traffic congestion, road congestion
def CreateGraph():
    customGraph = Graph()
    customGraph.addNode("BFP")
    customGraph.addNode("LAGON")
    customGraph.addNode("LAGONP1")
    customGraph.addNode("LAGONP2")
    customGraph.addNode("LAGONP3")
    customGraph.addNode("LAGONP4")
    customGraph.addNode("LAGONP5")
    customGraph.addNode("LAGONP6")
    customGraph.addNode("LAGONP7")  
    customGraph.addNode("ALAWIHAOP1") 
    customGraph.addNode("ALAWIHAOP2")  
    customGraph.addNode("ALAWIHAOP3")
    customGraph.addNode("ALAWIHAOP4")
    customGraph.addNode("ALAWIHAOP5")
    customGraph.addNode("ALAWIHAOP6") 
    customGraph.addNode("ALAWIHAOP7")  
    customGraph.addNode("ALAWIHAOP8")
    customGraph.addNode("ALAWIHAOP9")
    customGraph.addNode("ALAWIHAOP10")
    customGraph.addNode("HATDOG")   
    customGraph.addEdge("BFP", "LAGONP1", 350, 2, 2) 
    customGraph.addEdge("BFP", "LAGONP4", 400, 1, 2) 
    customGraph.addEdge("LAGONP1", "LAGON", 290, 2, 2)
    customGraph.addEdge("LAGONP4", "LAGONP3", 700, 1, 2)
    customGraph.addEdge("LAGONP3", "LAGONP2", 950, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP2", 700, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP5", 400, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP7", 550, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP6", 130, 1, 2)
    customGraph.addEdge("LAGONP7", "ALAWIHAOP1", 650, 1, 2)
    customGraph.addEdge("ALAWIHAOP1", "ALAWIHAOP2", 290, 1, 2)
    customGraph.addEdge("ALAWIHAOP2", "ALAWIHAOP3", 700, 1, 2)
    customGraph.addEdge("ALAWIHAOP3", "ALAWIHAOP4", 700, 1, 2)
    customGraph.addEdge("ALAWIHAOP4", "ALAWIHAOP6", 350, 1, 2)
    customGraph.addEdge("ALAWIHAOP6", "ALAWIHAOP5", 350, 1, 2)
    customGraph.addEdge("ALAWIHAOP6", "ALAWIHAOP7", 350, 1, 2)
    customGraph.addEdge("ALAWIHAOP6", "ALAWIHAOP9", 640, 1, 2)
    customGraph.addEdge("ALAWIHAOP7", "ALAWIHAOP10", 450, 1, 2)
    customGraph.addEdge("ALAWIHAOP8", "ALAWIHAOP5", 290, 1, 2)

    return customGraph

# Algorithm for getting the shortest path
def SearchShortestPath(startNode, targetNode, paths, distances): 
    shortestDistance = distances[targetNode] 
    shortestPath = [targetNode] 
    shortestTraffic = []
    roadLane = []

    while shortestPath[-1] != startNode: 
        recommended_path = paths[shortestPath[-1]][0]
        recommended_traffic = paths[shortestPath[-1]][1]
        recommended_roadlane = paths[shortestPath[-1]][2]
        shortestPath.append(recommended_path)
        shortestTraffic.append(recommended_traffic)
        roadLane.append(recommended_roadlane)
    
    shortestPath.reverse()
    shortestTraffic.reverse()

    starting_point = 0
    shortestTraffic.insert(0, starting_point)
    roadLane.insert(0, starting_point)


    return shortestDistance, shortestPath, shortestTraffic, roadLane


# Initialize all the data and get the shortest possible route
def GetShortestPath(Initial, Destination):
    start_node = Initial
    target_node = Destination

    # Create and get the Graph
    customGraph = CreateGraph()

    # Implement Dijkstra algorithm and get the distances and paths
    distances, paths = Dijkstra(customGraph, start_node, target_node) 

    # Get the shortest path only
    shortest_distance, shortest_path, shortest_traffic, roadLane = SearchShortestPath(start_node, target_node, paths, distances)

    print("-"*40)
    print("Starting Point:", Initial)
    print("Destination:", Destination)
    print("-"*40)
    print("Shortest Distance:", shortest_distance * 0.001, "km")
    print("Shortest Path:", shortest_path)
    print("-"*40)
    print("Expected Traffic:") 

    for i, (path, traffic) in enumerate(zip(shortest_path, shortest_traffic)):  
        trafficLevel = ""
        pathLabel = "" 

        if path == "A":
            pathLabel = "Fire Station"
        elif path == "B":
            pathLabel = "SM City"
        elif path == "C":
            pathLabel = "Mantagbac Road"
        elif path == "D":
            pathLabel = "Vinzons Ave."
        elif path == "E":
            pathLabel = "Total Road"
        elif path == "F":
            pathLabel = "Japan Surplus"
        elif path == "H":
            pathLabel = "Pabico Elem School"

        if traffic == 0:
            trafficLevel = "[You're Here]"
        elif traffic == 1:
            trafficLevel = "Minimal traffic"
        elif traffic == 2:
            trafficLevel = "Moderate traffic"
        elif traffic == 3:
            trafficLevel = "Heavy traffic"
            
        print(f'~> {path}: {trafficLevel} '  )
        
    print("-"*40)

    print("Road Condition")
    for i, (path, lane) in enumerate(zip(shortest_path, roadLane)):  
        trafficLevel = ""
        pathLabel = "" 

        '''if path == "A":
            pathLabel = "Fire Station"
        elif path == "B":
            pathLabel = "SM City"
        elif path == "C":
            pathLabel = "Mantagbac Road"
        elif path == "D":
            pathLabel = "Vinzons Ave."
        elif path == "E":
            pathLabel = "Total Road"
        elif path == "F":
            pathLabel = "Japan Surplus"
        elif path == "H":
            pathLabel = "Pabico Elem School"

        if lane == 0:
            print(f"~> {pathLabel}: [You're Here]"  )
        else:
            print(f"~> {pathLabel}: {lane}-way-road")'''
                
    print("-"*40)

    return shortest_path, shortest_distance

GetShortestPath("BFP", "ALAWIHAOP10")