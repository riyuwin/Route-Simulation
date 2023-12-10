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

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance, duration, traffic_congestion, road_condition):
        self.edges[fromNode].append([toNode, distance, duration, traffic_congestion, road_condition])
        self.distances[(fromNode, toNode)] = duration  # Use duration as the distance for Dijkstra

def dijkstra(graph, initial, target):
    visited = {initial: (0, 0)}  # Composite weight (duration, distance)
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None or visited[node][0] < visited[minNode][0]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        if minNode == target:
            break

        for edge in graph.edges[minNode]:
            toNode, distance, duration, traffic_congestion, road_condition = edge
            weight = (currentWeight[0] + duration, currentWeight[1] + distance)

            if toNode not in visited or weight < visited[toNode]:
                visited[toNode] = weight
                path[toNode] = [minNode, distance, duration, traffic_congestion, road_condition]

    return visited, path

def dfs_paths(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return [path]
    if start not in graph.nodes:
        return []

    paths = []
    for edge in graph.edges[start]:
        to_node, distance, duration, traffic_congestion, road_condition = edge
        if to_node not in path:
            new_paths = dfs_paths(graph, to_node, end, path + [to_node])
            for p in new_paths:
                paths.append(p)

    return paths

def display_path_info(path_info, start_node, end_node, graph):
    current_node = end_node
    total_duration = 0
    total_distance = 0  # Initialize total distance
    total_traffic_congestion = 0
    total_road_condition = 0
    path_sequence = []

    while current_node != start_node:
        previous_node, distance, duration, traffic_congestion, road_condition = path_info[current_node]
        total_duration += duration
        total_distance += distance  # Accumulate total distance
        total_traffic_congestion += traffic_congestion
        total_road_condition += road_condition
        path_sequence.append((previous_node, current_node, distance, duration, traffic_congestion, road_condition))
        current_node = previous_node

    # Reverse the path sequence to display from start to end
    path_sequence.reverse()

    shortest_distance = []
    route_only_shortest_distance = ["BFP"]

    print("Shortest Path:")
    for step in path_sequence:
        from_node, to_node, distance, duration, traffic_congestion, road_condition = step
        print(f"From {from_node} to {to_node}: Distance {distance} units, Duration {duration} mins, Traffic Congestion {traffic_congestion}, Road Condition {road_condition}")
        shortest_distance.append([to_node, distance, duration, traffic_congestion, road_condition])
        route_only_shortest_distance.append(to_node)
    
    avg_total_traffic_congestion = round(total_traffic_congestion / len(path_sequence), 2)
    avg_total_road_condition = round(total_road_condition / len(path_sequence), 2)

    print(f"\nTotal Duration from {start_node} to {end_node}: {total_duration} mins")
    print(f"Total Distance from {start_node} to {end_node}: {total_distance} units")  # Display total distance
    print(f"Average Traffic Congestion: {avg_total_traffic_congestion}")
    print(f"Average Road Condition: {avg_total_road_condition}")

    shortest_path_details = {
        'Total Duration': total_duration,
        'Total Distance': total_distance,
        'Average Traffic Congestion': avg_total_traffic_congestion,
        'Average Road Condition': avg_total_road_condition,
    }

    return route_only_shortest_distance, shortest_distance, shortest_path_details

def display_all_paths_info(paths_info, graph):
    all_paths = []  # List to store all paths
 
    for path_info in paths_info:
        total_duration = 0
        total_distance = 0
        total_traffic_congestion = 0
        total_road_condition = 0
        path_sequence = []

        current_path = []  # List to store 'to_node' values for the current path

        print("Path:")
        for step in path_info:
            from_node, to_node, distance, duration, traffic_congestion, road_condition = step
            total_duration += duration
            total_distance += distance
            total_traffic_congestion += traffic_congestion
            total_road_condition += road_condition
            path_sequence.append((from_node, to_node, distance, duration, traffic_congestion, road_condition))

            current_path.append([to_node, distance, duration, traffic_congestion, road_condition])  # Append 'to_node' to the current path list
            print(f"From {from_node} to {to_node}: Distance {distance} units, Duration {duration} mins, Traffic Congestion {traffic_congestion}, Road Condition {road_condition}")

        all_paths.append(current_path)  # Append the current path list to all_paths

        print(f"Total Duration: {total_duration} mins")
        print(f"Total Distance: {total_distance} units")
        print(f"Average Traffic Congestion: {round(total_traffic_congestion / len(path_info), 2)}")
        print(f"Average Road Condition: {round(total_road_condition / len(path_info), 2)}\n")

    return all_paths

# Example usage
#myGraph = Graph()

myGraph = Graph()

myGraph.addNode("BFP")

    #LAGON
myGraph.addNode("LAGON")
myGraph.addNode("LAGONP1")
myGraph.addNode("LAGONP2")
myGraph.addNode("LAGONP3")
myGraph.addNode("LAGONP4")
myGraph.addNode("LAGONP4R1")
myGraph.addNode("LAGONP5")
myGraph.addNode("LAGONP6")
myGraph.addNode("LAGONP7")


myGraph.addEdge("BFP", "LAGONP1", 350, 1, 2, 2) 
myGraph.addEdge("BFP", "LAGONP4", 464, 2, 1, 2) 
myGraph.addEdge("BFP", "LAGONP4R1", 400, 3, 1, 2) 

myGraph.addEdge("LAGONP1", "LAGON", 450, 1, 1, 2)
myGraph.addEdge("LAGONP4", "LAGONP3", 450, 1, 1, 2)
myGraph.addEdge("LAGONP3", "LAGONP2", 450, 2, 1, 2)
myGraph.addEdge("LAGON", "LAGONP2", 450, 2, 1, 2)
myGraph.addEdge("LAGON", "LAGONP5", 300, 1, 1, 2)
myGraph.addEdge("LAGONP5", "LAGONP7", 230, 1, 1, 2)
myGraph.addEdge("LAGON", "LAGONP6", 120, 0.5, 1, 2)


# ALAWIHAO
myGraph.addNode("ALAWIHAOP1") 
myGraph.addNode("ALAWIHAOP2")  
myGraph.addNode("ALAWIHAOP3")
myGraph.addNode("ALAWIHAOP4")
myGraph.addNode("ALAWIHAOP5")
myGraph.addNode("ALAWIHAOP6") 
myGraph.addNode("ALAWIHAOP7")  
myGraph.addNode("ALAWIHAOP8")
myGraph.addNode("ALAWIHAOP9")
myGraph.addNode("ALAWIHAOP10") 


myGraph.addEdge("LAGONP7", "ALAWIHAOP1", 650, 1, 1, 2)
myGraph.addEdge("ALAWIHAOP1", "ALAWIHAOP2", 290, 1, 1, 2)
myGraph.addEdge("ALAWIHAOP2", "ALAWIHAOP3", 700, 1, 1, 2)
myGraph.addEdge("ALAWIHAOP3", "ALAWIHAOP4", 700, 1, 1, 2)
myGraph.addEdge("ALAWIHAOP4", "ALAWIHAOP5", 884, 2, 1, 2)
myGraph.addEdge("ALAWIHAOP5", "ALAWIHAOP6", 350, 1, 1, 2)
myGraph.addEdge("ALAWIHAOP6", "ALAWIHAOP7", 350, 2, 1, 2)
myGraph.addEdge("ALAWIHAOP5", "ALAWIHAOP8", 341, 1, 1, 2)
myGraph.addEdge("ALAWIHAOP8", "ALAWIHAOP10", 359, 2, 1, 2)
myGraph.addEdge("ALAWIHAOP8", "ALAWIHAOP9", 249, 1, 1, 2)

   # DOGONGAN
myGraph.addNode("DOGONGANP1") 
myGraph.addNode("DOGONGANP2")  
myGraph.addNode("DOGONGANP3")
myGraph.addNode("DOGONGANP4")
myGraph.addNode("DOGONGANP5")
myGraph.addNode("DOGONGANP6")

myGraph.addEdge("ALAWIHAOP9", "DOGONGANP1", 530, 3, 1, 2)
myGraph.addEdge("DOGONGANP1", "DOGONGANP2", 650, 2, 1, 2)
myGraph.addEdge("DOGONGANP2", "DOGONGANP4", 340, 2, 2, 2)
myGraph.addEdge("DOGONGANP2", "DOGONGANP5", 269, 2, 2, 2) 
myGraph.addEdge("DOGONGANP1", "DOGONGANP3", 300, 2, 2, 2)  
myGraph.addEdge("DOGONGANP3", "DOGONGANP6", 500, 2, 2, 2)  


    #CAMAMBUGAN
myGraph.addNode("CAMAMBUGANP1") 
myGraph.addNode("CAMAMBUGANP2")  
myGraph.addNode("CAMAMBUGANP3")
myGraph.addNode("CAMAMBUGANP4")
myGraph.addNode("CAMAMBUGANP5")
myGraph.addNode("CAMAMBUGANP6") 
myGraph.addNode("CAMAMBUGANP7") 

myGraph.addEdge("LAGONP6", "CAMAMBUGANP7", 550, 1, 1, 4)
myGraph.addEdge("CAMAMBUGANP7", "CAMAMBUGANP6", 500, 2, 2, 2)
myGraph.addEdge("CAMAMBUGANP6", "CAMAMBUGANP5", 450, 1, 2, 2)
myGraph.addEdge("CAMAMBUGANP7", "CAMAMBUGANP2", 550, 2, 1, 4)
myGraph.addEdge("CAMAMBUGANP2", "CAMAMBUGANP3", 190, 1, 1, 4)
myGraph.addEdge("CAMAMBUGANP3", "CAMAMBUGANP1", 42, 0.5, 1, 4)
myGraph.addEdge("CAMAMBUGANP3", "CAMAMBUGANP4", 600, 2, 2, 2)
myGraph.addEdge("CAMAMBUGANP2", "CAMAMBUGANP4", 450, 2, 2, 2)
myGraph.addEdge("CAMAMBUGANP4", "CAMAMBUGANP5", 350, 1, 2, 2)

# BARANGAY6
myGraph.addNode("BIBIRAOP1")
myGraph.addNode("BIBIRAOP2")
myGraph.addNode("BIBIRAOP3")
myGraph.addNode("BIBIRAOP4")
myGraph.addNode("BIBIRAOP5")


myGraph.addEdge("CAMAMBUGANP1", "BIBIRAOP1", 1804, 9, 1, 2)
myGraph.addEdge("BIBIRAOP1", "BIBIRAOP2", 497, 1, 1, 2)
myGraph.addEdge("BIBIRAOP2", "BIBIRAOP3", 787, 2, 1, 2)
myGraph.addEdge("BIBIRAOP3", "BIBIRAOP4", 946, 3, 1, 2)
myGraph.addEdge("BIBIRAOP4", "BIBIRAOP5", 279, 1, 1, 2)

    # MAGANG
myGraph.addNode("MAGANGP1")
myGraph.addNode("MAGANGP2")
myGraph.addNode("MAGANGP2R1")
myGraph.addNode("MAGANGP3")
myGraph.addNode("MAGANGP4")
myGraph.addNode("MAGANGP4R1")
myGraph.addNode("MAGANGP5")
myGraph.addNode("MAGANGP6")

myGraph.addEdge("BIBIRAOP1", "MAGANGP4R1", 1500, 6, 1, 2)
myGraph.addEdge("MAGANGP4R1", "MAGANGP2", 300, 2, 1, 2)


myGraph.addEdge("CAMAMBUGANP1", "MAGANGP1", 752, 1, 1, 2)
myGraph.addEdge("MAGANGP1", "MAGANGP2R1", 477, 2, 1, 2)
myGraph.addEdge("MAGANGP2R1", "MAGANGP2", 338, 1, 1, 2)
myGraph.addEdge("MAGANGP2", "MAGANGP3", 710, 1,  1, 2)
myGraph.addEdge("MAGANGP3", "MAGANGP4", 353, 3,  1, 2) 
myGraph.addEdge("MAGANGP2", "MAGANGP5", 971, 4,  1, 2)
myGraph.addEdge("MAGANGP5", "MAGANGP6", 293, 1,  1, 2)

    # CALASGASAN
myGraph.addNode("CALASGASANP1")
myGraph.addNode("CALASGASANP2")
myGraph.addNode("CALASGASANP3")
myGraph.addNode("CALASGASANP4")
myGraph.addNode("CALASGASANP5")
myGraph.addNode("CALASGASANP6")

myGraph.addEdge("MAGANGP6", "CALASGASANP1", 492, 1, 2, 2)
myGraph.addEdge("CALASGASANP1", "CALASGASANP2", 170, 1, 2, 2)
myGraph.addEdge("CALASGASANP2", "CALASGASANP3", 157, 1, 2, 2)
myGraph.addEdge("CALASGASANP3", "CALASGASANP4", 118, 1, 2, 2)
myGraph.addEdge("CALASGASANP4", "CALASGASANP5", 194, 1, 2, 2)
myGraph.addEdge("CALASGASANP5", "CALASGASANP6", 386, 1, 2, 2)

    # MANCURZ
myGraph.addNode("MANCRUZP1")
myGraph.addNode("MANCRUZP2")
myGraph.addNode("MANCRUZP3")
myGraph.addNode("MANCRUZP4")


# PAMORANGON
myGraph.addNode("PAMORANGONP1")
myGraph.addNode("PAMORANGONP2")
myGraph.addNode("PAMORANGONP3")
myGraph.addNode("PAMORANGONP4")
myGraph.addNode("PAMORANGONP5")
myGraph.addNode("PAMORANGONP6")

myGraph.addEdge("MAGANGP2R1", "PAMORANGONP1", 338, 1, 1, 4)
myGraph.addEdge("PAMORANGONP1", "MANCRUZP4", 338, 1, 1, 4)
myGraph.addEdge("MAGANGP2R1", "MANCRUZP4", 464, 1, 1, 4)
myGraph.addEdge("MANCRUZP4", "MANCRUZP2", 130, 1, 1, 2)
myGraph.addEdge("MANCRUZP2", "MANCRUZP1", 641, 2, 1, 2)
myGraph.addEdge("MANCRUZP1", "MANCRUZP3", 265, 0.5, 1, 2)

myGraph.addEdge("MANCRUZP4", "PAMORANGONP2", 130, 0.5, 1, 2)
myGraph.addEdge("PAMORANGONP1", "PAMORANGONP3", 102, 0.5, 1, 2)
myGraph.addEdge("PAMORANGONP3", "PAMORANGONP5", 68, 0.5, 1, 2)
myGraph.addEdge("PAMORANGONP3", "PAMORANGONP4", 413, 2, 1, 2)
myGraph.addEdge("PAMORANGONP3", "PAMORANGONP6", 891, 2, 1, 2) 
myGraph.addEdge("PAMORANGONP4", "PAMORANGONP6", 1102, 2, 2, 2)


# PAMORANGON
myGraph.addNode("BRGY5P1")
myGraph.addNode("BRGY5P2")
myGraph.addNode("BRGY5P3")
myGraph.addNode("BRGY5P3R1")
myGraph.addNode("BRGY5P3R2")
myGraph.addNode("BRGY5P4")
myGraph.addNode("BRGY5P5")
myGraph.addNode("BRGY5P5R1")
myGraph.addNode("BRGY5P5R2")
myGraph.addNode("BRGY5P6")


myGraph.addEdge("LAGONP4", "BRGY5P1", 384, 1, 2, 2) 
myGraph.addEdge("LAGONP4R1", "BRGY5P1", 574, 1, 2, 4)

#myGraph.addEdge("LAGONP4R1", "BRGY5P2", 573, 1, 2, 4)

myGraph.addEdge("LAGONP4R1", "BRGY5P3", 146, 0.5, 2, 2) 
myGraph.addEdge("BRGY5P3", "BRGY5P1", 137, 0.5, 2, 2)
myGraph.addEdge("BRGY5P1", "BRGY5P3", 137, 0.5, 2, 2)

myGraph.addEdge("BRGY5P3", "BRGY5P3R1", 137, 0.5, 2, 2)
myGraph.addEdge("BRGY5P3R1", "BRGY5P4", 159, 0.5, 2, 2)
myGraph.addEdge("BRGY5P4", "BRGY5P5", 214, 0.5, 2, 2)

myGraph.addEdge("BRGY5P3R1", "BRGY5P3R2", 450, 2, 3, 2)
myGraph.addEdge("BRGY5P3R2", "BRGY5P2", 137, 0.5, 3, 2)


# PAMORANGON
myGraph.addNode("MANTAGBACP1")
myGraph.addNode("MANTAGBACP2") 
myGraph.addNode("MANTAGBACP2R1") 
myGraph.addNode("MANTAGBACP3") 
myGraph.addNode("MANTAGBACP4") 
myGraph.addNode("MANTAGBACP5") 
myGraph.addNode("MANTAGBACP6")  
myGraph.addNode("MANTAGBACP7") 
myGraph.addNode("MANTAGBACP8")
myGraph.addNode("MANTAGBACP9")
myGraph.addNode("MANTAGBACP9R1")   

myGraph.addEdge("BFP", "MANTAGBACP9", 684, 3, 2, 2) 
myGraph.addEdge("LAGONP4R1", "MANTAGBACP9", 300, 1, 2, 2)
myGraph.addEdge("MANTAGBACP9", "MANTAGBACP9R1", 117, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP9R1", "MANTAGBACP4", 210, 1, 2, 2)
myGraph.addEdge("MANTAGBACP4", "MANTAGBACP5", 125, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP5", "MANTAGBACP2R1", 125, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP2R1", "MANTAGBACP2", 172, 0.5, 2, 2)


myGraph.addEdge("LAGONP4R1", "MANTAGBACP6", 513, 1, 2, 4)
myGraph.addEdge("MANTAGBACP6", "BRGY5P2", 52, 0.5, 2, 4)
myGraph.addEdge("BRGY5P2", "BRGY6P4", 129, 0.8, 3, 4)
myGraph.addEdge("BRGY5P2", "BRGY6P3", 129, 0.8, 3, 4)

myGraph.addEdge("MANTAGBACP6", "MANTAGBACP2R1", 66, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP2R1", "MANTAGBACP5", 102, 1, 2, 2)
myGraph.addEdge("MANTAGBACP2R1", "MANTAGBACP2", 172, 0.7, 2, 2)

myGraph.addEdge("MANTAGBACP9R1", "MANTAGBACP8", 123, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP8", "MANTAGBACP3", 114, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP3", "MANTAGBACP2", 112, 0.5, 2, 2)
myGraph.addEdge("MANTAGBACP2", "MANTAGBACP1", 150, 0.5, 2, 2)

# PAMORANGON
myGraph.addNode("BRGY6P1")
myGraph.addNode("BRGY6P2")
myGraph.addNode("BRGY6P3")
myGraph.addNode("BRGY6P4")
myGraph.addNode("BRGY6P5")

myGraph.addEdge("BRGY5P5", "BRGY5P5R1", 70, 0.3, 2, 2)
myGraph.addEdge("BRGY5P5R1", "BRGY5P5R2", 480, 0.4, 2, 2)
myGraph.addEdge("BRGY5P5R1", "BORABODP3", 1079, 0.4, 2, 2)
myGraph.addEdge("BRGY5P5R2", "BRGY6P1", 100, 0.2, 2, 2)

myGraph.addEdge("BRGY6P4", "MANTAGBACP1", 75, 0.5, 3, 4)
myGraph.addEdge("BRGY5P3R2", "BRGY6P3", 92, 0.5, 1, 4)
myGraph.addEdge("BRGY6P3", "BRGY6P2", 150, 0.5, 1, 4)
myGraph.addEdge("BRGY6P2", "BRGY6P5", 147, 0.5, 2, 4)
myGraph.addEdge("BRGY6P5", "BRGY6P1", 166, 0.5, 2, 4)

# PAMORANGON
myGraph.addNode("GAHONONP1")
myGraph.addNode("GAHONONP2")
myGraph.addNode("GAHONONP3")
myGraph.addNode("GAHONONP4")
myGraph.addNode("GAHONONP5")
myGraph.addNode("GAHONONP6")

myGraph.addEdge("LAGONP4", "GAHONONP3", 209, 1, 2, 4)
myGraph.addEdge("GAHONONP3", "GAHONONP2", 210, 0.5, 2, 4)
myGraph.addEdge("GAHONONP3", "GAHONONP4", 700, 3, 2, 2)
myGraph.addEdge("GAHONONP4", "GAHONONP5", 279, 1, 2, 1)

myGraph.addEdge("GAHONONP2", "GAHONONP1", 600, 2, 2, 4)
myGraph.addEdge("GAHONONP2", "GAHONONP6", 1600, 5, 2, 4)

myGraph.addEdge("GAHONONP5", "BRGY5P5", 80, 0.5, 2, 1)
myGraph.addEdge("BRGY5P5", "GAHONONP5", 80, 0.5, 2, 2)
#myGraph.addEdge("BRGY5P5", "BORABODP3", 1079, 2, 2, 2)


# PAMORANGON
myGraph.addNode("AWITANP1")
myGraph.addNode("AWITANP2")
myGraph.addNode("AWITANP3")

myGraph.addEdge("GAHONONP6", "AWITANP3", 950, 5, 2, 2)
myGraph.addEdge("AWITANP3", "AWITANP2", 171, 1, 2, 2)
myGraph.addEdge("AWITANP2", "AWITANP1", 741, 3, 2, 2) 


# PAMORANGON
myGraph.addNode("BORABODP1")
myGraph.addNode("BORABODP2")
myGraph.addNode("BORABODP3")
myGraph.addNode("BORABODP4")
myGraph.addNode("BORABODP5")

myGraph.addEdge("BORABODP3", "AWITANP1", 869, 1, 1, 2)
myGraph.addEdge("BRGY6P1", "BORABODP1", 534, 0.5, 1, 4)
myGraph.addEdge("BORABODP1", "BORABODP2", 494, 0.5, 1, 4)
myGraph.addEdge("BORABODP2", "BORABODP4", 950, 3, 1, 4)
myGraph.addEdge("BORABODP2", "BORABODP5", 668, 1, 1, 4)
myGraph.addEdge("BORABODP5", "AWITANP1", 726, 1, 1, 2)

# PAMORANGON
myGraph.addNode("BAGASBASP1")
myGraph.addNode("BAGASBASP2")
myGraph.addNode("BAGASBASP3")
myGraph.addNode("BAGASBASP4")
myGraph.addNode("BAGASBASP5")
myGraph.addNode("BAGASBASP6")

myGraph.addEdge("BORABODP5", "BAGASBASP2", 1379, 1, 1, 4)
myGraph.addEdge("BAGASBASP2", "BAGASBASP3", 84, 0.5, 1, 4)
myGraph.addEdge("BAGASBASP2", "BAGASBASP1", 507, 1, 1, 4)
myGraph.addEdge("BAGASBASP3", "BAGASBASP4", 362, 1, 2, 2)
myGraph.addEdge("BAGASBASP4", "BAGASBASP5", 340, 1, 2, 2)
myGraph.addEdge("BAGASBASP5", "BAGASBASP6", 297, 1, 2, 2)


    # BARANGAY7
myGraph.addNode("BRGY7P1")
myGraph.addNode("BRGY7P2")
myGraph.addNode("BRGY7P3")
myGraph.addNode("BRGY7P4")
myGraph.addNode("BRGY7P5")
myGraph.addNode("BRGY7P6")
myGraph.addNode("BRGY7P7")
myGraph.addNode("BRGY7P7R1")
myGraph.addNode("BRGY7P3R1")  

 # BARANGAY 7
myGraph.addEdge("BRGY5P2", "BRGY7P1", 190, 1, 2, 4)
myGraph.addEdge("BRGY7P1", "BRGY7P2", 270, 1, 2, 2)
myGraph.addEdge("BRGY7P2", "BRGY7P3R1", 80, 0.5, 1, 4)
myGraph.addEdge("BRGY7P3R1", "BRGY7P3", 70, 0.5, 1, 4)
myGraph.addEdge("BRGY7P3", "BRGY7P4", 149, 1, 1, 4)
myGraph.addEdge("BRGY7P4", "BRGY7P5", 252, 1, 1, 4)
myGraph.addEdge("BRGY6P3", "BRGY7P6", 590, 1, 2, 2)
myGraph.addEdge("BRGY7P6", "BRGY7P7", 77, 0.5, 1, 2)
myGraph.addEdge("BRGY7P7", "BRGY7P7R1", 270, 1, 1, 2)


    # BARANGAY7
myGraph.addNode("BRGY8P1")
myGraph.addNode("BRGY8P2")
myGraph.addNode("BRGY8P3")
myGraph.addNode("BRGY8P4")
myGraph.addNode("BRGY8P5")
myGraph.addNode("BRGY8P6")
myGraph.addNode("BRGY8P7")
myGraph.addNode("BRGY8P7") 
myGraph.addNode("BRGY8P8") 
myGraph.addNode("BRGY8P9R1")
myGraph.addNode("BRGY8P9")
myGraph.addNode("BRGY8P9R3")  

myGraph.addEdge("BRGY6P4", "BRGY8P1", 198, 1, 2, 4)   
myGraph.addEdge("MANTAGBACP1", "BRGY8P2", 169, 1, 2, 4)   

myGraph.addEdge("BRGY8P1", "BRGY8P3", 150, 1, 2, 2)   
myGraph.addEdge("BRGY8P2", "BRGY8P4", 157, 1, 2, 2)   

myGraph.addEdge("BRGY7P2", "BRGY8P3", 74, 0.5, 2, 2)   
myGraph.addEdge("BRGY8P3", "BRGY8P4", 92, 0.5, 2, 2)   

myGraph.addEdge("BRGY8P3", "BRGY8P6", 97, 0.5, 2, 2)   
myGraph.addEdge("BRGY8P4", "BRGY8P7", 157, 1, 2, 2)  
myGraph.addEdge("BRGY8P4", "BRGY8P8", 157, 1, 2, 2)   

myGraph.addEdge("BRGY8P7", "BRGY8P9", 247, 1, 2, 2)   
myGraph.addEdge("BRGY8P3", "BRGY8P6", 97, 0.5, 2, 2)   


myGraph.addEdge("BRGY8P3", "BRGY8P9R1", 100, 0.5, 2, 2)
myGraph.addEdge("BRGY8P9R1", "BRGY8P5", 25, 0.5, 2, 2)
myGraph.addEdge("BRGY7P3R1", "BRGY8P5", 100, 0.5, 2, 2)
myGraph.addEdge("BRGY8P5", "BRGY8P6", 100, 0.5, 2, 2)

myGraph.addEdge("BRGY8P6", "BRGY8P9R1", 207, 0.5, 2, 2) 
myGraph.addEdge("BRGY8P9R1", "BRGY8P9", 126, 0.5, 2, 2) 
 
myGraph.addEdge("BRGY8P9", "BRGY8P9R3", 109, 0.5, 2, 2)  
myGraph.addEdge("BRGY8P9R3", "BRGY8P10", 209, 1, 2, 2)  
 
myGraph.addEdge("BRGY7P5", "BRGY8P10", 198, 1, 2, 2)  



    # BARANGAY7
    # GUBAT
myGraph.addNode("BRGYGUBATP1GUYABANO")
myGraph.addNode("BRGYGUBATP2UBAS")
myGraph.addNode("BRGYGUBATP3BAYABAS")
myGraph.addNode("BRGYGUBATP4ATIS")
myGraph.addNode("BRGYGUBATP5TSIKO") 


myGraph.addEdge("BRGY7P5", "BRGYGUBATP1GUYABANO", 237, 1, 2, 4)
myGraph.addEdge("BRGYGUBATP1GUYABANO", "BRGYGUBATP2UBAS", 94, 0.5, 2, 2)  
myGraph.addEdge("BRGYGUBATP1GUYABANO", "BRGYGUBATP3BAYABAS", 465, 2, 2, 4)
myGraph.addEdge("BRGYGUBATP3BAYABAS", "BRGYGUBATP4ATIS", 483, 2, 2, 4)  
myGraph.addEdge("BRGYGUBATP3BAYABAS", "BRGYGUBATP4ATIS", 483, 1, 2, 4)  
myGraph.addEdge("BRGYGUBATP4ATIS", "BRGYGUBATP5TSIKO", 427, 1, 2, 4)  
  
myGraph.addEdge("BORABODP4", "GUBATP5", 1700, 6, 2, 4)  

myGraph.addNode("BRGY1P1")
myGraph.addNode("BRGY1P2")
myGraph.addNode("BRGY1P3")
myGraph.addNode("BRGY1P4")
myGraph.addNode("BRGY1P5") 
myGraph.addNode("BRGY1P6") 
myGraph.addNode("BRGY1P7")
myGraph.addNode("BRGY1P8")  
myGraph.addNode("BRGY1P4R1") 
myGraph.addNode("BRGY1P4R2")  
myGraph.addNode("BRGY1P5R1")  
myGraph.addNode('BRGY1P5R2')

myGraph.addEdge("BRGY8P2", "BRGY1P1", 130, 1, 2, 4)

myGraph.addEdge("BRGY1P1", "BRGY1P2", 114, 0.5, 2, 2)
myGraph.addEdge("BRGY1P2", "BRGY1P3", 212, 0.5, 2, 2) 
myGraph.addEdge("BRGY1P3", "BRGY1P6", 83, 0.5, 2, 2)  
myGraph.addEdge("BRGY1P6", "BRGY1P7", 89, 0.5, 2, 2)  
myGraph.addEdge("BRGY1P7", "BRGY1P8", 366, 1, 2, 2)  

myGraph.addEdge("BRGY1P1", "BRGY1P4", 222, 1, 2, 2)
myGraph.addEdge("BRGY1P2", "BRGY1P4R1", 188, 0.5, 2, 2)
myGraph.addEdge("BRGY1P4", "BRGY1P4R1", 117, 0.5, 2, 2)

myGraph.addEdge("BRGY1P5", "BRGY1P5R1", 118, 0.5, 2, 2)
myGraph.addEdge("BRGY1P5R1", "BRGY1P5R2", 210, 0.5, 2, 2)

myGraph.addEdge("BRGY1P3", "BRGY1P4R2", 162, 0.5, 2, 2)
myGraph.addEdge("BRGY1P4R1", "BRGY1P4R2", 211, 0.5, 2, 2)

myGraph.addEdge("BRGY1P4R2", "BRGY1P5R2", 51, 0.5, 2, 2)

myGraph.addEdge("BRGY1P4", "BRGY1P5", 68, 0.5, 2, 2)



myGraph.addNode("BRGY3P1")
myGraph.addNode("BRGY3P2")
myGraph.addNode("BRGY3P3")
myGraph.addNode("BRGY3P4")
myGraph.addNode("BRGY3P5") 
myGraph.addNode("BRGY3P6") 

myGraph.addEdge("MANTAGBACP1", "BRGY3P1", 79, 0.5, 2, 4)
myGraph.addEdge("BRGY3P1", "BRGY3P2", 76, 0.5, 2, 4)
myGraph.addEdge("BRGY3P2", "BRGY1P1", 146, 0.5, 2, 4)
myGraph.addEdge("CAMAMBUGANP5", "BRGY3P2", 209, 1, 2, 2)
myGraph.addEdge("BRGY3P2", "BRGY3P3", 86, 0.5, 2, 2)
myGraph.addEdge("BRGY3P3", "BRGY3P4", 61, 0.5, 2, 2)
myGraph.addEdge("BRGY3P4", "BRGY3P5", 88, 0.5, 2, 2)
myGraph.addEdge("BRGY3P5", "BRGY3P6", 88, 0.5, 2, 2)

myGraph.addEdge("BRGY3P6", "CAMAMBUGANP4", 215, 0.5, 2, 2)
myGraph.addEdge("BRGY1P5", "BRGY3P6", 156, 0.5, 2, 2)


myGraph.addNode("BRGY2P1")
myGraph.addNode("BRGY2P2")
myGraph.addNode("BRGY2P3")
myGraph.addNode("BRGY2P4")
myGraph.addNode("BRGY2P5") 
myGraph.addNode("BRGY2P6") 
myGraph.addNode("BRGY2P7") 
myGraph.addNode("BRGY2P7R1")  
myGraph.addNode("BRGY2P7R2")  
myGraph.addNode("BRGY2P8") 
myGraph.addNode("BRGY2P8R1") 
myGraph.addNode("BRGY2P8R2") 
myGraph.addNode("BRGY2P8R3") 

myGraph.addEdge("BRGY1P5", "BRGY2P8", 239, 1, 2, 4)
myGraph.addEdge("BRGY2P8", "BRGY2P1", 128, 1, 2, 2)
myGraph.addEdge("BRGY3P6", "BRGY3P6R1", 128, 1, 2, 2)
myGraph.addEdge("BRGY3P6R1", "BRGY2P1", 100, 1, 2, 2)

myGraph.addEdge("BRGY2P8", "BRGY2P8R1", 72, 0.5, 2, 4)
myGraph.addEdge("BRGY2P8R1", "BRGY2P8R2", 71, 0.5, 2, 4)
myGraph.addEdge("BRGY2P8R2", "BRGY2P8R3", 71, 0.5, 2, 4)

myGraph.addEdge("BRGY2P8R3", "BRGY2P7", 69, 0.5, 2, 4)
myGraph.addEdge("BRGY2P7", "BRGY2P7R1", 69, 0.5, 2, 4)

myGraph.addEdge("BRGY2P7R1", "BRGY2P7R2", 83, 0.5, 2, 4)

myGraph.addEdge("BRGY2P7R2", "PAMORANGONP1", 500, 1, 2, 4)

myGraph.addEdge("BRGY2P1", "BRGY2P2", 76, 0.5, 2, 2)
myGraph.addEdge("BRGY2P2", "BRGY2P3", 74, 0.5, 2, 2)
myGraph.addEdge("BRGY2P3", "BRGY2P4", 66, 0.5, 2, 2)

myGraph.addEdge("BRGY2P8R1", "BRGY2P2", 130, 0.5, 2, 2)
myGraph.addEdge("BRGY2P8R2", "BRGY2P3", 130, 0.5, 2, 2)
myGraph.addEdge("BRGY2P8R3", "BRGY2P4", 130, 0.5, 2, 2)

myGraph.addEdge("BRGY2P7", "BRGY2P5", 127, 0.5, 2, 2)

myGraph.addEdge("BRGY2P7", "BRGY2P5", 127, 0.5, 2, 2)
myGraph.addEdge("BRGY2P7R1", "BRGY2P6", 118, 0.5, 2, 2)

    # SAN ISIDRO
myGraph.addNode("SANISIDROP1")
myGraph.addNode("SANISIDROP2")
myGraph.addNode("SANISIDROP3")
myGraph.addNode("SANISIDROP4")
myGraph.addNode("SANISIDROP5")
myGraph.addNode("SANISIDROP6")

myGraph.addEdge("BRGY1P8", "SANISIDROP1", 50, 0.1, 1, 2)
myGraph.addEdge("SANISIDROP1", "SANISIDROP2", 268, 1, 1, 2)
myGraph.addEdge("SANISIDROP1", "SANISIDROP3", 899, 2, 2, 2)
myGraph.addEdge("SANISIDROP2", "SANISIDROP4", 730, 2, 2, 2)
myGraph.addEdge("SANISIDROP3", "SANISIDROP5", 523, 2, 1, 2)
myGraph.addEdge("SANISIDROP5", "SANISIDROP6", 523, 2, 1, 2)

    # SAN ISIDRO
myGraph.addNode("COBANGBANGP1")
myGraph.addNode("COBANGBANGP1R1")
myGraph.addNode("COBANGBANGP1R2")
myGraph.addNode("COBANGBANGP1R3")
myGraph.addNode("COBANGBANGP1R4")
myGraph.addNode("COBANGBANGP2")
myGraph.addNode("COBANGBANGP2R1")
myGraph.addNode("COBANGBANGP3R1")
myGraph.addNode("COBANGBANGP3")
myGraph.addNode("COBANGBANGP4")
myGraph.addNode("COBANGBANGP5")
myGraph.addNode("COBANGBANGP6")

myGraph.addEdge("BRGY1P5R2", "COBANGBANGP2R1", 60, 0.5, 1, 2)
myGraph.addEdge("COBANGBANGP2R1", "COBANGBANGP2", 74, 0.5, 1, 2)
myGraph.addEdge("COBANGBANGP2", "COBANGBANGP3", 159, 0.5, 1, 2)
myGraph.addEdge("COBANGBANGP3", "COBANGBANGP3R1", 159, 0.5, 1, 2)
myGraph.addEdge("COBANGBANGP3R1", "COBANGBANGP4", 200, 0.5, 1, 2)
myGraph.addEdge("COBANGBANGP4", "COBANGBANGP5", 150, 0.5, 1, 2)
myGraph.addEdge("COBANGBANGP5", "COBANGBANGP6", 150, 0.5, 1, 2)

myGraph.addEdge("BRGY2P7R2", "COBANGBANGP1R1", 30, 0.2, 1, 2)
myGraph.addEdge("COBANGBANGP1R1", "COBANGBANGP1R2", 30, 0.2, 1, 2)
myGraph.addEdge("COBANGBANGP1R2", "COBANGBANGP1R3", 30, 0.2, 1, 2)
myGraph.addEdge("COBANGBANGP1R3", "COBANGBANGP1R4", 30, 0.2, 1, 2)
myGraph.addEdge("COBANGBANGP1R4", "COBANGBANGP1", 60, 0.4, 1, 2)

myGraph.addEdge("COBANGBANGP1", "COBANGBANGP3R1", 299, 0.5, 1, 2)

    # SAN ISIDRO
myGraph.addNode("MAMBALITEP1")
myGraph.addNode("MAMBALITEP2")
myGraph.addNode("MAMBALITEP3")
myGraph.addNode("MAMBALITEP4")
myGraph.addNode("MAMBALITEP5")
myGraph.addNode("MAMBALITEP6")
myGraph.addNode("MAMBALITEP7")

myGraph.addEdge("COBANGBANGP6", "MAMBALITEP1", 1258, 4, 1, 2)
myGraph.addEdge("MAMBALITEP1", "MAMBALITEP6", 628, 2, 1, 2)
myGraph.addEdge("MAMBALITEP1", "MAMBALITEP2", 480, 1, 1, 2)
myGraph.addEdge("MAMBALITEP2", "MAMBALITEP3", 480, 1, 1, 2)
myGraph.addEdge("MAMBALITEP3", "MAMBALITEP4", 337, 1, 1, 2)
myGraph.addEdge("MAMBALITEP4", "MAMBALITEP5", 649, 1, 1, 2)
myGraph.addEdge("MAMBALITEP5", "MAMBALITEP7", 449, 1, 1, 2)

myGraph.addEdge("SANISIDROP6", "MAMBALITEP6", 1330, 5, 1, 2)

start_node = "BFP"
end_node = "COBANGBANGP2"


def GetShortestPath(start_node, end_node):
    all_paths_info = []
    all_paths = dfs_paths(myGraph, start_node, end_node)

    for path in all_paths:
        total_duration = 0
        total_distance = 0
        total_traffic_congestion = 0
        total_road_condition = 0
        path_info = []

        for i in range(len(path) - 1):
            from_node, to_node = path[i], path[i + 1]
            
            # Find the correct edge for the current node pair
            edges = myGraph.edges[from_node]
            for edge in edges:
                if edge[0] == to_node:
                    distance, duration, traffic_congestion, road_condition = edge[1:]
                    total_duration += duration
                    total_distance += distance
                    total_traffic_congestion += traffic_congestion
                    total_road_condition += road_condition
                    path_info.append((from_node, to_node, distance, duration, traffic_congestion, road_condition))
                    break  # Exit the loop once the correct edge is found

        all_paths_info.append(path_info)

    print("All Possible Paths:")
    all = display_all_paths_info(all_paths_info, myGraph)

    shortest_distance, path_info = dijkstra(myGraph, start_node, end_node)

    print("\nShortest Path:")
    route_only, short, shortest_path_details = display_path_info(path_info, start_node, end_node, myGraph)

    return all, short, route_only, shortest_path_details


GetShortestPath(start_node, end_node)