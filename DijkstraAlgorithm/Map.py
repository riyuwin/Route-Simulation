from tkinter import *
import tkintermapview
from DijsktraAlgo import GetShortestPath

paths_list = []

def GetCoordinates(routes):
    BFP = map_widget.set_marker(14.118062, 122.945806, text="BFP")
    BFPR1 = map_widget.set_marker(14.117622, 122.945908, text="") 
    ALAWIHAOR1 = map_widget.set_marker(14.109158, 122.929057, text="")
    ALAWIHAOR2 = map_widget.set_marker(14.106762, 122.926053, text="")
    ALAWIHAOR3 = map_widget.set_marker(14.106046, 122.924161, text="")
    ALAWIHAO = map_widget.set_marker(14.106661, 122.917411, text="ALAWIHAO")
    GAHONON = map_widget.set_marker(14.1192071, 122.9504177, text="Gahonon") 
    TOTAL = map_widget.set_marker(14.115620, 122.941004, text="Total")
    TOTALR1 = map_widget.set_marker(14.114174, 122.941746, text="") 
    GREENVIEW = map_widget.set_marker(14.1111768, 122.9450618, text="Greenview")   
    SAMAKAR1 = map_widget.set_marker(14.1103009, 122.9459915, text="")      
    SAMAKA = map_widget.set_marker(14.1096255, 122.9453269, text="Samaka")  
    IRAYAR1 = map_widget.set_marker(14.1122498, 122.9461457, text="")    
    IRAYAR2 = map_widget.set_marker(14.1119168, 122.9473044, text="")  
    IRAYAR3 = map_widget.set_marker(14.1135816, 122.9476048, text="")  
    IRAYA = map_widget.set_marker(14.1137273, 122.9459526, text="Iraya")   
    CAMAMBUGANP1 = map_widget.set_marker(14.107145, 122.949019, text="Camambugan P-1")
    BIBIRAOR1 = map_widget.set_marker(14.1025505, 122.9530775, text="BR1")
    BIBIRAOR2 = map_widget.set_marker(14.1043611, 122.9477794, text="BR2")
    BIBIRAOR3 = map_widget.set_marker(14.1039296, 122.9407360, text="BR3")
    BIBIRAOR4 = map_widget.set_marker(14.1025791, 122.9390007, text="BR4")
    BIBIRAOR5 = map_widget.set_marker(14.1000401, 122.9354816, text="BIBIRAO")

    raw_routes = []
    raw_coordinates = []

    
    for i in routes:
        if i == 'BFP':
            raw_coordinates.append([14.118062, 122.945806]) 
            raw_coordinates.append([14.117622, 122.945908]) 
            
            raw_routes.append(BFP)
            raw_routes.append(BFPR1)

        if i == 'TOTAL':
            raw_coordinates.append([14.115620, 122.941004]) 

            raw_routes.append(TOTAL)

        if i == 'GAHONON':
            raw_coordinates.append([14.1192071, 122.9504177]) 

            raw_routes.append(GAHONON)


        if i == 'GREENVIEW':
            raw_coordinates.append([14.114174, 122.941746]) 
            raw_coordinates.append([14.1111768, 122.9450618]) 

            raw_routes.append(TOTALR1)
            raw_routes.append(GREENVIEW)

        if i == 'IRAYA':
            raw_coordinates.append([14.1122498, 122.9461457]) 
            raw_coordinates.append([14.1119168, 122.9473044]) 
            raw_coordinates.append([14.1135816, 122.9476048]) 
            raw_coordinates.append([14.1137273, 122.9459526]) 

            raw_routes.append(IRAYAR1)
            raw_routes.append(IRAYAR2)
            raw_routes.append(IRAYAR3)
            raw_routes.append(IRAYA)


        if i == 'SAMAKA':
            raw_coordinates.append([14.1103009, 122.9459915])  #14.1103009 122.9459915
            raw_coordinates.append([14.1096255, 122.9453269])  

            raw_routes.append(SAMAKAR1) 
            raw_routes.append(SAMAKA) 

        if i == 'CAMAMBUGANP-1':
            raw_coordinates.append([14.107145, 122.949019])  

            raw_routes.append(CAMAMBUGANP1) 

        if i == 'BIBIRAO':
            raw_coordinates.append([14.1025505, 122.9530775])
            raw_coordinates.append([14.1043611, 122.9477794])
            raw_coordinates.append([14.1039296, 122.9407360])
            raw_coordinates.append([14.1025791, 122.9390007])
            raw_coordinates.append([14.1000401, 122.9354816])  

            raw_routes.append(BIBIRAOR1) 
            raw_routes.append(BIBIRAOR2) 
            raw_routes.append(BIBIRAOR3) 
            raw_routes.append(BIBIRAOR4) 
            raw_routes.append(BIBIRAOR5) 

        if i == "ALAWIHAO": 
            ALAWIHAOR1 = map_widget.set_marker(14.109158, 122.929057, text="")
            ALAWIHAOR2 = map_widget.set_marker(14.106762, 122.926053, text="")
            ALAWIHAOR3 = map_widget.set_marker(14.106046, 122.924161, text="")
            ALAWIHAO = map_widget.set_marker(14.106661, 122.917411, text="ALAWIHAO")

            raw_coordinates.append([14.109158, 122.929057])
            raw_coordinates.append([14.106762, 122.926053])
            raw_coordinates.append([14.106046, 122.924161])
            raw_coordinates.append([14.106661, 122.917411])  
            
            raw_routes.append(ALAWIHAOR1) 
            raw_routes.append(ALAWIHAOR2) 
            raw_routes.append(ALAWIHAOR3) 
            raw_routes.append(ALAWIHAO) 

            raw_routes.append(BIBIRAOR1) 


    return raw_routes, raw_coordinates

