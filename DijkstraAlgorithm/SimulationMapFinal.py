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


        if i == 'ALAWIHAOP1':
            ALAWIHAOPR1 = map_widget.set_marker(14.1116075, 122.9333130, text="ALAWIHAOP1") 
            
            raw_coordinates.append([14.1116075, 122.9333130])  

            raw_routes.append(ALAWIHAOPR1)

        if i == 'ALAWIHAOP2':
            ALAWIHAOPR2 = map_widget.set_marker(14.110115305360178, 122.9301106387936, text="ALAWIHAOP2") 
            
            raw_coordinates.append([14.110115305360178, 122.9301106387936]) # 

            raw_routes.append(ALAWIHAOPR2)

        if i == 'ALAWIHAOP3':
            ALAWIHAOPR3 = map_widget.set_marker(14.1071302, 122.9266863, text="ALAWIHAOP3") 
            
            raw_coordinates.append([14.1071302, 122.9266863]) #14.1072151 122.9266099 

            raw_routes.append(ALAWIHAOPR3)

        if i == 'ALAWIHAOP4':
            ALAWIHAOPR41 = map_widget.set_marker(14.1063920, 122.9255939, text="ALAWIHAOP4")
            ALAWIHAOPR42 = map_widget.set_marker(14.1060704, 122.9241374, text="ALAWIHAOP4") #14.1063095 122.9223818
            ALAWIHAOPR43 = map_widget.set_marker(14.1063095, 122.9223818, text="ALAWIHAOP4")
            
            raw_coordinates.append([14.1063920, 122.9255939]) #14.1067043, 122.9184628
            raw_coordinates.append([14.1060704, 122.9241374])
            raw_coordinates.append([14.1063095, 122.9223818])

            raw_routes.append(ALAWIHAOPR41)
            raw_routes.append(ALAWIHAOPR42)
            raw_routes.append(ALAWIHAOPR43)
        
        if i == 'ALAWIHAOP6':
            ALAWIHAOPR6 = map_widget.set_marker(14.1067139, 122.9174642, text="ALAWIHAOP6")
            
            raw_coordinates.append([14.1067139, 122.9174642])
            
            raw_routes.append(ALAWIHAOPR6)

        if i == 'ALAWIHAOP8':
            ALAWIHAOPR8 = map_widget.set_marker(14.1066948, 122.9174276, text="ALAWIHAOP8")
            
            raw_coordinates.append([14.1066948, 122.9174276])
            
            raw_routes.append(ALAWIHAOPR8)
           
        if i == 'ALAWIHAOP5':
            ALAWIHAOPR5 = map_widget.set_marker(14.1055357, 122.9174664, text="ALAWIHAOP5")
            
            raw_coordinates.append([14.1055357, 122.9174664])
            
            raw_routes.append(ALAWIHAOPR5)

        if i == 'ALAWIHAOP8':
            ALAWIHAOPR8 = map_widget.set_marker(14.1060501, 122.9142542, text="ALAWIHAOP8")
            
            raw_coordinates.append([14.1060501, 122.9142542])
            
            raw_routes.append(ALAWIHAOPR8)

        if i == 'COBANGBANGP3':
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1123827, 122.9589967, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1092531, 122.9591187, text="")
            COBANGBANGR8 = map_widget.set_marker(14.1068418, 122.9604321, text="COBANGBANGP3")

            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1123827, 122.9589967])
            raw_coordinates.append([14.1092531, 122.9591187])
            raw_coordinates.append([14.1068418, 122.9604321])
            
            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)
            raw_routes.append(COBANGBANGR8)

        if i == 'COBANGBANGP2':
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1123827, 122.9589967, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1092531, 122.9591187, text="")
            COBANGBANGR8 = map_widget.set_marker(14.1068418, 122.9604321, text="")
            COBANGBANGR9 = map_widget.set_marker(14.1057139, 122.9609740, text="COBANGBANGP2")

            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1123827, 122.9589967])
            raw_coordinates.append([14.1092531, 122.9591187])
            raw_coordinates.append([14.1068418, 122.9604321])
            raw_coordinates.append([14.1057139, 122.9609740])

            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)
            raw_routes.append(COBANGBANGR8)
            raw_routes.append(COBANGBANGR9)

        if i == 'COBANGBANGP4':
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1123827, 122.9589967, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1092531, 122.9591187, text="")
            COBANGBANGR8 = map_widget.set_marker(14.1068418, 122.9604321, text="")
            COBANGBANGR9 = map_widget.set_marker(14.1057139, 122.9609740, text="")
            COBANGBANGR10 = map_widget.set_marker(14.1048514, 122.9616246, text="")
            COBANGBANGR11 = map_widget.set_marker(14.1039828, 122.9634231, text="")
            COBANGBANGR12 = map_widget.set_marker(14.1041027, 122.9636565, text="COBANGBANGP4")
            
            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1123827, 122.9589967])
            raw_coordinates.append([14.1092531, 122.9591187])
            raw_coordinates.append([14.1068418, 122.9604321])
            raw_coordinates.append([14.1057139, 122.9609740])
            raw_coordinates.append([14.1048514, 122.9616246])
            raw_coordinates.append([14.1039828, 122.9634231])
            raw_coordinates.append([14.1041027, 122.9636565])

            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)
            raw_routes.append(COBANGBANGR8)
            raw_routes.append(COBANGBANGR9)
            raw_routes.append(COBANGBANGR10)
            raw_routes.append(COBANGBANGR11)
            raw_routes.append(COBANGBANGR12)
 

        if i == 'COBANGBANGP5':
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1123827, 122.9589967, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1092531, 122.9591187, text="")
            COBANGBANGR8 = map_widget.set_marker(14.1068418, 122.9604321, text="")
            COBANGBANGR9 = map_widget.set_marker(14.1057139, 122.9609740, text="")
            COBANGBANGR10 = map_widget.set_marker(14.1048514, 122.9616246, text="")
            COBANGBANGR11 = map_widget.set_marker(14.1039100, 122.9635519, text="")
            COBANGBANGR12 = map_widget.set_marker(14.1035439, 122.9634229, text="COBANGBANGP5")

            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1123827, 122.9589967])
            raw_coordinates.append([14.1092531, 122.9591187])
            raw_coordinates.append([14.1068418, 122.9604321])
            raw_coordinates.append([14.1057139, 122.9609740])
            raw_coordinates.append([14.1048514, 122.9616246])
            raw_coordinates.append([14.1039100, 122.9635519])
            raw_coordinates.append([14.1035439, 122.9634229])

            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)
            raw_routes.append(COBANGBANGR8)
            raw_routes.append(COBANGBANGR9)
            raw_routes.append(COBANGBANGR10)
            raw_routes.append(COBANGBANGR11)
            raw_routes.append(COBANGBANGR12)

        if i == 'COBANGBANGP6':
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1051243, 122.9562600, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1050619, 122.9565872, text="COBANGBANGP6")


            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1051243, 122.9562600])
            raw_coordinates.append([14.1050619, 122.9565872])

            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)



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

