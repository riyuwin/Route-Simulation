from tkinter import *
import tkintermapview
from DijsktraAlgo import GetShortestPath

paths_list = []

routes_label_list = []

def GetCoordinates(routes): 

    raw_routes = []
    raw_coordinates = []

    
    for i in routes:
        if i == 'BFP':
            
            if routes[1] == "LAGONP1":
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
                BFPR1 = map_widget.set_marker(14.117622, 122.945908, text="") 

                raw_coordinates.append([14.1181492, 122.9458283]) 
                raw_coordinates.append([14.117622, 122.945908]) 
                
                raw_routes.append(BFP)
                raw_routes.append(BFPR1)
            elif routes[1] == "LAGONP4":
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
                
                raw_coordinates.append([14.1181492, 122.9458283]) 
                
                raw_routes.append(BFP)
                
        if i == 'LAGONP1':
            LAGONP1 = map_widget.set_marker(14.1168800, 122.9432159, text="LAGONP1")
            
            raw_coordinates.append([14.1168800, 122.9432159]) 

            raw_routes.append(LAGONP1)


        if i == 'LAGON':
            LAGON = map_widget.set_marker(14.1156366, 122.9409842, text="LAGON")
            
            raw_coordinates.append([14.1156366, 122.9409842]) 
            
            raw_routes.append(LAGON)
 
        if i == 'LAGONP2':
            LAGONP2R1 = map_widget.set_marker(14.1161958, 122.9407131, text="LAGONP2R1")
            LAGONP2R2 = map_widget.set_marker(14.1169251, 122.9413635, text="LAGONP2R2")
            LAGONP2R3 = map_widget.set_marker(14.1178483, 122.9406330, text="LAGONP3R3")
            LAGONP2R4 = map_widget.set_marker(14.1179370, 122.9402085, text="LAGONP4R4")
            LAGONP2R5 = map_widget.set_marker(14.1184001, 122.9398437, text="LAGONP5R5")
            LAGONP2R6 = map_widget.set_marker(14.1207033, 122.9392599, text="LAGONP5R6")
            LAGONP2R7 = map_widget.set_marker(14.1224618, 122.9390640, text="LAGONP5R7")
            LAGONP2R8 = map_widget.set_marker(14.1232970, 122.9386402, text="LAGONP5R8")

            raw_coordinates.append([14.1161958, 122.9407131]) 
            raw_coordinates.append([14.1169251, 122.9413635]) 
            raw_coordinates.append([14.1178483, 122.9406330]) 
            raw_coordinates.append([14.1179370, 122.9402085])
            raw_coordinates.append([14.1184001, 122.9398437])
            raw_coordinates.append([14.1207033, 122.9392599])
            raw_coordinates.append([14.1224618, 122.9390640])
            raw_coordinates.append([14.1232970, 122.9386402])

            raw_routes.append(LAGONP2R1)
            raw_routes.append(LAGONP2R2)
            raw_routes.append(LAGONP2R3)
            raw_routes.append(LAGONP2R4)
            raw_routes.append(LAGONP2R5)
            raw_routes.append(LAGONP2R6)
            raw_routes.append(LAGONP2R7)
            raw_routes.append(LAGONP2R8)

        if i == 'LAGONP7':
            LAGONP7 = map_widget.set_marker(14.1131212, 122.9366253, text="LAGONP7")
            
            raw_coordinates.append([14.1131212, 122.9366253]) 

            raw_routes.append(LAGONP7)

        
        if i == 'LAGONP5':
            
            LAGONP5R1 = map_widget.set_marker(14.1161958, 122.9407131, text="LAGONP5R1")
            LAGONP5R2 = map_widget.set_marker(14.1150188, 122.9389632, text="LAGONP5R2")
            LAGONP5R3 = map_widget.set_marker(14.1147849, 122.9381085, text="LAGONP5R3")
            LAGONP5R4 = map_widget.set_marker(14.1144514, 122.9350615, text="LAGONP5R4")
            
            raw_coordinates.append([14.1161958, 122.9407131]) 
            raw_coordinates.append([14.1150188, 122.9389632]) 
            raw_coordinates.append([14.1147849, 122.9381085]) 
            raw_coordinates.append([14.1144514, 122.9350615]) 

            raw_routes.append(LAGONP5R1)
            raw_routes.append(LAGONP5R2)
            raw_routes.append(LAGONP5R3)
            raw_routes.append(LAGONP5R4)

        if i == 'LAGONP4':
            LAGONP4 = map_widget.set_marker(14.1185202, 122.9472156, text="LAGONP4")
            LAGONP4R1 = map_widget.set_marker(14.1191716, 122.9469856, text="LAGONP4")
            LAGONP4R2 = map_widget.set_marker(14.1197948, 122.9467542, text="LAGONP4")


            raw_coordinates.append([14.1185202, 122.9472156])
            raw_coordinates.append([14.1191716, 122.9469856]) 
            raw_coordinates.append([14.1197948, 122.9467542]) 
 


            raw_routes.append(LAGONP4)
            raw_routes.append(LAGONP4R1)
            raw_routes.append(LAGONP4R2)


        if i == 'LAGONP3':
            LAGON3 = map_widget.set_marker(14.1209278, 122.9475108, text="LAGON3")
            LAGONP3R1 = map_widget.set_marker(14.1229959, 122.9440899, text="LAGONP3")
            
            raw_coordinates.append([14.1209278, 122.9475108]) 
            raw_coordinates.append([14.1229959, 122.9440899])

            raw_routes.append(LAGON3)
            raw_routes.append(LAGONP3R1)

        if i == 'LAGONP6':
            LAGON6 = map_widget.set_marker(14.1145746, 122.9415359, text="LAGON6")
            
            raw_coordinates.append([14.1145746, 122.9415359]) 

            raw_routes.append(LAGON6)


    return raw_routes, raw_coordinates