def Set(destination):

    destination_routes, shortest_distance_path = GetShortestPath("BFP", destination)

    routes, coordinates = GetCoordinates(destination_routes)
    
    print(coordinates)

    for i in range(len(coordinates) - 1):
        path_1 = map_widget.set_path([routes[i].position, routes[i+1].position, coordinates[i]])

def RemoveCoordinates():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()

def SetCoordinates():
    StartingPoint = map_widget.set_marker(14.118062, 122.945806, text="BFP")
    StaticRoute1 = map_widget.set_marker(14.117622, 122.945908, text="Route1")
    TotalRoute = map_widget.set_marker(14.115620, 122.941004, text="Total")
    StaticRoute2 = map_widget.set_marker(14.114174, 122.941746, text="Route3") 
    desination = map_widget.set_marker(14.107145, 122.949019, text="Panol Drive, Barangay Camambugan")
    
    path_1 = map_widget.set_path([StartingPoint.position, StaticRoute1.position, (14.118062, 122.945806), (14.117622, 122.945908), 
                                  (14.115620, 122.941004), (14.114174, 122.941746), (14.107145, 122.949019) ])

def SetCoordinates1():
    marker_2 = map_widget.set_marker(14.118062, 122.945806, text="BFP")
    marker_3 = map_widget.set_marker(14.117622, 122.945908, text="Route1")
    marker_4 = map_widget.set_marker(14.115620, 122.941004, text="Lagon")


    path_1 = map_widget.set_path([marker_2.position, marker_3.position, (14.118062, 122.945806), (14.117622, 122.945908), (14.115620, 122.941004)])
    


root = Tk()
root.title('Daet Map')
root.geometry('1200x700+50+0')



my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
#map_widget.set_position(14.0996, 122.9550)

map_widget.set_address("Daet, Camarines Norte, Philippines")


map_widget.set_zoom(15)

map_widget.pack()

alawihao_btn = Button(my_label, text="Alawihao", command=lambda:Set('ALAWIHAO'))
alawihao_btn.pack(side="left")

gahonon_btn = Button(my_label, text="Gahonon", command=lambda:Set('GAHONON'))
gahonon_btn.pack(side="left")

camambuganp1_btn = Button(my_label, text="Camambugan P-1", command=lambda:Set('CAMAMBUGANP-1'))
camambuganp1_btn.pack(side="left")

camambuganp2_btn = Button(my_label, text="Camambugan P-2", command=lambda:Set('CAMAMBUGANP-2'))
camambuganp2_btn.pack(side="left")

greenview_btn = Button(my_label, text="Greenview", command=lambda:Set('GREENVIEW'))
greenview_btn.pack(side="left")

samaka_btn = Button(my_label, text="Samaka", command=lambda:Set('SAMAKA'))
samaka_btn.pack(side="left")

iraya_btn = Button(my_label, text="Iraya",  command=lambda:Set('IRAYA'))
iraya_btn.pack(side="left")

bibirao_btn = Button(my_label, text="Bibirao", command=lambda:Set('BIBIRAO'))
bibirao_btn.pack(side="left")

remove_coordinates_button = Button(my_label, text="Remove Coordinates", command=RemoveCoordinates)
remove_coordinates_button.pack(side="left")


root.mainloop()