alawihaop1_btn = Button(my_label, text="ALAWIHAOP1", command=lambda:Set('ALAWIHAOP1'))
alawihaop1_btn.pack(side="left")

alawihaop2_btn = Button(my_label, text="ALAWIHAOP2", command=lambda:Set('ALAWIHAOP2'))
alawihaop2_btn.pack(side="left")

alawihaop3_btn = Button(my_label, text="ALAWIHAOP3", command=lambda:Set('ALAWIHAOP3'))
alawihaop3_btn.pack(side="left")

alawihaop4_btn = Button(my_label, text="ALAWIHAOP4", command=lambda:Set('ALAWIHAOP4'))
alawihaop4_btn.pack(side="left")

alawihaop5_btn = Button(my_label, text="ALAWIHAOP5", command=lambda:Set('ALAWIHAOP5'))
alawihaop5_btn.pack(side="left")

alawihaop6_btn = Button(my_label, text="ALAWIHAOP6", command=lambda:Set('ALAWIHAOP6'))
alawihaop6_btn.pack(side="left")

alawihaop7_btn = Button(my_label, text="ALAWIHAOP7", command=lambda:Set('ALAWIHAOP7'))
alawihaop7_btn.pack(side="left")

alawihaop8_btn = Button(my_label, text="ALAWIHAOP8", command=lambda:Set('ALAWIHAOP8'))
alawihaop8_btn.pack(side="left")

alawihaop9_btn = Button(my_label, text="ALAWIHAOP9", command=lambda:Set('ALAWIHAOP9'))
alawihaop9_btn.pack(side="left")

alawihaop10_btn = Button(my_label, text="ALAWIHAOP10", command=lambda:Set('ALAWIHAOP10'))
alawihaop10_btn.pack(side="left")


# COBANGBANG

cobangbangp1_btn = Button(my_label, text="COBANGBANGP1", command=lambda:Set('COBANGBANGP1'))
cobangbangp1_btn.pack(side="bottom")

cobangbangp2_btn = Button(my_label, text="COBANGBANGP2", command=lambda:Set('COBANGBANGP2'))
cobangbangp2_btn.pack(side="bottom")

cobangbangp3_btn = Button(my_label, text="COBANGBANGP3", command=lambda:Set('COBANGBANGP3'))
cobangbangp3_btn.pack(side="bottom")

cobangbangp4_btn = Button(my_label, text="COBANGBANGP4", command=lambda:Set('COBANGBANGP4'))
cobangbangp4_btn.pack(side="bottom")

cobangbangp5_btn = Button(my_label, text="COBANGBANGP5", command=lambda:Set('COBANGBANGP5'))
cobangbangp5_btn.pack(side="bottom")

cobangbangp6_btn = Button(my_label, text="COBANGBANGP6", command=lambda:Set('COBANGBANGP6'))
cobangbangp6_btn.pack(side="bottom")



remove_coordinates_button = Button(root, text="Reset", background="black", fg="gold", width=10, height=2, command=RemoveCoordinates)
canvas.create_window(1130, 600, window=remove_coordinates_button)

root.mainloop()
