from tkinter import *
from tkinter import ttk  # Import the ttk module for themed widgets
import tkintermapview
from DijsktraAlgo import GetShortestPath

paths_list = []

routes_label_list = []


# Get location
all_barangay = ["Alawihao", "Bibirao", "Camambugan", 
                "Lagon",  "Pasig", "Gahonon", 
                "Mancruz", "Pamorangon", "Cobangbang"]

all_lagon_purok = ["LAGON", "LAGONP1", "LAGONP2",
                    "LAGONP3", "LAGONP4", "LAGONP5",
                   "LAGONP6", "LAGONP7"]

all_camambugan_purok = ["CAMAMBUGANP1", "CAMAMBUGANP2", "CAMAMBUGANP3",
                    "CAMAMBUGANP4", "CAMAMBUGANP5", "CAMAMBUGANP6",
                   "CAMAMBUGANP7"]

def show_notifier(message):
    notifier_window = Toplevel(root)
    notifier_window.title("Notifier")
    notifier_window.geometry("300x500+400+300")  # Adjust the size and position as needed

    full_message = '\n'.join(message)
    
    label1 = ttk.Label(notifier_window, text='Route details:', font=('century gothic', 12))
    label1.pack(pady=20)

    label = ttk.Label(notifier_window, text=full_message, font=('century gothic', 12))
    label.pack(pady=20)

    ok_button = ttk.Button(notifier_window, text="OK", command=notifier_window.destroy)
    ok_button.pack()

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
        


        
    return raw_routes, raw_coordinates

# ----> Algorithm Pang determine ng destination <-------------------

def Set(destination):
    global specific_routes_label, specific_routes_label

    destination_routes, shortest_distance_path = GetShortestPath("BFP", destination)

    routes, coordinates = GetCoordinates(destination_routes)

    
    view_btn['command'] = lambda:show_notifier(destination_routes)

    y_axis = 450
    for i in destination_routes:
        specific_routes_label = canvas.create_text(160, y_axis, text=i, anchor='center', fill='white', font=('courier new', 10))
        y_axis+=30
        routes_label_list.append(specific_routes_label)

    canvas.itemconfig(routes_label, text=f"Routes: ")
    canvas.itemconfig(total_distance_label, text=f"Total Distance: {(shortest_distance_path)} meters")

    print(coordinates)

    for i in range(len(coordinates) - 1):
        path_1 = map_widget.set_path([routes[i].position, routes[i+1].position, coordinates[i]])


    view_btn['state'] = 'normal'

# ----> Algorithm Pang reset ng lahat ng fields <-------------------

def RemoveCoordinates():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()

    purok_combo_var.set("")
    barangay_combo_var.set("")

    canvas.itemconfig(routes_label, text=f"")
    canvas.itemconfig(total_distance_label, text=f"")
    canvas.itemconfig(barangay_combo_var, text=f"")
    canvas.itemconfig(purok_combo_box, text=f"")

    for i in routes_label_list:
        canvas.itemconfig(i, text=f"")

# ----> Algorithm Pang determine kung nagfill up na sa barangay <-------------------
# ----> Dito rin maconditionals kung anong mga purok ng barangay <-------------------

def update_purok_combobox(*args):
    # Enable the purok_combobox if a barangay is selected
    barangayDestination = barangay_combo_var.get()

    if barangayDestination:
        purok_combo_box["state"] = "readonly"

            
        if barangayDestination == "Lagon":
            purok_combo_box["values"] = all_lagon_purok
        elif barangayDestination == "Camambugan":
            purok_combo_box["values"] = all_camambugan_purok
        else:
            purok_combo_box["state"] = "disabled"

    else:
        purok_combo_box.set("")  # Clear the selection
        purok_combo_box["state"] = "disabled"


def MainMenu():
    global root, canvas, map_widget, routes_label, total_distance_label, barangay_combo_var, purok_combo_box, purok_combo_var, view_btn
    root = Tk()
    root.title('Daet Map')
    root.geometry('1200x650+70+20')

    canvas = Canvas(root, width=1200, height=700, bg='#686362')
    canvas.pack()

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    text = "Details:"
    canvas.create_text(100, 380, text=text, anchor='center', fill='white', font=('courier new', 12))
    routes_label = canvas.create_text(160, 390, text="", anchor='center', fill='white', font=('courier new', 10))
    total_distance_label = canvas.create_text(160, 420, text="", anchor='center', fill='white', font=('courier new', 10))

    map_widget = tkintermapview.TkinterMapView(my_label, width=650, height=400, corner_radius=0)
    #map_widget.set_position(14.0996, 122.9550)

    canvas.create_window(830, 300, window=my_label)

    map_widget.set_address("Daet, Camarines Norte, Philippines")
    map_widget.set_zoom(14)
    map_widget.pack()


    # Add a ComboBox to the canvas 
    canvas.create_text(120, 120, text="Select barangay:", anchor='center', fill='white', font=('century gothic', 10))
    barangay_combo_var = StringVar()
    combo_box = ttk.Combobox(canvas, textvariable=barangay_combo_var, values=all_barangay, width=30, height=3, font=('century gothic', 10))   
    canvas.create_window(190, 150, window=combo_box)

    canvas.create_text(105, 180, text="Select Purok:", anchor='center', fill='white', font=('century gothic', 10))
    purok_combo_var = StringVar()
    purok_combo_box = ttk.Combobox(canvas, textvariable=purok_combo_var, values=all_barangay, width=30, height=5, font=('century gothic', 10), state='disabled')   
    canvas.create_window(190, 210, window=purok_combo_box)

    # Bind the function to the <<ComboboxSelected>> event
    combo_box.bind("<<ComboboxSelected>>", update_purok_combobox)

    search_btn = Button(canvas, text="Search", command=lambda:Set(purok_combo_var.get()), width=30, height=1)
    canvas.create_window(190, 280, window=search_btn)

    view_btn = Button(canvas, text="View", command=lambda:show_notifier("Hey"), width=30, height=1, state="disabled")
    canvas.create_window(190, 340, window=view_btn)

    remove_coordinates_button = Button(root, text="Reset", fg="black", width=11, height=2, command=RemoveCoordinates)
    canvas.create_window(1110, 550, window=remove_coordinates_button)

    root.mainloop()

MainMenu()