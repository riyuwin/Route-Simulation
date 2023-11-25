from collections import defaultdict
from datetime import datetime
ct = datetime.now()

formatted_time = ct.strftime("%Y-%m-%d %H:%M:%S")

#Test

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

    #LAGON
    customGraph.addNode("LAGON")
    customGraph.addNode("LAGONP1")
    customGraph.addNode("LAGONP2")
    customGraph.addNode("LAGONP3")
    customGraph.addNode("LAGONP4")
    customGraph.addNode("LAGONP4R1")
    customGraph.addNode("LAGONP5")
    customGraph.addNode("LAGONP6")
    customGraph.addNode("LAGONP7")

    #MANTAGBAC
    customGraph.addNode("MANTAGBACP9")
    customGraph.addNode("MANTAGBACP8")
    customGraph.addNode("MANTAGBACP7")
    customGraph.addNode("MANTAGBACP6")
    customGraph.addNode("MANTAGBACP5")
    customGraph.addNode("MANTAGBACP4")
    customGraph.addNode("MANTAGBACP3")
    customGraph.addNode("MANTAGBACP2")
    customGraph.addNode("MANTAGBACP1")

    #CAMAMBUGAN
    customGraph.addNode("CAMAMBUGANP1") 
    customGraph.addNode("CAMAMBUGANP2")  
    customGraph.addNode("CAMAMBUGANP3")
    customGraph.addNode("CAMAMBUGANP4")
    customGraph.addNode("CAMAMBUGANP5")
    customGraph.addNode("CAMAMBUGANP6") 
    customGraph.addNode("CAMAMBUGANP7")  

    #BARANGAY 4
    customGraph.addNode("BARANGAY4P1") 
    customGraph.addNode("BARANGAY4P2")  
    customGraph.addNode("BARANGAY4P3")
    customGraph.addNode("BARANGAY4P4")
    customGraph.addNode("BARANGAY4P5")
    customGraph.addNode("BARANGAY4P6") 
    customGraph.addNode("BARANGAY4P7")  
    customGraph.addNode("BARANGAY4P8") 

    #BARANGAY8
    customGraph.addNode("BRGY8P1")
    customGraph.addNode("BRGY8P2")
    customGraph.addNode("BRGY8P3")
    customGraph.addNode("BRGY8P3R1")
    customGraph.addNode("BRGY8P4")
    customGraph.addNode("BRGY8P5")
    customGraph.addNode("BRGY8P6")
    customGraph.addNode("BRGY8P7")
    customGraph.addNode("BRGY8P8")
    customGraph.addNode("BRGY8P9")
    customGraph.addNode("BRGY8P10")

    # BARANGAY7
    customGraph.addNode("BRGY7P1")
    customGraph.addNode("BRGY7P2")
    customGraph.addNode("BRGY7P3")
    customGraph.addNode("BRGY7P4")
    customGraph.addNode("BRGY7P5")
    customGraph.addNode("BRGY7P6")
    customGraph.addNode("BRGY7P7")
    
    # BARANGAY6
    customGraph.addNode("BRGY6P1")
    customGraph.addNode("BRGY6P2")
    customGraph.addNode("BRGY6P3")
    customGraph.addNode("BRGY6P4")
    customGraph.addNode("BRGY6P4R1")
    customGraph.addNode("BRGY6P5") 
    customGraph.addNode("BRGY6P4R2")
    customGraph.addNode("BRGY6P4R3")
    
    # GUBAT
    customGraph.addNode("BRGYGUBATP1GUYABANO")
    customGraph.addNode("BRGYGUBATP2UBAS")
    customGraph.addNode("BRGYGUBATP3BAYABAS")
    customGraph.addNode("BRGYGUBATP4ATIS")
    customGraph.addNode("BRGYGUBATP5TSIKO") 
    
    # BARANGAY 2
    customGraph.addNode("BRGY2PASIGP1")
    customGraph.addNode("BRGY2PASIGP2")
    customGraph.addNode("BRGY2PASIGP3")
    customGraph.addNode("BRGY2PASIGP4")
    customGraph.addNode("BRGY2PASIGP5")
    customGraph.addNode("BRGY2PASIGP6")
    customGraph.addNode("BRGY2PASIGP7")
    customGraph.addNode("BRGY2PASIGP8")
    customGraph.addNode("BRGY2PASIGP8R1")
    

    customGraph.addEdge("LAGONP4R1", "BRGY6P4", 600, 3, 4)
    customGraph.addEdge("BRGY6P4", "BRGY4P4R1", 200, 3, 4)
    customGraph.addEdge("LAGONP4R1", "BRGY6P4", 600, 3, 4)
    customGraph.addEdge("BRGY6P4", "BRGY6P3", 160, 3, 4)
    customGraph.addEdge("BRGY6P3", "BRGY6P2", 250, 3, 4) 
    customGraph.addEdge("BRGY6P2", "BRGY6P5", 250, 3, 4) 
    customGraph.addEdge("BRGY6P5", "BRGY6P1", 210, 3, 4) 

    customGraph.addEdge("BFP", "LAGONP1", 350, 2, 2) 
    customGraph.addEdge("BFP", "LAGONP4", 400, 1, 2) 
    customGraph.addEdge("BFP", "LAGONP4R1", 400, 1, 2) 
    customGraph.addEdge("LAGONP1", "LAGON", 290, 2, 2)
    customGraph.addEdge("LAGONP4", "LAGONP3", 700, 1, 2)
    customGraph.addEdge("LAGONP3", "LAGONP2", 950, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP2", 700, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP5", 400, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP7", 550, 1, 2)
    customGraph.addEdge("LAGON", "LAGONP6", 130, 1, 2)

    
    customGraph.addEdge("LAGONP6", "CAMAMBUGANP7", 130, 1, 4)
    customGraph.addEdge("CAMAMBUGANP7", "CAMAMBUGANP6", 500, 2, 2)
    customGraph.addEdge("CAMAMBUGANP6", "CAMAMBUGANP5", 350, 2, 2)
    customGraph.addEdge("CAMAMBUGANP7", "CAMAMBUGANP2", 550, 1, 4)
    customGraph.addEdge("CAMAMBUGANP2", "CAMAMBUGANP3", 190, 1, 4)
    customGraph.addEdge("CAMAMBUGANP3", "CAMAMBUGANP1", 42, 1, 4)
    customGraph.addEdge("CAMAMBUGANP2", "CAMAMBUGANP4", 450, 2, 2)
    customGraph.addEdge("CAMAMBUGANP4", "CAMAMBUGANP5", 160, 2, 2)
    
    customGraph.addEdge("BFP", "MANTAGBACP9", 500, 1, 2)
    customGraph.addEdge("MANTAGBACP9", "MANTAGBACP8", 350, 1, 2)
    customGraph.addEdge("MANTAGBACP8", "MANTAGBACP7", 150, 1, 2)
    customGraph.addEdge("MANTAGBACP7", "MANTAGBACP6", 200, 1, 2)
    customGraph.addEdge("MANTAGBACP7", "MANTAGBACP5", 200, 1, 2)
    customGraph.addEdge("MANTAGBACP7", "MANTAGBACP4", 200, 1, 2)
    customGraph.addEdge("MANTAGBACP8", "MANTAGBACP3", 100, 1, 2)
    customGraph.addEdge("MANTAGBACP3", "MANTAGBACP2", 300, 1, 2)
    customGraph.addEdge("MANTAGBACP2", "MANTAGBACP1", 400, 1, 2)


    # BARANGAY 8
    customGraph.addEdge("LAGONP4R1", "BRGY6P4R1", 600, 3, 4)
    customGraph.addEdge("BRGY6P4R1", "BRGY6P4R2", 69, 2, 2 )
    customGraph.addEdge("BRGY6P4R2", "BRGY8P1", 38, 1, 2)
    customGraph.addEdge("BRGY8P1", "BRGY8P3", 200, 1, 2)
    customGraph.addEdge("BRGY8P3", "BRGY8P3R1", 49, 1, 2)
    customGraph.addEdge("BRGY8P3R1", "BRGY8P5", 83, 1, 2)
    customGraph.addEdge("BRGY8P3", "BRGY8P6", 200, 1, 2)
    customGraph.addEdge("BRGY6P4R2", "BRGY6P4R3", 150, 1, 2)
    customGraph.addEdge("BRGY6P4R3", "BRGY8P2", 74, 1, 2)
    customGraph.addEdge("BRGY8P2", "BRGY8P4", 100, 1, 2)
    customGraph.addEdge("BRGY8P4", "BRGY8P7", 100, 1, 2)
    customGraph.addEdge("BRGY8P4", "BRGY8P8", 100, 1, 2)
    customGraph.addEdge("BRGY8P8", "BRGY8P9", 300, 1, 2)
    customGraph.addEdge("BRGY8P9", "BRGY8P10", 200, 1, 2)  #ang prob ko nalang is nareread yung purok 1 sa purok 2, 4, 7, 8, 9, 10
    
    
     # BARANGAY 7
    customGraph.addEdge("LAGONP4R1", "BRGY6P4R1", 600, 3, 4)
    customGraph.addEdge("BRGY6P4", "BRGY7P1", 57, 2, 2 )
    customGraph.addEdge("BRGY6P4", "BRGY7P2", 170, 1, 2)
    customGraph.addEdge("BRGY7P2", "BRGY7P3", 400, 1, 2)
    customGraph.addEdge("BRGY7P3", "BRGY7P4", 200, 1, 2)
    customGraph.addEdge("BRGY7P4", "BRGY7P5", 100, 1, 2)
    customGraph.addEdge("BRGY7P2", "BRGY7P7", 400, 1, 2)
    
    # FOR BARANGAY 7 PUROK 6    
    customGraph.addEdge("LAGONP4R1", "BRGY6P4", 600, 3, 4)
    customGraph.addEdge("BRGY6P4", "BRGY4P4R1", 200, 3, 4)
    customGraph.addEdge("LAGONP4R1", "BRGY6P4", 600, 3, 4)
    customGraph.addEdge("BRGY6P4", "BRGY6P3", 160, 3, 4)
    customGraph.addEdge("BRGY6P3", "BRGY7P6", 250, 3, 4)
    
    
    
    # BARANGAY GUBAT
    customGraph.addEdge("LAGONP4R1", "BRGY6P4R1", 600, 3, 4)
    customGraph.addEdge("BRGY6P4", "BRGY7P1", 57, 2, 2 )
    customGraph.addEdge("BRGY6P4", "BRGY7P2", 170, 1, 2)
    customGraph.addEdge("BRGY7P2", "BRGY7P3", 400, 1, 2)
    customGraph.addEdge("BRGY7P3", "BRGY7P4", 200, 1, 2)
    customGraph.addEdge("BRGY7P4", "BRGY7P5", 100, 1, 2)
    customGraph.addEdge("BRGY7P5", "BRGYGUBATP1GUYABANO", 200, 1, 2)
    customGraph.addEdge("BRGY7P5", "BRGYGUBATP2UBAS", 200, 1, 2)
    customGraph.addEdge("BRGYGUBATP2UBAS", "BRGYGUBATP3BAYABAS", 1000, 1, 2)
    customGraph.addEdge("BRGYGUBATP3BAYABAS", "BRGYGUBATP4ATIS", 200, 1, 2)
    customGraph.addEdge("BRGYGUBATP4ATIS", "BRGYGUBATP5TSIKO", 200, 1, 2)
    
    # BARANGAY 2 
    customGraph.addEdge("LAGONP4R1", "BRGY6P4R1", 600, 3, 4)
    customGraph.addEdge("BRGY6P4R1", "BRGY6P4R2", 69, 2, 2 )
    customGraph.addEdge("BRGY6P4R2", "BRGY6P4R3", 150, 1, 2)
    customGraph.addEdge("BRGY6P4R3", "BRGY2PASIGP8R1", 130, 1, 2)
    customGraph.addEdge("BRGY2PASIGP8R1", "BRGY2PASIGP1", 600, 1, 2)
    customGraph.addEdge("BRGY2PASIGP8R1", "BRGY2PASIGP8", 600, 1, 2)
    customGraph.addEdge("BRGY2PASIGP8", "BRGY2PASIGP2", 86, 1, 2)
    customGraph.addEdge("BRGY2PASIGP2", "BRGY2PASIGP3", 66, 1, 2)
    customGraph.addEdge("BRGY2PASIGP3", "BRGY2PASIGP4", 71, 1, 2)
    customGraph.addEdge("BRGY2PASIGP4", "BRGY2PASIGP5", 69, 1, 2)
    customGraph.addEdge("BRGY2PASIGP4", "BRGY2PASIGP7", 69, 1, 2)
    
    # FOR BARANGAY 2 P 6    
    customGraph.addEdge("BFP", "LAGONP1", 350, 2, 2)  
    customGraph.addEdge("LAGONP1", "LAGON", 290, 2, 2)
    customGraph.addEdge("LAGON", "BRGY2PASIGP6", 290, 2, 2)

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

GetShortestPath("BFP", "BRGY6P4")