def Set(destination):
    global specific_routes_label

    destination_routes, shortest_distance_path = GetShortestPath("BFP", destination)

    routes, coordinates = GetCoordinates(destination_routes)

    y_axis = 220
    for i in destination_routes:
        specific_routes_label = canvas.create_text(1020, y_axis, text=i, anchor='center', fill='white', font=('courier new', 10))
        y_axis+=30
        routes_label_list.append(specific_routes_label)

    canvas.itemconfig(routes_label, text=f"Routes: ")
    canvas.itemconfig(total_distance_label, text=f"Total Distance: {(shortest_distance_path)} meters")

    print(coordinates)

    for i in range(len(coordinates) - 1):
        path_1 = map_widget.set_path([routes[i].position, routes[i+1].position, coordinates[i]])

def RemoveCoordinates():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()
    
    canvas.itemconfig(routes_label, text=f"")
    canvas.itemconfig(total_distance_label, text=f"")

    for i in routes_label_list:
        canvas.itemconfig(i, text=f"")


root = Tk()
root.title('Daet Map')
root.geometry('1200x700+50+0')

canvas = Canvas(root, width=1200, height=700, bg='#686362')
canvas.pack()

my_label = LabelFrame(root)
my_label.pack(pady=20)

label_text = "Simulation Map"
label = Label(canvas, text=label_text, bg='white', font=('Arial', 15)) 
label_window = canvas.create_window(450, 50, window=label)

text = "Details:"
canvas.create_text(930, 130, text=text, anchor='center', fill='white', font=('courier new', 12))
routes_label = canvas.create_text(925, 190, text="", anchor='center', fill='white', font=('courier new', 10))
total_distance_label = canvas.create_text(1000, 160, text="", anchor='center', fill='white', font=('courier new', 10))

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=500, corner_radius=0)
#map_widget.set_position(14.0996, 122.9550)

canvas.create_window(450, 360, window=my_label)

map_widget.set_address("Daet, Camarines Norte, Philippines")


map_widget.set_zoom(14)

map_widget.pack()





lagon_btn = Button(my_label, text="LAGON", command=lambda:Set('LAGON'))
lagon_btn.pack(side="left")

lagonp1_btn = Button(my_label, text="LAGONP1", command=lambda:Set('LAGONP1'))
lagonp1_btn.pack(side="left")

lagonp2_btn = Button(my_label, text="LAGONP2", command=lambda:Set('LAGONP2'))
lagonp2_btn.pack(side="left")

lagonp3_btn = Button(my_label, text="LAGONP3", command=lambda:Set('LAGONP3'))
lagonp3_btn.pack(side="left")

lagonp4_btn = Button(my_label, text="LAGONP4", command=lambda:Set('LAGONP4'))
lagonp4_btn.pack(side="left")

lagonp5_btn = Button(my_label, text="LAGONP5", command=lambda:Set('LAGONP5'))
lagonp5_btn.pack(side="left")

lagonp6_btn = Button(my_label, text="LAGONP6", command=lambda:Set('LAGONP6'))
lagonp6_btn.pack(side="left")

lagonp7_btn = Button(my_label, text="LAGONP7", command=lambda:Set('LAGONP7'))
lagonp7_btn.pack(side="left")







lagonp6_btn = Button(my_label, text="LAGONP6", command=lambda:Set('LAGONP6'))
lagonp6_btn.pack(side="left")

remove_coordinates_button = Button(root, text="Reset", background="black", fg="gold", width=10, height=2, command=RemoveCoordinates)
canvas.create_window(1130, 600, window=remove_coordinates_button)

root.mainloop()
