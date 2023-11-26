from collections import defaultdict
from datetime import datetime
ct = datetime.now()

formatted_time = ct.strftime("%Y-%m-%d %H:%M:%S")

#Sean

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
    

    
    # BARANGAY6
    customGraph.addNode("BIBIRAOP1")
    customGraph.addNode("BIBIRAOP2")
    customGraph.addNode("BIBIRAOP3")
    customGraph.addNode("BIBIRAOP4")
    customGraph.addNode("BIBIRAOP5")

    # MAGANG
    customGraph.addNode("MAGANGP1")
    customGraph.addNode("MAGANGP2")
    customGraph.addNode("MAGANGP3")
    customGraph.addNode("MAGANGP4")
    customGraph.addNode("MAGANGP5")
    customGraph.addNode("MAGANGP6")


    # PAMORANGON
    customGraph.addNode("PAMORANGONP1")
    customGraph.addNode("PAMORANGONP2")
    customGraph.addNode("PAMORANGONP3")
    customGraph.addNode("PAMORANGONP4")
    customGraph.addNode("PAMORANGONP5")
    customGraph.addNode("PAMORANGONP6")

    # ALAWIHAO
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

    # DOGONGAN
    customGraph.addNode("DOGONGANP1") 
    customGraph.addNode("DOGONGANP2")  
    customGraph.addNode("DOGONGANP3")
    customGraph.addNode("DOGONGANP4")
    customGraph.addNode("DOGONGANP5")
    customGraph.addNode("DOGONGANP6")

    # MANCURZ
    customGraph.addNode("MANCRUZP1")
    customGraph.addNode("MANCRUZP2")
    customGraph.addNode("MANCRUZP3")
    customGraph.addNode("MANCRUZP4")

    # SAN ISIDRO
    customGraph.addNode("SANISIDROP1")
    customGraph.addNode("SANISIDROP2")
    customGraph.addNode("SANISIDROP3")
    customGraph.addNode("SANISIDROP4")
    customGraph.addNode("SANISIDROP5")
    customGraph.addNode("SANISIDROP6")

    # MAMBALITE
    customGraph.addNode("MAMBALITEP1")
    customGraph.addNode("MAMBALITEP2")
    customGraph.addNode("MAMBALITEP3")
    customGraph.addNode("MAMBALITEP4")
    customGraph.addNode("MAMBALITEP5")
    customGraph.addNode("MAMBALITEP6")
    customGraph.addNode("MAMBALITEP7")


    customGraph.addEdge("ALAWIHAOP9", "DOGONGANP1", 2573, 1, 2)
    customGraph.addEdge("DOGONGANP1", "DOGONGANP3", 1057, 1, 2)
    customGraph.addEdge("DOGONGANP3", "DOGONGANP6", 340, 2, 2)
    customGraph.addEdge("DOGONGANP3", "DOGONGANP2", 269, 2, 2)
    customGraph.addEdge("DOGONGANP2", "DOGONGANP4", 500, 2, 2)
    customGraph.addEdge("DOGONGANP4", "DOGONGANP5", 300, 2, 2)  



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

    
    customGraph.addEdge("LAGONP7", "ALAWIHAOP1", 650, 1, 2)
    customGraph.addEdge("ALAWIHAOP1", "ALAWIHAOP2", 290, 1, 2)
    customGraph.addEdge("ALAWIHAOP2", "ALAWIHAOP3", 700, 1, 2)
    customGraph.addEdge("ALAWIHAOP3", "ALAWIHAOP4", 700, 1, 2)
    customGraph.addEdge("ALAWIHAOP4", "ALAWIHAOP5", 884, 1, 2)
    customGraph.addEdge("ALAWIHAOP5", "ALAWIHAOP6", 330, 1, 2)
    customGraph.addEdge("ALAWIHAOP6", "ALAWIHAOP7", 311, 1, 2)
    customGraph.addEdge("ALAWIHAOP5", "ALAWIHAOP8", 341, 1, 2)
    customGraph.addEdge("ALAWIHAOP8", "ALAWIHAOP10", 359, 1, 2)
    customGraph.addEdge("ALAWIHAOP8", "ALAWIHAOP9", 249, 1, 2)


    
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

    
    customGraph.addEdge("CAMAMBUGANP1", "BIBIRAOP1", 1804, 1, 2)
    customGraph.addEdge("BIBIRAOP1", "BIBIRAOP2", 497, 1, 2)
    customGraph.addEdge("BIBIRAOP2", "BIBIRAOP3", 787, 1, 2)
    customGraph.addEdge("BIBIRAOP3", "BIBIRAOP4", 946, 1, 2)
    customGraph.addEdge("BIBIRAOP4", "BIBIRAOP5", 279, 1, 2)

    customGraph.addEdge("CAMAMBUGANP1", "MAGANGP1", 752, 1, 2)
    customGraph.addEdge("MAGANGP1", "MAGANGP2", 477, 1, 2)
    customGraph.addEdge("MAGANGP2", "MAGANGP3", 710, 1, 2)
    customGraph.addEdge("MAGANGP3", "MAGANGP4", 353, 1, 2)
    customGraph.addEdge("MAGANGP2", "MAGANGP5", 971, 1, 2)
    customGraph.addEdge("MAGANGP2", "MAGANGP6", 288, 1, 2)


    customGraph.addEdge("MAGANGP1", "PAMORANGONP1", 338, 1, 2)
    customGraph.addEdge("PAMORANGONP1", "PAMORANGONP2", 334, 1, 2)
    customGraph.addEdge("PAMORANGONP2", "PAMORANGONP3", 724, 1, 2)
    customGraph.addEdge("PAMORANGONP3", "PAMORANGONP4", 413, 1, 2)
    customGraph.addEdge("PAMORANGONP3", "PAMORANGONP5", 67, 1, 2)
    customGraph.addEdge("PAMORANGONP5", "PAMORANGONP6", 891, 1, 2)

    customGraph.addEdge("MAGANGP1", "MANCRUZP4", 464, 1, 2)
    customGraph.addEdge("MANCRUZP4", "MANCRUZP2", 130, 1, 2)
    customGraph.addEdge("MANCRUZP2", "MANCRUZP1", 641, 1, 2)
    customGraph.addEdge("MANCRUZP1", "MANCRUZP3", 265, 1, 2)

    customGraph.addEdge("COBANGBANGP6", "MAMBALITEP1", 1258, 1, 2)
    customGraph.addEdge("MAMBALITEP1", "MAMBALITEP2", 480, 1, 2)
    customGraph.addEdge("MAMBALITEP1", "MAMBALITEP6", 628, 1, 2)
    customGraph.addEdge("MAMBALITEP2", "MAMBALITEP3", 270, 1, 2)
    customGraph.addEdge("MAMBALITEP3", "MAMBALITEP4", 337, 1, 2)
    customGraph.addEdge("MAMBALITEP4", "MAMBALITEP5", 649, 1, 2)
    customGraph.addEdge("MAMBALITEP5", "MAMBALITEP7", 449, 1, 2)

    customGraph.addEdge("CAMAMBUGANP5", "SANISIDROP1", 1246, 1, 2)
    customGraph.addEdge("SANISIDROP1", "SANISIDROP2", 268, 1, 2)
    customGraph.addEdge("SANISIDROP2", "SANISIDROP3", 899, 1, 2)
    customGraph.addEdge("SANISIDROP2", "SANISIDROP4", 730, 1, 2)
    customGraph.addEdge("SANISIDROP3", "SANISIDROP5", 560, 1, 2)
    customGraph.addEdge("SANISIDROP5", "SANISIDROP6", 523, 1, 2)


    customGraph.addEdge("BFP", "BRGY8P1", 1400, 1, 2)

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

    # Cobangbang
    customGraph.addNode("COBANGBANGP1")
    customGraph.addNode("COBANGBANGP2") 
    customGraph.addNode("COBANGBANGP3") 
    customGraph.addNode("COBANGBANGP4") 
    customGraph.addNode("COBANGBANGP5") 
    customGraph.addNode("COBANGBANGP6")

    customGraph.addEdge("BARANGAY1P5", "COBANGBANGP1", 2600, 2, 2)
    customGraph.addEdge("COBANGBANGP3", "COBANGBANGP2", 2700, 1, 2)
    customGraph.addEdge("BARANGAY1P6", "COBANGBANGP3", 2600, 1, 2)
    customGraph.addEdge("COBANGBANGP2", "COBANGBANGP4", 3100, 1, 2)  
    customGraph.addEdge("COBANGBANGP4", "COBANGBANGP5", 3100, 1, 2)
    customGraph.addEdge("COBANGBANGP4", "COBANGBANGP6", 3400, 1, 2)

    # AWITAN
    customGraph.addNode("AWITANP3")
    customGraph.addNode("AWITANP1")
    customGraph.addNode("AWITANP2")

    customGraph.addEdge("LAGONP3", "AWITANP3", 3500, 2, 2)
    customGraph.addEdge("AWITANP3", "AWITANP1", 3800, 2, 2)
    customGraph.addEdge("AWITANP1", "AWITANP2", 4100, 2, 2)

    # BAGASBAS
    customGraph.addNode("BAGASBASP1")
    customGraph.addNode("BAGASBASP2")
    customGraph.addNode("BAGASBASP3")
    customGraph.addNode("BAGASBASP4")
    customGraph.addNode("BAGASBASP5")
    customGraph.addNode("BAGASBASP6")
    
    customGraph.addEdge("BORABODP5", "BAGASBASP1", 4400, 2, 2)
    customGraph.addEdge("BAGASBASP1", "BAGASBASP2", 4600, 2, 2)
    customGraph.addEdge("BAGASBASP2", "BAGASBASP3", 4800, 2, 2)
    customGraph.addEdge("BAGASBASP3", "BAGASBASP4", 5000, 2, 2)
    customGraph.addEdge("BAGASBASP4", "BAGASBASP5", 5300, 2, 2)
    customGraph.addEdge("BAGASBASP5", "BAGASBASP6", 5600, 2, 2)

    #BORABOD
    customGraph.addNode("BORABODP1")
    customGraph.addNode("BORABODP2")
    customGraph.addNode("BORABODP3")
    customGraph.addNode("BORABODP4")
    customGraph.addNode("BORABODP5")
    customGraph.addNode("BORABODP6")
    
    customGraph.addEdge("BFP", "BORABODP1", 2000, 2, 2)
    customGraph.addEdge("BORABODP1", "BORABODP2", 2400, 2, 2)
    customGraph.addEdge("BORABODP2", "BORABODP4", 2700, 2, 2)
    customGraph.addEdge("BORABODP4", "BORABODP5", 3400, 2, 2)
    customGraph.addEdge("BORABODP5", "BORABODP6", 3800, 2, 2)
    customGraph.addEdge("BFP", "BORABODP3", 2600, 2, 2)


    #BARANGAY 1
    customGraph.addNode("BARANGAY1P1")
    customGraph.addNode("BARANGAY1P2")
    customGraph.addNode("BARANGAY1P3")
    customGraph.addNode("BARANGAY1P4")
    customGraph.addNode("BARANGAY1P5")
    customGraph.addNode("BARANGAY1P6")
    customGraph.addNode("BARANGAY1P7")
    customGraph.addNode("BARANGAY1P8")
    
    customGraph.addEdge("BFP", "BARANGAY1P1", 16000, 2, 2)
    customGraph.addEdge("BARANGAY1P1", "BARANGAY1P2", 1700, 2, 2)
    customGraph.addEdge("BARANGAY1P2", "BARANGAY1P3", 1900, 2, 2)
    customGraph.addEdge("BARANGAY1P3", "BARANGAY1P6", 2000, 2, 2)
    customGraph.addEdge("BARANGAY1P6", "BARANGAY1P7", 2000, 2, 2)
    customGraph.addEdge("BARANGAY1P7", "BARANGAY1P8", 2100, 2, 2)
    customGraph.addEdge("BARANGAY1P1", "BARANGAY1P4", 1900, 2, 2)
    customGraph.addEdge("BARANGAY1P4", "BARANGAY1P5", 1900, 2, 2)

    # CALASGASAN
    customGraph.addNode("CALASGASANP1")
    customGraph.addNode("CALASGASANP2")
    customGraph.addNode("CALASGASANP3")
    customGraph.addNode("CALASGASANP4")
    customGraph.addNode("CALASGASANP5")
    customGraph.addNode("CALASGASANP6")

    customGraph.addEdge("MAGANGP6", "CALASGASANP1", 492, 2, 2)
    customGraph.addEdge("CALASGASANP1", "CALASGASANP2", 170, 2, 2)
    customGraph.addEdge("CALASGASANP2", "CALASGASANP3", 157, 2, 2)
    customGraph.addEdge("CALASGASANP3", "CALASGASANP4", 118, 2, 2)
    customGraph.addEdge("CALASGASANP4", "CALASGASANP5", 194, 2, 2)
    customGraph.addEdge("CALASGASANP5", "CALASGASANP6", 386, 2, 2)



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
