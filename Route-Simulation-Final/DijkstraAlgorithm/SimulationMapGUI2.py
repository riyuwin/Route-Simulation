from tkinter import *
import tkinter as tk
from tkinter import ttk  # Import the ttk module for themed widgets
import tkintermapview
from DijsktraAlgo2 import GetShortestPath
from tkinter import PhotoImage
from PIL import Image, ImageTk


paths_list = []

routes_label_list = []

def get_index_by_purok(loc_list, purok):
    for location, puroks in loc_list.items():
        if purok in puroks:
            return puroks.index(purok)
    return None  # Kung hindi makita ang purok, pwede mong i-handle depende sa iyong pangangailangan


# get purok
all_purok = {
    'Awitan': ["Purok 1","Purok 2","Purok 3"], 
    'Alawihao': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7', 'Purok 8', 'Purok 9', 'Purok 10'],
    'Bibirao': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5'],
    'Dogongan': ['Purok 1', 'Purok 2','Purok 3','Purok 4','Purok 5','Purok 6'],
    'Bagasbas': ["Purok 1","Purok 2","Purok 3", "Purok 4","Purok 5","Purok 6"],
    'Barangay 3': ["Purok 1", "Purok 2", "Purok 3", "Purok 4", "Purok 5", "Purok 6"],
    'Barangay 1': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6","Purok 7","Purok 8"],
    'Barangay 5': ["Purok 1", "Purok 2", "Purok 3","Purok 4", "Purok 5", "Purok 6"],
    'Barangay 6': ["Purok 1", "Purok 2", "Purok 3","Purok 4", "Purok 5"],
    'Barangay 7': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7'],
    'Barangay 8': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7', 'Purok 8', 'Purok 9', 'Purok 10'],
    'Barangay Gubat': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5'],
    'Barangay 2': [ 'Purok 1','Purok 2','Purok 3', 'Purok 4', 'Purok 5', 'Purok 6',  'Purok 7',   'Purok 8', ],
    'Borabod': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6"],
    'Calasgasan': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
    'Camambugan': ["Purok 1", "Purok 2", "Purok 3","Purok 4", "Purok 5", "Purok 6","Purok 7"],
    'Cobangbang': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6"],
    'Gahonon': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
    'Lag-on': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6","Purok 7"],
    'Mantagbac': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7', 'Purok 8', 'Purok 9'],
    'Magang': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
    'Mambalite': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7'],
    'Mancruz': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4'],
    'Pamorangon': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
    'San Isidro': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
}


# get location
all_location = {
    'Awitan': ["AWITANP1","AWITANP2","AWITANP3"], 
    'Alawihao': ['ALAWIHAOP1', 'ALAWIHAOP2', 'ALAWIHAOP3', 'ALAWIHAOP4', 'ALAWIHAOP5', 'ALAWIHAOP6', 'ALAWIHAOP7', 'ALAWIHAOP8', 'ALAWIHAOP9', 'ALAWIHAOP10'],
    'Bagasbas': ["BAGASBASP1","BAGASBASP2","BAGASBASP3", "BAGASBASP4","BAGASBASP5","BAGASBASP6"],
    'Barangay 1': ["BRGY1P1","BRGY1P2","BRGY1P3","BRGY1P4","BRGY1P5","BRGY1P6","BRGY1P7","BRGY1P8"],
    'Barangay 2': [ 'BRGY2P1','BRGY2P2','BRGY2P3', 'BRGY2P4', 'BRGY2P5','BRGY2P6',  'BRGY2P7',   'BRGY2P8', ],
    'Barangay 3': ["BRGY3P1","BRGY3P2","BRGY3P3","BRGY3P4","BRGY3P5","BRGY3P6"],
    'Barangay 5': ["BRGY5P1", "BRGY5P2", "BRGY5P3","BRGY5P4", "BRGY5P5", "BRGY5P6"],
    'Barangay 6': ["BRGY6P1", "BRGY6P2", "BRGY6P3","BRGY6P4", "BRGY6P5"],
    'Barangay 7': ['BRGY7P1', 'BRGY7P2', 'BRGY7P3', 'BRGY7P4', 'BRGY7P5', 'BRGY7P6', 'BRGY7P7'],
    'Barangay 8': ['BRGY8P1', 'BRGY8P2', 'BRGY8P3', 'BRGY8P4', 'BRGY8P5', 'BRGY8P6', 'BRGY8P7', 'BRGY8P8', 'BRGY8P9', 'BRGY8P10'],
    'Barangay Gubat': ['BRGYGUBATP1GUYABANO', 'BRGYGUBATP2UBAS', 'BRGYGUBATP3BAYABAS', 'BRGYGUBATP4ATIS', 'BRGYGUBATP5TSIKO'],
    'Bibirao': ['BIBIRAOP1', 'BIBIRAOP2', 'BIBIRAOP3', 'BIBIRAOP4', 'BIBIRAOP5'],
    'Borabod': ["BORABODP1","BORABODP2","BORABODP3","BORABODP4","BORABODP5","BORABODP6"],
    'Calasgasan': ['CALASGASANP1', 'CALASGASANP2', 'CALASGASANP3', 'CALASGASANP4', 'CALASGASANP5', 'CALASGASANP6'],
    'Camambugan': ["CAMAMBUGANP1", "CAMAMBUGANP2", "CAMAMBUGANP3","CAMAMBUGANP4", "CAMAMBUGANP5", "CAMAMBUGANP6","CAMAMBUGANP7"],
    'Cobangbang': ["COBANGBANGP1","COBANGBANGP2","COBANGBANGP3","COBANGBANGP4","COBANGBANGP5","COBANGBANGP6"],
    'Dogongan': ['DOGONGANP1', 'DOGONGANP2','DOGONGANP3','DOGONGANP4','DOGONGANP5','DOGONGANP6'],
    'Gahonon': ['GAHONONP1', 'GAHONONP2', 'GAHONONP3', 'GAHONONP4', 'GAHONONP5', 'GAHONONP6'],
    'Lag-on': ["LAGONP1","LAGONP2","LAGONP3","LAGONP4","LAGONP5","LAGONP6","LAGONP7"],
    'Mambalite': ['MAMBALITEP1', 'MAMBALITEP2', 'MAMBALITEP3', 'MAMBALITEP4', 'MAMBALITEP5', 'MAMBALITEP6', 'MAMBALITEP7'],
    'Mantagbac': ['MANTAGBACP1', 'MANTAGBACP2', 'MANTAGBACP3', 'MANTAGBACP4', 'MANTAGBACP5', 'MANTAGBACP6', 'MANTAGBACP7', 'MANTAGBACP8', 'MANTAGBACP9'],
    'Magang': ['MAGANGP1', 'MAGANGP2', 'MAGANGP3', 'MAGANGP4', 'MAGANGP5', 'MAGANGP6'],
    'Pamorangon': ['PAMORANGONP1', 'PAMORANGONP2', 'PAMORANGONP3', 'PAMORANGONP4', 'PAMORANGONP5', 'PAMORANGONP6'],
    'Mancruz': ['MANCRUZP1', 'MANCRUZP2', 'MANCRUZP3', 'MANCRUZP4'],
    'San Isidro': ['SANISIDROP1', 'SANISIDROP2', 'SANISIDROP3', 'SANISIDROP4', 'SANISIDROP5', 'SANISIDROP6'],
}


firetruck_marker = None
def update_firetruck_position(coordinate, icon_image):
    global firetruck_marker

    if firetruck_marker:
        firetruck_marker.delete()  # Delete the existing marker
        firetruck_marker = None

    firetruck_marker = map_widget.set_marker(coordinate[0], coordinate[1], text="Firetruck", icon=icon_image, text_color="blue")

def create_firetruck_icon():
    global firetruck_icon

    original_image = Image.open("firetruck.png")
    resized_image = original_image.resize((50, 50))
    firetruck_icon = ImageTk.PhotoImage(resized_image)
    label = Label(root, image=firetruck_icon)
    label.pack()
 
def on_select(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, 'values')
    print(f'You selected: {values}') 

def all_on_select(event): 
     
    
    selected_item = all_tree.selection()
    if selected_item:
        item_values = all_tree.item(selected_item)['values']
        print(f"Selected item values: {item_values}")

        route_number = item_values[0].split(" ")[-1]

        new_path = selected_routes[int(route_number)]

        final_route = ['BFP']
        for i in new_path:
            print(i[0])
            final_route.append(i[0])

        GetCoordinates(final_route)    
        

def compute_response_time(total_distance_meters, traffic_condition, road_condition): 
    # Coefficients 
    a = 0.7
    b = 0.2
    c = 0.1

    # Formula 
    response_time = a * (total_distance_meters / 1000) + b * traffic_condition + c * road_condition

    return response_time

def path_notifier(all_paths):
    global all_tree, selected_routes

    selected_routes = all_paths

    # Create a Treeview widget with three columns
    tree = ttk.Treeview(notifier_window, columns=('Routes', 'Distance', 'Time Travel', 'Traffic Congestions', 'Road Conditions'), show='headings', height=14)

    # Define column headings
    tree.heading('Routes', text='Routes')
    tree.heading('Distance', text='Distance')
    tree.heading('Time Travel', text='Time Travel')
    tree.heading('Traffic Congestions', text='Traffic Congestions')
    tree.heading('Road Conditions', text='Road Conditions')

    # Set the width of each column
    tree.column('Routes', width=180)  # Adjust the width as needed
    tree.column('Distance', width=100)  # Adjust the width as needed
    tree.column('Time Travel', width=100)  # Adjust the width as needed
    tree.column('Traffic Congestions', width=80)  # Adjust the width as needed
    tree.column('Road Conditions', width=100)  # Adjust the width as needed
            
    routes_details = []

        
    for num, path in enumerate(all_paths, start=1):
        print(f'Route {num} Details:')
        
        for incident in path:
            total_distance = incident[1]
            total_duration = round(incident[2], 2) 
            avg_congestion = round(incident[3], 2)
            avg_conditions = round(incident[4], 2)
            
            response_time = round(compute_response_time(total_distance, avg_congestion, avg_conditions), 2)

            print(f"{incident[0]}, {total_distance}, Response Time: {response_time}, {total_duration}, {avg_congestion}, {avg_conditions}")

            routes_details.append((f"Route {num}. {incident[0]}", f"{incident[1]} meters", f"{response_time} mins", incident[3], f"{incident[4]}-lane road"))

        print('\n')

    '''for route_number, path in enumerate(all_paths, start=1):
        for sublist in path:
            print(f"Route {route_number}. {sublist[0]}", sublist[1], sublist[2], sublist[3], sublist[4])
            routes_details.append((f"Route {route_number}. {sublist[0]}", f"{sublist[1]} meters", f"{sublist[2]} mins", sublist[3], f"{sublist[4]}-lane road"))'''

    '''for i in all_paths:
        for index, k in enumerate(i):
            print(index+1, k[0], k[1], k[2], k[3], k[4])
            routes_details.append((f'{index+1}. {k[0]}', f'{k[1]}', f'{k[2]}', f'{k[3]}', f'{k[4]}'))
    '''
    
    for row in routes_details:
        tree.insert('', tk.END, values=row)

    # Pack the Treeview
    #tree.pack(pady=10)
    notifier_canvas.create_window(700, 320, window=tree)

    # Create a label for output
    listbox_label = tk.Label(root, text="")
    listbox_label.pack(pady=10)

    # Bind the event handler for item selection
    tree.bind("<ButtonRelease-1>", on_select)

    # ----------------- NEW ---------------------------------------------

    # Create a Treeview widget with three columns
    all_tree = ttk.Treeview(notifier_window, columns=('Route', 'Total Distance', 'Total Response Time', 'Average Traffic Congestions', 'Average Road Conditions'), show='headings', height=14)

    # Define column headings
    all_tree.heading('Route', text='Route')
    all_tree.heading('Total Distance', text='Total Distance')
    all_tree.heading('Total Response Time', text='Total Response Time')
    all_tree.heading('Average Traffic Congestions', text='Average Traffic Congestions')
    all_tree.heading('Average Road Conditions', text='Average Road Conditions')

    # Set the width of each column
    all_tree.column('Route', width=150)  # Adjust the width as needed
    all_tree.column('Total Distance', width=100)  # Adjust the width as needed
    all_tree.column('Total Response Time', width=100)  # Adjust the width as needed
    all_tree.column('Average Traffic Congestions', width=130)  # Adjust the width as needed
    all_tree.column('Average Road Conditions', width=100)  # Adjust the width as needed
             
    routes_total_details = []
    # Initialize a variable to store the route number
    route_number = 1

    min_response_time = float('inf')  # In
    route_num_response_time = float('inf')

    min_total_response_time = float('inf')  # Initialize to positive infinity
    min_route_details = None

    for num, path in enumerate(all_paths, start=1):
        print(f'Route {num} Details:')
        total_response_time = 0
        total_distance_ = []
        avg_congestion_ = []
        avg_conditions_ = []
        
        for incident in path:
            total_distance = incident[1]
            total_duration = round(incident[2], 2) 
            avg_congestion = round(incident[3], 2)
            avg_conditions = round(incident[4], 2)
                

            total_distance_.append(total_distance) 
            avg_congestion_.append(avg_congestion)
            avg_conditions_.append(avg_conditions)

            response_time = compute_response_time(total_distance, avg_congestion, avg_conditions)
            response_time = round(response_time, 2)

            print(f"{incident[0]}, {total_distance}, Response Time: {response_time}, {total_duration}, {avg_congestion}, {avg_conditions}")
            
            total_response_time += response_time
 

        print(f'Total Response Time for Route {num}: {total_response_time:.2f} {sum(total_distance_)} \n')
        routes_total_details.append((f'Route {num}', f'{sum(total_distance_)} meters', f'{total_response_time:.2f} mins', f'{round(sum(avg_congestion_[3] for sublist in path) / len(path), 2)}', f'{round(sum(avg_conditions_[2] for sublist in path) / len(path), 2)}')) 
                
        # Check for the minimum total response time
        if total_response_time < min_total_response_time:
            min_total_response_time = total_response_time
            min_route_details = f"Route {num}, Total Response Time: {total_response_time:.2f} {total_distance}"
                    
            destination_details = Label(notifier_window, text=f'Suggested shortest path: Route {num}', font=('century gothic', 10))
            notifier_canvas.create_window(400, 90, window=destination_details)
        
    '''for path in all_paths:
        # Calculate the sum of the second elements in each sublist
        total_distance = sum(sublist[1] for sublist in path)
        total_duration = round(sum(sublist[2] for sublist in path), 2) 
        avg_congestion = round(sum(sublist[2] for sublist in path) / len(path), 2)
        avg_conditions = round(sum(sublist[3] for sublist in path) / len(path), 2)
    
        response_time = compute_response_time(total_distance, avg_congestion, avg_conditions)

        # Round response_time to two decimal places
        response_time = round(response_time, 2)

        # Print the route number and total distance
        print(f"Route {route_number}: Total Distance: {total_distance}")
        # Print the route number and total distance
        print(f"Route {route_number}: Total Duration: {total_duration}")
        # Print the route number and averages
        print(f"Route {route_number}: Average Congestion = {avg_congestion}, Average Conditions = {avg_conditions}")

        routes_total_details.append((f'Route {route_number}', f'{total_distance} meters', f'{response_time} mins', f'{avg_congestion}', f'{avg_conditions}')) 
        
        # Check if current response_time is the new minimum
        if response_time < min_response_time:
            min_response_time = response_time
            route_num_response_time = route_number

        # Increment the route number
        route_number += 1'''


    for row in routes_total_details:
        all_tree.insert('', tk.END, values=row)

    # Pack the Treeview
    #tree.pack(pady=10)
    notifier_canvas.create_window(100, 320, window=all_tree)

    

    # Bind the event handler for item selection
    all_tree.bind("<ButtonRelease-1>", all_on_select)



def show_all_paths(all_paths, shortest_path_details, destination, barangay):
    global tree, listbox_label, routes_tree, notifier_window, notifier_canvas, distance_label
    print(shortest_path_details, 'asfsafas')

    # Create a Toplevel window
    notifier_window = Toplevel(root)
    notifier_window.title("Details")
    notifier_window.geometry("1250x500+50+100")  # Adjust the size and position as needed

    # Create a Canvas widget inside the Toplevel window
    notifier_canvas = Canvas(notifier_window, width=800, height=500)
    notifier_canvas.pack()

    distance_label = Label(notifier_window, text=f'Suggested Possible Path:', font=('century gothic', 12, 'bold'))
    notifier_canvas.create_window(400, 30, window=distance_label)

    total_paths_details = Label(notifier_window, text=f'Total Suggested Routes: {len(all_paths)}', font=('century gothic', 10))
    notifier_canvas.create_window(400, 60, window=total_paths_details)

    shortest_route = None
    min_total_time = float('inf')  # Set to positive infinity initially

    for route_number, path in enumerate(all_paths, start=1):
        total_time = sum(sublist[2] for sublist in path)
        
        print(f"Route {route_number}: Total Time = {total_time}")

        # Check if the current route has a smaller total time
        if total_time < min_total_time:
            min_total_time = total_time
            shortest_route = route_number

    print(f"The route with the shortest total time is Route {shortest_route} with a total time of {min_total_time} minutes")


    destination_details = Label(notifier_window, text=f'Route: From BFP to Barangay {barangay} {destination}', font=('century gothic', 10))
    notifier_canvas.create_window(400, 120, window=destination_details)


    path_notifier(all_paths)

    '''ok_button = ttk.Button(notifier_window, text="OK", command=notifier_window.destroy)
    ok_button.pack()'''


def show_notifier(all_paths, shortest_path_details, destination, route_only):
    global tree, listbox_label

    print(shortest_path_details, 'asfsafas')

    # Create a Toplevel window
    notifier_window = Toplevel(root)
    notifier_window.title("Details")
    notifier_window.geometry("1000x400+100+100")  # Adjust the size and position as needed

    # Create a Canvas widget inside the Toplevel window
    notifier_canvas = Canvas(notifier_window, width=800, height=500)
    notifier_canvas.pack()

    distance_label = Label(notifier_window, text=f'Suggested Shortest Possible Path:', font=('century gothic', 12, 'bold'))
    notifier_canvas.create_window(400, 30, window=distance_label)

    distance_label = Label(notifier_window, text='Details', font=('century gothic', 10, 'bold'))
    notifier_canvas.create_window(710, 100, window=distance_label)

    destination_details = Label(notifier_window, text=f'Route: From BFP to {destination}', font=('century gothic', 10))
    notifier_canvas.create_window(710, 140, window=destination_details)

    distance_details = Label(notifier_window, text=f'Total Distance: {shortest_path_details["Total Distance"]} meters', font=('century gothic', 10))
    notifier_canvas.create_window(710, 170, window=distance_details)

    avg_traffic_details = Label(notifier_window, text=f'Average Traffic Congestion: {shortest_path_details["Average Traffic Congestion"]}', font=('century gothic', 10))
    notifier_canvas.create_window(710, 240, window=avg_traffic_details)

    average_congestion = shortest_path_details["Average Traffic Congestion"]

    desc_traffic_details = Label(notifier_window, text='Traffic Description: ', font=('century gothic', 10))
    notifier_canvas.create_window(710, 270, window=desc_traffic_details)

    if 0 <= average_congestion < 1.99:
        desc_traffic_details.config(text="Traffic Description: Light")
    elif 2 <= average_congestion < 2.99:
        desc_traffic_details.config(text="Traffic Description: Moderate")
    elif 3 <= average_congestion <= 3:
        desc_traffic_details.config(text="Traffic Description: Heavy")


    # Create a Treeview widget with three columns
    tree = ttk.Treeview(notifier_window, columns=('Routes', 'Distance', 'Time Travel', 'Traffic Congestions', 'Road Conditions'), show='headings')

    # Define column headings
    tree.heading('Routes', text='Routes')
    tree.heading('Distance', text='Distance')
    tree.heading('Time Travel', text='Time Travel')
    tree.heading('Traffic Congestions', text='Traffic Congestions')
    tree.heading('Road Conditions', text='Road Conditions')

    # Set the width of each column
    tree.column('Routes', width=150)  # Adjust the width as needed
    tree.column('Distance', width=100)  # Adjust the width as needed
    tree.column('Time Travel', width=100)  # Adjust the width as needed
    tree.column('Traffic Congestions', width=130)  # Adjust the width as needed
    tree.column('Road Conditions', width=100)  # Adjust the width as needed

    routes_details = []

    total_time_travelled = []

    num = 1
    min_response_time = float('inf')  # Inisyal na value para sa minimum response time
    route_num_response_time = float('inf')  # Inisyal na value para sa minimum response time

    for num, (i) in enumerate(route_only):
        print(f'{num+1}. {i[0]}')

        response_time = compute_response_time(i[1], i[3], i[4])
    
        # Round response_time to two decimal places
        response_time = round(response_time, 2)
        total_time_travelled.append(response_time)

        routes_details.append((f'{num+1}. {i[0]}', f'{i[1]}', f'{i[2]}', f'{i[3]}', f'{i[4]}'))

        # Check if current response_time is the new minimum
        if response_time < min_response_time:
            min_response_time = response_time
            route_num_response_time = num

    for row in routes_details:
        tree.insert('', tk.END, values=row)

    # Pack the Treeview
    #tree.pack(pady=10)
    notifier_canvas.create_window(250, 200, window=tree)

    # Create a label for output
    listbox_label = tk.Label(root, text="")
    listbox_label.pack(pady=10)

    # Bind the event handler for item selection
    tree.bind("<ButtonRelease-1>", on_select)
    
    duration_details = Label(notifier_window, text=f'Total Response Time: {sum(total_time_travelled)} mins', font=('century gothic', 10))
    notifier_canvas.create_window(710, 200, window=duration_details)

    ok_button = ttk.Button(notifier_window, text="OK", command=notifier_window.destroy)
    ok_button.pack()

    

def GetCoordinates(routes):

    raw_routes = []
    raw_coordinates = []
    print("test", routes)


    for i in routes:


        if i == 'BFP':

            if routes[1] == "LAGONP4":
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="LAGONP4")

                raw_coordinates.append([14.1181492, 122.9458283])

                raw_routes.append(BFP)
            elif routes[1] == "LAGONP4R1":
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
                BFPR1 = map_widget.set_marker(14.1176889, 122.9459710, text="LAGONP4R1")
                BFPR2 = map_widget.set_marker(14.1191091, 122.9504383, text="LAGONP4R1")

                raw_coordinates.append([14.1181492, 122.9458283])
                raw_coordinates.append([14.1192002, 122.9503752])
                raw_coordinates.append([14.1191091, 122.9504383])

                raw_routes.append(BFP)
                raw_routes.append(BFPR1)
                raw_routes.append(BFPR2)

            else:
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
                BFPR1 = map_widget.set_marker(14.1176889, 122.9459710, text="")

                raw_coordinates.append([14.1181492, 122.9458283])
                raw_coordinates.append([14.1176889, 122.9459710])

                raw_routes.append(BFP)
                raw_routes.append(BFPR1)

        if i == 'LAGONP1':
            LAGONP1 = map_widget.set_marker(14.1168800, 122.9432159, text="LAGONP1")

            raw_coordinates.append([14.1168800, 122.9432159])

            raw_routes.append(LAGONP1)

        if i == 'LAGON':
            LAGON = map_widget.set_marker(14.1156366, 122.9409842, text="LAGON")

            raw_coordinates.append([14.1156366, 122.9409842])

            raw_routes.append(LAGON)

        if i == 'LAGONP2':
            LAGONP2R1 = map_widget.set_marker(14.1161958, 122.9407131, text="LAGONP2")
            LAGONP2R2 = map_widget.set_marker(14.1169251, 122.9413635, text="LAGONP2") 
            LAGONP2R3 = map_widget.set_marker(14.1191822, 122.9430729, text="LAGONP2") 

            raw_coordinates.append([14.1161958, 122.9407131])
            raw_coordinates.append([14.1169251, 122.9413635])
            raw_coordinates.append([14.1191822, 122.9430729]) 

            raw_routes.append(LAGONP2R1)
            raw_routes.append(LAGONP2R2) 
            raw_routes.append(LAGONP2R3) 

        if i == 'LAGONP7':
            LAGONP7 = map_widget.set_marker(14.1131212, 122.9366253, text="LAGONP7")

            raw_coordinates.append([14.1131212, 122.9366253])

            raw_routes.append(LAGONP7)


        if i == 'LAGONP5':

            LAGONP5R1 = map_widget.set_marker(14.1141365, 122.9384722, text="LAGONP5") 

            raw_coordinates.append([14.1141365, 122.9384722]) 

            raw_routes.append(LAGONP5R1) 

        if i == 'LAGONP4':
            LAGONP4 = map_widget.set_marker(14.1185202, 122.9472156, text="LAGONP4")
            LAGONP4R1 = map_widget.set_marker(14.1191716, 122.9469856, text="LAGONP4")
            LAGONP4R2 = map_widget.set_marker(14.1197948, 122.9467542, text="LAGONP4")
            LAGONP4R3 = map_widget.set_marker(14.1209412, 122.9475004, text="LAGONP4")


            raw_coordinates.append([14.1185202, 122.9472156])
            raw_coordinates.append([14.1191716, 122.9469856])
            raw_coordinates.append([14.1197948, 122.9467542])
            raw_coordinates.append([14.1209412, 122.9475004])



            raw_routes.append(LAGONP4)
            raw_routes.append(LAGONP4R1)
            raw_routes.append(LAGONP4R2)
            raw_routes.append(LAGONP4R3)


        if i == 'LAGONP3':
            LAGON3 = map_widget.set_marker(14.1209278, 122.9475108, text="LAGONP3")
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

            raw_coordinates.append([14.110115305360178, 122.9301106387936])  #

            raw_routes.append(ALAWIHAOPR2)

        if i == 'ALAWIHAOP3':
            ALAWIHAOPR3 = map_widget.set_marker(14.1071302, 122.9266863, text="ALAWIHAOP3")

            raw_coordinates.append([14.1071302, 122.9266863])  # 14.1072151 122.9266099

            raw_routes.append(ALAWIHAOPR3)

        if i == 'ALAWIHAOP4':
            ALAWIHAOPR41 = map_widget.set_marker(14.1063920, 122.9255939, text="ALAWIHAOP4")
            ALAWIHAOPR42 = map_widget.set_marker(14.1060704, 122.9241374, text="ALAWIHAOP4")  # 14.1063095 122.9223818
            ALAWIHAOPR43 = map_widget.set_marker(14.1063095, 122.9223818, text="ALAWIHAOP4")

            raw_coordinates.append([14.1063920, 122.9255939])  # 14.1067043, 122.9184628
            raw_coordinates.append([14.1060704, 122.9241374])
            raw_coordinates.append([14.1063095, 122.9223818])

            raw_routes.append(ALAWIHAOPR41)
            raw_routes.append(ALAWIHAOPR42)
            raw_routes.append(ALAWIHAOPR43)

        if i == 'ALAWIHAOP6':
            ALAWIHAOPR6 = map_widget.set_marker(14.1071629, 122.9175127, text="ALAWIHAOP6")
            ALAWIHAOPR2 = map_widget.set_marker(14.1082933, 122.9178748, text="ALAWIHAOP6")
            ALAWIHAOPR3 = map_widget.set_marker(14.1082942, 122.9178809, text="ALAWIHAOP6")
            ALAWIHAOPR4 = map_widget.set_marker(14.1095697, 122.9182075, text="ALAWIHAOP6")

            raw_coordinates.append([14.1071629, 122.9175127])
            raw_coordinates.append([14.1082933, 122.9178748])
            raw_coordinates.append([14.1082942, 122.9178809])
            raw_coordinates.append([14.1095697, 122.9182075])

            raw_routes.append(ALAWIHAOPR6)
            raw_routes.append(ALAWIHAOPR2)
            raw_routes.append(ALAWIHAOPR3)
            raw_routes.append(ALAWIHAOPR4)

        if i == 'ALAWIHAOP5':
            ALAWIHAOPR5 = map_widget.set_marker(14.1066927, 122.9174750, text="ALAWIHAOP5")

            raw_coordinates.append([14.1066927, 122.9174750])
            raw_routes.append(ALAWIHAOPR5)

        if i == 'ALAWIHAOP5':
            ALAWIHAOPR5 = map_widget.set_marker(14.1066927, 122.9174750, text="ALAWIHAOP5")

            raw_coordinates.append([14.1066927, 122.9174750])
            raw_routes.append(ALAWIHAOPR5)

        if i == 'ALAWIHAOP7':
            ALAWIHAOPR1 = map_widget.set_marker(14.1103463, 122.9184194, text="ALAWIHAOP7")
            ALAWIHAOPR2 = map_widget.set_marker(14.1104035, 122.9189075, text="ALAWIHAOP7")
            ALAWIHAOPR3 = map_widget.set_marker(14.1103619, 122.9191650, text="ALAWIHAOP7")
            ALAWIHAOPR4 = map_widget.set_marker(14.1106221, 122.9192380, text="ALAWIHAOP7")
            ALAWIHAOPR5 = map_widget.set_marker(14.1110695, 122.9186747, text="ALAWIHAOP7")
            ALAWIHAOPR6 = map_widget.set_marker(14.1115402, 122.9192719, text="ALAWIHAOP7")

            raw_coordinates.append([14.1103463, 122.9184194])
            raw_coordinates.append([14.1104035, 122.9189075])
            raw_coordinates.append([14.1103619, 122.9191650])
            raw_coordinates.append([14.1106221, 122.9192380])
            raw_coordinates.append([14.1110695, 122.9186747])
            raw_coordinates.append([14.1115402, 122.9192719])

            raw_routes.append(ALAWIHAOPR1)
            raw_routes.append(ALAWIHAOPR2)
            raw_routes.append(ALAWIHAOPR3)
            raw_routes.append(ALAWIHAOPR4)
            raw_routes.append(ALAWIHAOPR5)
            raw_routes.append(ALAWIHAOPR6)

        if i == 'ALAWIHAOP8':
            ALAWIHAOPR1 = map_widget.set_marker(14.1066268, 122.9161801, text="ALAWIHAOP8")
            ALAWIHAOPR2 = map_widget.set_marker(14.1060501, 122.9142848, text="ALAWIHAOP8")

            raw_coordinates.append([14.1066268, 122.9161801])
            raw_coordinates.append([14.1060501, 122.9142848])

            raw_routes.append(ALAWIHAOPR1)
            raw_routes.append(ALAWIHAOPR2)

        if i == 'ALAWIHAOP9':
            ALAWIHAOPR1 = map_widget.set_marker(14.1049793, 122.9110073, text="ALAWIHAOP10")

            raw_coordinates.append([14.1049793, 122.9110073])

            raw_routes.append(ALAWIHAOPR1) 

        if i == 'ALAWIHAOP10':
            ALAWIHAOPR1 = map_widget.set_marker(14.1084846, 122.9134482, text="ALAWIHAOP10")

            raw_coordinates.append([14.1084846, 122.9134482])

            raw_routes.append(ALAWIHAOPR1)  

        if i == 'DOGONGANP1':

            DOGONGANR1 = map_widget.set_marker(14.1031087, 122.9073333, text="DOGONGANP1")
            DOGONGANR2 = map_widget.set_marker(14.1027602, 122.9046792, text="DOGONGANP1")

            raw_coordinates.append([14.1031087, 122.9073333]) 
            raw_coordinates.append([14.1027602, 122.9046792])

            raw_routes.append(DOGONGANR1) 
            raw_routes.append(DOGONGANR2) 

        if i == 'DOGONGANP2':

            DOGONGANR1 = map_widget.set_marker(14.1021100, 122.9045912, text="DOGONGANP2")   
            DOGONGANR2 = map_widget.set_marker(14.1018365, 122.9046882, text="DOGONGANP2")   
            DOGONGANR3 = map_widget.set_marker(14.1016788, 122.9049055, text="DOGONGANP2")   
            DOGONGANR4 = map_widget.set_marker(14.1009388, 122.9049403, text="DOGONGANP2")   
            DOGONGANR5 = map_widget.set_marker(14.1006788, 122.9048920, text="DOGONGANP2")   
            DOGONGANR6 = map_widget.set_marker(14.1000201, 122.9046958, text="DOGONGANP2")    
            DOGONGANR7 = map_widget.set_marker(14.0989902, 122.9049332, text="DOGONGANP2")   
            DOGONGANR8 = map_widget.set_marker(14.0983359, 122.9048474, text="DOGONGANP2")   
            DOGONGANR9 = map_widget.set_marker(14.0978906, 122.9041285, text="DOGONGANP2")   
            DOGONGANR10 = map_widget.set_marker(14.0976333, 122.9039458, text="DOGONGANP2")   

            raw_coordinates.append([14.1021100, 122.9045912])   
            raw_coordinates.append([14.1018365, 122.9046882])
            raw_coordinates.append([14.1016788, 122.9049055])   
            raw_coordinates.append([14.1009388, 122.9049403])   
            raw_coordinates.append([14.1006788, 122.9048920])    
            raw_coordinates.append([14.1000201, 122.9046958])    
            raw_coordinates.append([14.0989902, 122.9049332])   
            raw_coordinates.append([14.0983359, 122.9048474])     
            raw_coordinates.append([14.0978906, 122.9041285])     
            raw_coordinates.append([14.0976333, 122.9039458])    

            raw_routes.append(DOGONGANR1)      
            raw_routes.append(DOGONGANR2)   
            raw_routes.append(DOGONGANR3)   
            raw_routes.append(DOGONGANR4)   
            raw_routes.append(DOGONGANR5)   
            raw_routes.append(DOGONGANR6)   
            raw_routes.append(DOGONGANR7)     
            raw_routes.append(DOGONGANR8)      
            raw_routes.append(DOGONGANR9)      
            raw_routes.append(DOGONGANR10)      

        if i == 'DOGONGANP3':

            DOGONGANR1 = map_widget.set_marker(14.1028139, 122.9037973, text="DOGONGANP3")
            DOGONGANR2 = map_widget.set_marker(14.1029242, 122.9035027, text="DOGONGANP3")

            raw_coordinates.append([14.1028139, 122.9037973]) 
            raw_coordinates.append([14.1029242, 122.9035027])

            raw_routes.append(DOGONGANR1) 
            raw_routes.append(DOGONGANR2) 

        if i == 'DOGONGANP4':

            DOGONGANR1 = map_widget.set_marker(14.0973709, 122.9040883, text="DOGONGANP4")
            DOGONGANR2 = map_widget.set_marker(14.0965205, 122.9043056, text="DOGONGANP4")

            raw_coordinates.append([14.0973709, 122.9040883]) 
            raw_coordinates.append([14.0965205, 122.9043056])

            raw_routes.append(DOGONGANR1) 
            raw_routes.append(DOGONGANR2) 

        if i == 'DOGONGANP5':

            DOGONGANR1 = map_widget.set_marker(14.0970865, 122.9036282, text="DOGONGANP5")
            DOGONGANR2 = map_widget.set_marker(14.0963353, 122.9028946, text="DOGONGANP5")

            raw_coordinates.append([14.0970865, 122.9036282]) 
            raw_coordinates.append([14.0963353, 122.9028946])

            raw_routes.append(DOGONGANR1) 
            raw_routes.append(DOGONGANR2) 
        
        if i == 'DOGONGANP6':

            DOGONGANR1 = map_widget.set_marker(14.1022798, 122.9032748, text="DOGONGANP6")
            DOGONGANR2 = map_widget.set_marker(14.1020327,122.9030629, text="DOGONGANP6")
            DOGONGANR3 = map_widget.set_marker(14.1018948, 122.9024709, text="DOGONGANP6")
            DOGONGANR4 = map_widget.set_marker(14.1017465, 122.9021034, text="DOGONGANP6")
            DOGONGANR5 = map_widget.set_marker(14.1010871, 122.9012607, text="DOGONGANP6")

            raw_coordinates.append([14.1022798, 122.9032748]) 
            raw_coordinates.append([14.1020327,122.9030629]) 
            raw_coordinates.append([14.1018948, 122.9024709]) 
            raw_coordinates.append([14.1017465, 122.9021034]) 
            raw_coordinates.append([14.1010871, 122.9012607])

            raw_routes.append(DOGONGANR1) 
            raw_routes.append(DOGONGANR2) 
            raw_routes.append(DOGONGANR3) 
            raw_routes.append(DOGONGANR4) 
            raw_routes.append(DOGONGANR5) 

# Camambugan coordinates ->
        if i == 'CAMAMBUGANP1':
            CAMAMBUGANP1 = map_widget.set_marker(14.1061920, 122.9497664, text="Camambugan P-1")

            raw_coordinates.append([14.1088772, 122.9475911])

            raw_routes.append(CAMAMBUGANP1)

            # Camambugan coordinates ->
        if i == 'CAMAMBUGANP7':
            CAMAMBUGANP7R1 = map_widget.set_marker(14.1139334, 122.9419680, text="")
            CAMAMBUGANP7R2 = map_widget.set_marker(14.1111761, 122.9450376, text="Camambugan P-7")

            raw_coordinates.append([14.1111761, 122.9450376])
            raw_coordinates.append([14.1111761, 122.9450376])

            raw_routes.append(CAMAMBUGANP7R1)
            raw_routes.append(CAMAMBUGANP7R2)

        if i == 'CAMAMBUGANP2':
            CAMAMBUGANP2R1 = map_widget.set_marker(14.1083947, 122.9480392, text="")
            CAMAMBUGANP2R2 = map_widget.set_marker(14.1078806, 122.9484225, text="Camambugan P-2")

            raw_coordinates.append([14.1083947, 122.9480392])
            raw_coordinates.append([14.1078806, 122.9484225])  # 000

            raw_routes.append(CAMAMBUGANP2R1)
            raw_routes.append(CAMAMBUGANP2R2)

            print("HELlo")

        if i == 'CAMAMBUGANP3':
            print(routes)
            CAMAMBUGANP3R1 = map_widget.set_marker(14.1064985, 122.9495805, text="CAMAMBUGANP3")

            raw_coordinates.append([14.1064985, 122.9495805])

            raw_routes.append(CAMAMBUGANP3R1)

        if i == 'CAMAMBUGANP6':
            CAMAMBUGANP6R1 = map_widget.set_marker(14.1122305, 122.9460843, text="")
            CAMAMBUGANP6R2 = map_widget.set_marker(14.1119103, 122.9473046, text="")
            CAMAMBUGANP6R3 = map_widget.set_marker(14.1135712, 122.9475964, text="CAMAMBUGANP6")

            raw_coordinates.append([14.1122305, 122.9460843])
            raw_coordinates.append([14.1119103, 122.9473046])
            raw_coordinates.append([14.1135712, 122.9475964])

            raw_routes.append(CAMAMBUGANP6R1)
            raw_routes.append(CAMAMBUGANP6R2)
            raw_routes.append(CAMAMBUGANP6R3)

        if i == 'CAMAMBUGANP5':
            CAMAMBUGANP6R1 = map_widget.set_marker(14.1132455, 122.9518581, text="CAMAMBUGANP5")

            raw_coordinates.append([14.1132455, 122.9518581])

            raw_routes.append(CAMAMBUGANP6R1)

        if i == 'CAMAMBUGANP4':
            CAMAMBUGANP6R1 = map_widget.set_marker(14.1083327, 122.9493454, text="")
            CAMAMBUGANP6R2 = map_widget.set_marker(14.1095474, 122.9505229, text="")
            CAMAMBUGANP6R3 = map_widget.set_marker(14.1100439, 122.9518772, text="CAMAMBUGANP4")

            raw_coordinates.append([14.1083327, 122.9493454])
            raw_coordinates.append([14.1095474, 122.9505229])
            raw_coordinates.append([14.1100439, 122.9518772])

            raw_routes.append(CAMAMBUGANP6R1)
            raw_routes.append(CAMAMBUGANP6R2)
            raw_routes.append(CAMAMBUGANP6R3)

            # Camambugan coordinates ->
        if i == 'CAMAMBUGANP1':
            CAMAMBUGANP1 = map_widget.set_marker(14.1061920, 122.9497664, text="Camambugan P-1")

            raw_coordinates.append([14.1061920, 122.9497664])

            raw_routes.append(CAMAMBUGANP1)

    # Bibirao
        if i == 'BIBIRAOP1':
            BIBIRAOR1 = map_widget.set_marker(14.1045602, 122.9481039, text="")
            BIBIRAOR2 = map_widget.set_marker(14.1043600, 122.9477651, text="")
            BIBIRAOR3 = map_widget.set_marker(14.1042956, 122.9472044, text="CNNHS")
            BIBIRAOR4 = map_widget.set_marker(14.1043014, 122.9460733, text="")
            BIBIRAOR5 = map_widget.set_marker(14.1042442, 122.9451103, text="")
            BIBIRAOR6 = map_widget.set_marker(14.1042026, 122.9426933, text="")
            BIBIRAOR7 = map_widget.set_marker(14.1042182, 122.9422642, text="")
            BIBIRAOR8 = map_widget.set_marker(14.1039527, 122.9407885, text="")
            BIBIRAOR9 = map_widget.set_marker(14.1035799, 122.9397107, text="")
            BIBIRAOR10 = map_widget.set_marker(14.1025920, 122.9390187, text="")
            BIBIRAOR11 = map_widget.set_marker(14.1015790, 122.9372753, text="")
            BIBIRAOR12 = map_widget.set_marker(14.1007049, 122.9360867, text="")
            BIBIRAOR13 = map_widget.set_marker(14.1000777, 122.9354673, text="")
            BIBIRAOR14 = map_widget.set_marker(14.0999059, 122.9354112, text="BIBIRAOP1")

            raw_coordinates.append([14.1045602, 122.9481039])
            raw_coordinates.append([14.1043600, 122.9477651])
            raw_coordinates.append([14.1042956, 122.9472044])
            raw_coordinates.append([14.1043014, 122.9460733])
            raw_coordinates.append([14.1042442, 122.9451103])
            raw_coordinates.append([14.1042026, 122.9426933])
            raw_coordinates.append([14.1042182, 122.9422642])
            raw_coordinates.append([14.1039527, 122.9407885])
            raw_coordinates.append([14.1035799, 122.9397107])
            raw_coordinates.append([14.1025920, 122.9390187])
            raw_coordinates.append([14.1015790, 122.9372753])
            raw_coordinates.append([14.1007049, 122.9360867])
            raw_coordinates.append([14.1000777, 122.9354673])
            raw_coordinates.append([14.0999059, 122.9354112])

            raw_routes.append(BIBIRAOR1)
            raw_routes.append(BIBIRAOR2)
            raw_routes.append(BIBIRAOR3)
            raw_routes.append(BIBIRAOR4)
            raw_routes.append(BIBIRAOR5)
            raw_routes.append(BIBIRAOR6)
            raw_routes.append(BIBIRAOR7)
            raw_routes.append(BIBIRAOR8)
            raw_routes.append(BIBIRAOR9)
            raw_routes.append(BIBIRAOR10)
            raw_routes.append(BIBIRAOR11)
            raw_routes.append(BIBIRAOR12)
            raw_routes.append(BIBIRAOR13)
            raw_routes.append(BIBIRAOR14)

            # Bibirao
        if i == 'BIBIRAOP2':
            BIBIRAOP2R1 = map_widget.set_marker(14.0999456, 122.9335326, text="")
            BIBIRAOP2R2 = map_widget.set_marker(14.1000652, 122.9331035, text="")
            BIBIRAOP2R3 = map_widget.set_marker(14.1003722, 122.9329479, text="")
            BIBIRAOP2R4 = map_widget.set_marker(14.1006323, 122.9318601, text="BIBIRAOP2")

            raw_coordinates.append([14.0999456, 122.9335326])
            raw_coordinates.append([14.1000652, 122.9331035])
            raw_coordinates.append([14.1003722, 122.9329479])
            raw_coordinates.append([14.1006323, 122.9318601])

            raw_routes.append(BIBIRAOP2R1)
            raw_routes.append(BIBIRAOP2R2)
            raw_routes.append(BIBIRAOP2R3)
            raw_routes.append(BIBIRAOP2R4)

            # Bibirao
        if i == 'BIBIRAOP3':
            BIBIRAOP2R1 = map_widget.set_marker(14.1004397, 122.9308557, text="")
            BIBIRAOP2R2 = map_widget.set_marker(14.1001276, 122.9300188, text="")
            BIBIRAOP2R3 = map_widget.set_marker(14.0997139, 122.9302227, text="")
            BIBIRAOP2R4 = map_widget.set_marker(14.0993809, 122.9300438, text="")
            BIBIRAOP2R5 = map_widget.set_marker(14.0973925, 122.9290504, text="")
            BIBIRAOP2R6 = map_widget.set_marker(14.0972988, 122.9286266, text="")
            BIBIRAOP2R7 = map_widget.set_marker(14.0968555, 122.9280557, text="")
            BIBIRAOP2R8 = map_widget.set_marker(14.0964562, 122.9271413, text="")
            BIBIRAOP2R9 = map_widget.set_marker(14.0963870, 122.9268806, text="")
            BIBIRAOP2R10 = map_widget.set_marker(14.0952111, 122.9263066, text="")
            BIBIRAOP2R11 = map_widget.set_marker(14.0950966, 122.9261296, text="BIBIRAOP3")

            raw_coordinates.append([14.1004397, 122.9308557])
            raw_coordinates.append([14.1001276, 122.9300188])
            raw_coordinates.append([14.0997139, 122.9302227])
            raw_coordinates.append([14.0993809, 122.9300438])
            raw_coordinates.append([14.0973925, 122.9290504])
            raw_coordinates.append([14.0972988, 122.9286266])
            raw_coordinates.append([14.0968555, 122.9280557])
            raw_coordinates.append([14.0964562, 122.9271413])
            raw_coordinates.append([14.0963870, 122.9268806])
            raw_coordinates.append([14.0952111, 122.9263066])
            raw_coordinates.append([14.0950966, 122.9261296])

            raw_routes.append(BIBIRAOP2R1)
            raw_routes.append(BIBIRAOP2R2)
            raw_routes.append(BIBIRAOP2R3)
            raw_routes.append(BIBIRAOP2R4)
            raw_routes.append(BIBIRAOP2R5)
            raw_routes.append(BIBIRAOP2R6)
            raw_routes.append(BIBIRAOP2R7)
            raw_routes.append(BIBIRAOP2R8)
            raw_routes.append(BIBIRAOP2R9)
            raw_routes.append(BIBIRAOP2R10)
            raw_routes.append(BIBIRAOP2R11)

            # Bibirao
        if i == 'BIBIRAOP4':
            BIBIRAOP2R1 = map_widget.set_marker(14.0945343, 122.9258461, text="")
            BIBIRAOP2R2 = map_widget.set_marker(14.0944413, 122.9258374, text="")
            BIBIRAOP2R3 = map_widget.set_marker(14.0940610, 122.9251777, text="")
            BIBIRAOP2R4 = map_widget.set_marker(14.0933217, 122.9245107, text="")
            BIBIRAOP2R5 = map_widget.set_marker(14.0932472, 122.9242961, text="")
            BIBIRAOP2R6 = map_widget.set_marker(14.0933278, 122.9233063, text="")
            BIBIRAOP2R7 = map_widget.set_marker(14.0932321, 122.9225700, text="")
            BIBIRAOP2R8 = map_widget.set_marker(14.0926555, 122.9215785, text="BIBIRAOP4")

            raw_coordinates.append([14.0945343, 122.9258461])
            raw_coordinates.append([14.0944413, 122.9258374])
            raw_coordinates.append([14.0940610, 122.9251777])
            raw_coordinates.append([14.0933217, 122.9245107])
            raw_coordinates.append([14.0932472, 122.9242961])
            raw_coordinates.append([14.0933278, 122.9233063])
            raw_coordinates.append([14.0932321, 122.9225700])
            raw_coordinates.append([14.0926555, 122.9215785])

            raw_routes.append(BIBIRAOP2R1)
            raw_routes.append(BIBIRAOP2R2)
            raw_routes.append(BIBIRAOP2R3)
            raw_routes.append(BIBIRAOP2R4)
            raw_routes.append(BIBIRAOP2R5)
            raw_routes.append(BIBIRAOP2R6)
            raw_routes.append(BIBIRAOP2R7)
            raw_routes.append(BIBIRAOP2R8)

            # Bibirao
        if i == 'BIBIRAOP5':
            BIBIRAOP2R1 = map_widget.set_marker(14.0925572, 122.9207990)
            BIBIRAOP2R2 = map_widget.set_marker(14.0927915, 122.9201804)
            BIBIRAOP2R3 = map_widget.set_marker(14.0928435, 122.9198854)
            BIBIRAOP2R4 = map_widget.set_marker(14.0928071, 122.9197248)
            BIBIRAOP2R5 = map_widget.set_marker(14.0920527, 122.9181581)
            BIBIRAOP2R6 = map_widget.set_marker(14.0917302, 122.9172525)
            BIBIRAOP2R7 = map_widget.set_marker(14.0920059, 122.9160105)
            BIBIRAOP2R8 = map_widget.set_marker(14.0915272, 122.9150953)
            BIBIRAOP2R9 = map_widget.set_marker(14.0914676, 122.9142880)
            BIBIRAOP2R10 = map_widget.set_marker(14.0901224, 122.9126567, text="BIBIRAOP5")

            raw_coordinates.append([14.0925572, 122.9207990])
            raw_coordinates.append([14.0927915, 122.9201804])
            raw_coordinates.append([14.0928435, 122.9198854])
            raw_coordinates.append([14.0928071, 122.9197248])
            raw_coordinates.append([14.0920527, 122.9181581])
            raw_coordinates.append([14.0917302, 122.9172525])
            raw_coordinates.append([14.0920059, 122.9160105])
            raw_coordinates.append([14.0915272, 122.9150953])
            raw_coordinates.append([14.0914676, 122.9142880])
            raw_coordinates.append([14.0901224, 122.9126567])

            raw_routes.append(BIBIRAOP2R1)
            raw_routes.append(BIBIRAOP2R2)
            raw_routes.append(BIBIRAOP2R3)
            raw_routes.append(BIBIRAOP2R4)
            raw_routes.append(BIBIRAOP2R5)
            raw_routes.append(BIBIRAOP2R6)
            raw_routes.append(BIBIRAOP2R7)
            raw_routes.append(BIBIRAOP2R8)
            raw_routes.append(BIBIRAOP2R9)
            raw_routes.append(BIBIRAOP2R10)

        if i == 'MAGANGP1':
            MAGANGP1 = map_widget.set_marker(14.1025882, 122.9530922, text="Magang P-1")
            raw_coordinates.append([14.1025882, 122.9530922])

            raw_routes.append(MAGANGP1)

        if i == 'MAGANGP2R1':
            MAGANGP2R1 = map_widget.set_marker(14.1008177, 122.9548042, text="Magang P-2") 

            raw_coordinates.append([14.1008177, 122.9548042]) 

            raw_routes.append(MAGANGP2R1) 

        if i == 'MAGANGP2': 
            MAGANGP2 = map_widget.set_marker(14.0974184, 122.9492379, text="Magang P-2")
 
            raw_coordinates.append([14.0974184, 122.9492379])

            raw_routes.append(MAGANGP2)

        if i == 'MAGANGP3':
            MAGANGP3R1 = map_widget.set_marker(14.0974189, 122.9492852)
            MAGANGP3 = map_widget.set_marker(14.099893691324574, 122.94837909876821, text="Magang P-3")

            raw_coordinates.append([14.0974189, 122.9492852])
            raw_coordinates.append([14.099893691324574, 122.94837909876821])

            raw_routes.append(MAGANGP3R1)
            raw_routes.append(MAGANGP3)

        if i == 'MAGANGP4':
            MAGANGP4R1 = map_widget.set_marker(14.099893691324574, 122.94837909876821)
            MAGANGP4 = map_widget.set_marker(14.1013062, 122.9506929, text="Magang P-4")

            raw_coordinates.append([14.1013062, 122.9506929])
            raw_coordinates.append([14.099893691324574, 122.94837909876821])

            raw_routes.append(MAGANGP4R1)
            raw_routes.append(MAGANGP4)

        if i == 'MAGANGP5':
            MAGANGP5 = map_widget.set_marker(14.0952499, 122.9466356, text="Magang P-5")

            raw_coordinates.append([14.0952499, 122.9466356])

            raw_routes.append(MAGANGP5)

        if i == 'MAGANGP6':
            MAGANGP6 = map_widget.set_marker(14.093771429391841, 122.94453425116983, text="Magang P-6")

            raw_coordinates.append([14.093771429391841, 122.94453425116983])

            raw_routes.append(MAGANGP6)

        if i == 'CALASGASANP1':
            CALASGASANP1 = map_widget.set_marker(14.0918129, 122.9422421, text="Calasgasan P-1")

            raw_coordinates.append([14.0918129, 122.9422421])

            raw_routes.append(CALASGASANP1)

        if i == 'CALASGASANP2':
            CALASGASANP1 = map_widget.set_marker(14.0897599, 122.9403186, text="Calasgasan P-2")

            raw_coordinates.append([14.0897599, 122.9403186])

            raw_routes.append(CALASGASANP1)

        
        if i == 'CALASGASANP3':
            CALASGASANP1 = map_widget.set_marker(14.0875122, 122.9381765, text="Calasgasan P-3")

            raw_coordinates.append([14.0875122, 122.9381765])

            raw_routes.append(CALASGASANP1)


        if i == 'CALASGASANP4':
            CALASGASANP1 = map_widget.set_marker(14.0858961, 122.9365731, text="Calasgasan P-4")

            raw_coordinates.append([14.0858961, 122.9365731])

            raw_routes.append(CALASGASANP1)


        if i == 'CALASGASANP5':
            CALASGASANP1 = map_widget.set_marker(14.0847408, 122.9353178, text="Calasgasan P-5")

            raw_coordinates.append([14.0847408, 122.9353178])

            raw_routes.append(CALASGASANP1)

        
        if i == 'CALASGASANP6':
            CALASGASANP1 = map_widget.set_marker(14.0819763, 122.9312213, text="Calasgasan P-6")
            CALASGASANP2 = map_widget.set_marker(14.0806240, 122.9263177, text="Calasgasan P-6")

            raw_coordinates.append([14.0819763, 122.9312213])
            raw_coordinates.append([14.0806240, 122.9263177])

            raw_routes.append(CALASGASANP1)
            raw_routes.append(CALASGASANP2)

        if i == 'MANCRUZP4':
            MANRCRUZP4R1 = map_widget.set_marker(14.0992103, 122.9563215, text="Mancruz P-4")
            MANRCRUZP4R2 = map_widget.set_marker(14.0986662, 122.9565453, text="Mancruz P-4")

            MANCRUZP4 = map_widget.set_marker(14.0981440, 122.9565617, text="Mancruz P-4")

            raw_coordinates.append([14.0992103, 122.9563215])
            raw_coordinates.append([14.0986662, 122.9565453])
            raw_coordinates.append([14.0981440, 122.9565617])

            raw_routes.append(MANRCRUZP4R1)
            raw_routes.append(MANRCRUZP4R2)
            raw_routes.append(MANCRUZP4)

        if i == 'MANCRUZP2':
            MANCRUZP2 = map_widget.set_marker(14.0969867, 122.9566183, text="Mancruz P-2")  #
            raw_coordinates.append([14.0969867, 122.9566183])
            raw_routes.append(MANCRUZP2)

        if i == 'MANCRUZP1':
            MANCRUZP1 = map_widget.set_marker(14.091255423325915, 122.95688903288227, text="Mancruz P-1")
            raw_coordinates.append([14.091255423325915, 122.95688903288227])
            raw_routes.append(MANCRUZP1)

        if i == 'MANCRUZP3':
            MANRCRUZP3R1 = map_widget.set_marker(14.0912982, 122.9564243, text="Pamorangon P-3")
            MANRCRUZP3R2 = map_widget.set_marker(14.0915791, 122.9563653, text="Pamorangon P-3")
            MANRCRUZP3R3 = map_widget.set_marker(14.0920940, 122.9551532, text="Pamorangon P-3")
            MANCRUZP3 = map_widget.set_marker(14.091702085263828, 122.95445844588974, text="Mancruz P-3")

            raw_coordinates.append([14.0912982, 122.9564243])
            raw_coordinates.append([14.0915791, 122.9563653])
            raw_coordinates.append([14.0920940, 122.9551532])
            raw_coordinates.append([14.091702085263828, 122.95445844588974])

            raw_routes.append(MANRCRUZP3R1)
            raw_routes.append(MANRCRUZP3R2)
            raw_routes.append(MANRCRUZP3R3)
            raw_routes.append(MANCRUZP3)


        if i == 'PAMORANGONP1':
            PAMORANGONP1R2 = map_widget.set_marker(14.09918256873587, 122.95653512316036, text="Pamorangon P-1")
            PAMORANGONP1R3 = map_widget.set_marker(14.0998925, 122.9565228, text="Pamorangon P-1")

            raw_coordinates.append([14.09918256873587, 122.95653512316036])

            raw_coordinates.append([14.0998925, 122.9565228])

            raw_routes.append(PAMORANGONP1R2)
            raw_routes.append(PAMORANGONP1R3)

        if i == 'PAMORANGONP2':
            PAMORANGONP2 = map_widget.set_marker(14.096943694822043, 122.95669766045388, text="Pamorangon P-2")

            raw_coordinates.append([14.096943694822043, 122.95669766045388])

            raw_routes.append(PAMORANGONP2)

        if i == 'PAMORANGONP3':
            PAMORANGONP3 = map_widget.set_marker(14.0904326, 122.9570458, text="Pamorangon P-3")

            raw_coordinates.append([14.0904326, 122.9570458])

            raw_routes.append(PAMORANGONP3)

        if i == 'PAMORANGONP4':
            PAMORANGONPR1 = map_widget.set_marker(14.0904744, 122.9579470, text="Pamorangon P-4")
            PAMORANGONPR2 = map_widget.set_marker(14.0909216, 122.9579904, text="Pamorangon P-4")
            PAMORANGONP4 = map_widget.set_marker(14.09300998788361, 122.95902296720664, text="Pamorangon P-4")

            raw_coordinates.append([14.0904744, 122.9579470])
            raw_coordinates.append([14.0909216, 122.9579904])
            raw_coordinates.append([14.09300998788361, 122.95902296720664])

            raw_routes.append(PAMORANGONPR1)
            raw_routes.append(PAMORANGONPR2)
            raw_routes.append(PAMORANGONP4)

        if i == 'PAMORANGONP5':
            PAMORANGONP5 = map_widget.set_marker(14.0903458, 122.9570227, text="Pamorangon P-5")

            raw_coordinates.append([14.0903458, 122.9570227])

            raw_routes.append(PAMORANGONP5)

        if i == 'PAMORANGONP6':
            PAMORANGONP6R1 = map_widget.set_marker(14.0903762, 122.9580091, text="Pamorangon P-6")
            PAMORANGONP6R2 = map_widget.set_marker(14.0903363, 122.9583052, text="Pamorangon P-6")
            PAMORANGONP6 = map_widget.set_marker(14.086770677594686, 122.96323398578951, text="Pamorangon P-6")

            raw_coordinates.append([14.0903762, 122.9580091])
            raw_coordinates.append([14.0903363, 122.9583052])
            raw_coordinates.append([14.086770677594686, 122.96323398578951])

            raw_routes.append(PAMORANGONP6R1)
            raw_routes.append(PAMORANGONP6R2)
            raw_routes.append(PAMORANGONP6)

        if i == 'BRGY5P1':
            #PAMORANGONP6R1 = map_widget.set_marker(14.1197996, 122.9493845, text="BRGY5P1") 
            PAMORANGONP6R2 = map_widget.set_marker(14.1208192, 122.9501033, text="BRGY5P1") 

            #raw_coordinates.append([14.1197996, 122.9493845]) 
            raw_coordinates.append([14.1208192, 122.9501033]) 

            #raw_routes.append(PAMORANGONP6R1) 
            raw_routes.append(PAMORANGONP6R2) 

        
        if i == 'BRGY5P2':
            BRGY5P1 = map_widget.set_marker(14.1163015, 122.9549350, text="BRGY5P2")  

            raw_coordinates.append([14.1163015, 122.9549350])  

            raw_routes.append(BRGY5P1)  

        if i == 'BRGY5P3':
            BRGY5P1 = map_widget.set_marker(14.1202044, 122.9511584, text="BRGY5P3")  

            raw_coordinates.append([14.1202044, 122.9511584])  

            raw_routes.append(BRGY5P1)  

        if i == 'BRGY5P3R1':
            BRGY5P1 = map_widget.set_marker(14.1198447, 122.9518162, text="BRGY5P3R1")  

            raw_coordinates.append([14.1198447, 122.9518162])  

            raw_routes.append(BRGY5P1)          
        
        if i == 'BRGY5P4':
            BRGY5P1 = map_widget.set_marker(14.1215112, 122.9523580, text="BRGY5P4")  

            raw_coordinates.append([14.1215112, 122.9523580])  

            raw_routes.append(BRGY5P1)          
        
        if i == 'BRGY5P5':
            BRGY5P1 = map_widget.set_marker(14.1230927, 122.9528032, text="BRGY5P5")  

            raw_coordinates.append([14.1230927, 122.9528032])  

            raw_routes.append(BRGY5P1)       
            
        if i == 'BRGY5P5R1':
            BRGY5P1 = map_widget.set_marker(14.1230949, 122.9536743, text="BRGY5P5R1")  

            raw_coordinates.append([14.1230949, 122.9536743])  

            raw_routes.append(BRGY5P1)       
            
        if i == 'BRGY5P5R2':
            BRGY5P1 = map_widget.set_marker(14.1221012, 122.9572944, text="BRGY5P5R2")
            BRGY5P2 = map_widget.set_marker(14.1221403, 122.9576303, text="BRGY5P5R2")  

            raw_coordinates.append([14.1221012, 122.9572944])  
            raw_coordinates.append([14.1221403, 122.9576303])  

            raw_routes.append(BRGY5P1)
            raw_routes.append(BRGY5P2)       
           
        if i == 'BRGY5P3R2':
            BRGY5P1 = map_widget.set_marker(14.1175384, 122.9556289, text="BRGY5P3R2")  

            raw_coordinates.append([14.1175384, 122.9556289])  

            raw_routes.append(BRGY5P1)  

        # MANTAGABAC
        if i == 'MANTAGBACP9':
            MANTAGBACP9 = map_widget.set_marker(14.1177123, 122.9460971, text="MANTAGBACP9")
            MANTAGBACP9R1 = map_widget.set_marker(14.1169254, 122.9463036, text="MANTAGBACP9")
            MANTAGBACP9R2 = map_widget.set_marker(14.1167239, 122.9462821, text="MANTAGBACP9")
            MANTAGBACP9R3 = map_widget.set_marker(14.1166536, 122.9468052, text="MANTAGBACP9")
            MANTAGBACP9R4 = map_widget.set_marker(14.1159503, 122.9472847, text="MANTAGBACP9")
            MANTAGBACP9R5 = map_widget.set_marker(14.1157874, 122.9475779, text="MANTAGBACP9")
            MANTAGBACP9R6 = map_widget.set_marker(14.1154143, 122.9475733, text="MANTAGBACP9")
            MANTAGBACP9R7 = map_widget.set_marker(14.1153250, 122.9477136, text="MANTAGBACP9")
            MANTAGBACP9R8 = map_widget.set_marker(14.1152331, 122.9476906, text="MANTAGBACP9")
            MANTAGBACP9R9 = map_widget.set_marker(14.1150695, 122.9482564, text="MANTAGBACP9")
            MANTAGBACP9R10 = map_widget.set_marker(14.1170267, 122.9496110, text="MANTAGBACP9")

            raw_coordinates.append([14.1177123, 122.9460971])
            raw_coordinates.append([14.1169254, 122.9463036])
            raw_coordinates.append([14.1167239, 122.9462821])
            raw_coordinates.append([14.1166536, 122.9468052])
            raw_coordinates.append([14.1159503, 122.9472847])
            raw_coordinates.append([14.1157874, 122.9475779])
            raw_coordinates.append([14.1154143, 122.9475733])
            raw_coordinates.append([14.1153250, 122.9477136])
            raw_coordinates.append([14.1152331, 122.9476906])
            raw_coordinates.append([14.1150695, 122.9482564])
            raw_coordinates.append([14.1170267, 122.9496110])

            raw_routes.append(MANTAGBACP9)
            raw_routes.append(MANTAGBACP9R1)
            raw_routes.append(MANTAGBACP9R2)
            raw_routes.append(MANTAGBACP9R3)
            raw_routes.append(MANTAGBACP9R4)
            raw_routes.append(MANTAGBACP9R5)
            raw_routes.append(MANTAGBACP9R6)
            raw_routes.append(MANTAGBACP9R7)
            raw_routes.append(MANTAGBACP9R8)
            raw_routes.append(MANTAGBACP9R9)
            raw_routes.append(MANTAGBACP9R10)
        
        # MANTAGABAC
        if i == 'MANTAGBACP9R1':
            MANTAGBACP9 = map_widget.set_marker(14.1164065, 122.9505256, text="MANTAGBACP9R1") 

            raw_coordinates.append([14.1164065, 122.9505256]) 

            raw_routes.append(MANTAGBACP9) 
        
        # MANTAGABAC
        if i == 'MANTAGBACP8':
            MANTAGBACP9 = map_widget.set_marker(14.1157878, 122.9515066, text="MANTAGBACP8") 

            raw_coordinates.append([14.1157878, 122.9515066]) 

            raw_routes.append(MANTAGBACP9) 

        # MANTAGABAC
        if i == 'MANTAGBACP4':
            MANTAGBACP9 = map_widget.set_marker(14.1167447, 122.9507026, text="MANTAGBACP4") 
            MANTAGBACP9R1 = map_widget.set_marker(14.1165158, 122.9512836, text="MANTAGBACP4") 
            MANTAGBACP9R2 = map_widget.set_marker(14.1164846, 122.9518410, text="MANTAGBACP4") 

            raw_coordinates.append([14.1167447, 122.9507026])
            raw_coordinates.append([14.1165158, 122.9512836])
            raw_coordinates.append([14.1164846, 122.9518410]) 

            raw_routes.append(MANTAGBACP9) 
            raw_routes.append(MANTAGBACP9R1) 
            raw_routes.append(MANTAGBACP9R2) 

        # MANTAGABAC
        if i == 'MANTAGBACP5':
            MANTAGBACP5 = map_widget.set_marker(14.1165569, 122.9521623, text="MANTAGBACP5")
            MANTAGBACP5R1 = map_widget.set_marker(14.1165517, 122.9525861, text="MANTAGBACP5")
            MANTAGBACP5R2 = map_widget.set_marker(14.1164585, 122.9530970, text="MANTAGBACP5")
            MANTAGBACP5R2 = map_widget.set_marker(14.1164595, 122.9534103, text="MANTAGBACP5")
            MANTAGBACP5R3 = map_widget.set_marker(14.1165599, 122.9535330, text="MANTAGBACP5")

            raw_coordinates.append([14.1165569, 122.9521623])
            raw_coordinates.append([14.1165517, 122.9525861])
            raw_coordinates.append([14.1164585, 122.9530970])
            raw_coordinates.append([14.1164595, 122.9534103])
            raw_coordinates.append([14.1165599, 122.9535330])
            
            raw_routes.append(MANTAGBACP5) 
            raw_routes.append(MANTAGBACP5R1) 
            raw_routes.append(MANTAGBACP5R2) 
            raw_routes.append(MANTAGBACP5R3) 

        # MANTAGABAC
        if i == 'MANTAGBACP3':
            MANTAGBACP9 = map_widget.set_marker(14.1157842, 122.9515031, text="MANTAGBACP3")

            raw_coordinates.append([14.1157842, 122.9515031])
            
            raw_routes.append(MANTAGBACP9) 

        # MANTAGABAC
        if i == 'MANTAGBACP6':
            MANTAGBACP9 = map_widget.set_marker(14.1165832, 122.9545596, text="MANTAGBACP6")

            raw_coordinates.append([14.1165832, 122.9545596])
            
            raw_routes.append(MANTAGBACP9) 

        # MANTAGABAC
        if i == 'MANTAGBACP2':
            MANTAGBACP9 = map_widget.set_marker(14.1146897, 122.9533764, text="MANTAGBACP2")

            raw_coordinates.append([14.1146897, 122.9533764])
            
            raw_routes.append(MANTAGBACP9) 
        
        # MANTAGABAC
        if i == 'MANTAGBACP1':
            MANTAGBACP9 = map_widget.set_marker(14.1144270, 122.9547175, text="MANTAGBACP1")

            raw_coordinates.append([14.1144270, 122.9547175])
            
            raw_routes.append(MANTAGBACP9) 

        
        # MANTAGABAC
        if i == 'MANTAGBACP2R1':
            MANTAGBACP9 = map_widget.set_marker(14.1161138, 122.9542087, text="MANTAGBACP2R1")

            raw_coordinates.append([14.1161138, 122.9542087])
            
            raw_routes.append(MANTAGBACP9) 
            

        
        # MANTAGABAC
        if i == 'BRGY6P4':
            MANTAGBACP9 = map_widget.set_marker(14.1150999, 122.9548041, text="BRGY6P4")

            raw_coordinates.append([14.1150999, 122.9548041])
            
            raw_routes.append(MANTAGBACP9) 
        
        # MANTAGABAC
        if i == 'BRGY6P3':
            MANTAGBACP9 = map_widget.set_marker(14.1175283, 122.9556293, text="BRGY6P3")

            raw_coordinates.append([14.1175283, 122.9556293])
            
            raw_routes.append(MANTAGBACP9) 

        # MANTAGABAC
        if i == 'BRGY6P2':
            MANTAGBACP9 = map_widget.set_marker(14.1188530, 122.9561174, text="BRGY6P2")
            MANTAGBACP9R1 = map_widget.set_marker(14.1195011, 122.9566700, text="BRGY6P2")

            raw_coordinates.append([14.1188530, 122.9561174])
            raw_coordinates.append([14.1195011, 122.9566700])
            
            raw_routes.append(MANTAGBACP9) 
            raw_routes.append(MANTAGBACP9R1) 


        # MANTAGABAC
        if i == 'BRGY6P5':
            MANTAGBACP9 = map_widget.set_marker(14.1205815, 122.9572065, text="BRGY6P2") 

            raw_coordinates.append([14.1205815, 122.9572065]) 
            
            raw_routes.append(MANTAGBACP9)  

        
        # MANTAGABAC
        if i == 'BRGY6P1':
            MANTAGBACP9 = map_widget.set_marker(14.1220340, 122.9579307, text="BRGY6P1") 

            raw_coordinates.append([14.1220340, 122.9579307]) 
            
            raw_routes.append(MANTAGBACP9)  

        # MANTAGABAC
        if i == 'GAHONONP3':
            GAHONONP3 = map_widget.set_marker(14.1220289, 122.9457446, text="GAHONONP3") 

            raw_coordinates.append([14.1220289, 122.9457446]) 
            
            raw_routes.append(GAHONONP3)  
            
        # MANTAGABAC
        if i == 'GAHONONP2':
            GAHONONP3 = map_widget.set_marker(14.1230290, 122.9441365, text="GAHONONP2") 

            raw_coordinates.append([14.1230290, 122.9441365]) 
            
            raw_routes.append(GAHONONP3)  

            
        # MANTAGABAC
        if i == 'GAHONONP1':
            GAHONONP3 = map_widget.set_marker(14.1257745, 122.9396880, text="GAHONONP1") 

            raw_coordinates.append([14.1257745, 122.9396880]) 
            
            raw_routes.append(GAHONONP3)  

        # MANTAGABAC
        if i == 'GAHONONP4':
            GAHONONP3 = map_widget.set_marker(14.1227090, 122.9458843, text="GAHONONP4") 
            GAHONONP3R1 = map_widget.set_marker(14.1234753, 122.9461434, text="GAHONONP4") 
            GAHONONP3R2 = map_widget.set_marker(14.1237704, 122.9463499, text="GAHONONP4") 
            GAHONONP3R3 = map_widget.set_marker(14.1235805, 122.9472392, text="GAHONONP4") 
            GAHONONP3R4 = map_widget.set_marker(14.1235869, 122.9479491, text="GAHONONP4") 
            GAHONONP3R5 = map_widget.set_marker(14.1236754, 122.9480564, text="GAHONONP4") 
            GAHONONP3R6 = map_widget.set_marker(14.1235661, 122.9483622, text="GAHONONP4")  
            GAHONONP3R7 = map_widget.set_marker(14.1242009, 122.9485768, text="GAHONONP4")  
            GAHONONP3R8 = map_widget.set_marker(14.1235975, 122.9504582, text="GAHONONP4") 


            raw_coordinates.append([14.1227090, 122.9458843]) 
            raw_coordinates.append([14.1234753, 122.9461434]) 
            raw_coordinates.append([14.1237704, 122.9463499]) 
            raw_coordinates.append([14.1235805, 122.9472392]) 
            raw_coordinates.append([14.1235869, 122.9479491]) 
            raw_coordinates.append([14.1236754, 122.9480564]) 
            raw_coordinates.append([14.1235661, 122.9483622]) 
            raw_coordinates.append([14.1242009, 122.9485768]) 
            raw_coordinates.append([14.1235975, 122.9504582]) 
            
            
            raw_routes.append(GAHONONP3) 
            raw_routes.append(GAHONONP3R1) 
            raw_routes.append(GAHONONP3R2) 
            raw_routes.append(GAHONONP3R3)  
            raw_routes.append(GAHONONP3R4)  
            raw_routes.append(GAHONONP3R5)  
            raw_routes.append(GAHONONP3R6)  
            raw_routes.append(GAHONONP3R7)  
            raw_routes.append(GAHONONP3R8)
            
               # MANTAGABAC
        if i == 'GAHONONP5':
            GAHONONP3 = map_widget.set_marker(14.1230031, 122.9523568, text="GAHONONP5") 
            #GAHONONP3R1 = map_widget.set_marker(14.1230811, 122.9528235, text="GAHONONP5") 

            raw_coordinates.append([14.1230031, 122.9523568]) 
            #raw_coordinates.append([14.1230811, 122.9528235]) 
            
            raw_routes.append(GAHONONP3)  
            #raw_routes.append(GAHONONP3R1)  
     
        # MANTAGABAC
        if i == 'GAHONONP6':
            GAHONONP3 = map_widget.set_marker(14.1242282, 122.9449436, text="GAHONONP6") 
            GAHONONP3R1 = map_widget.set_marker(14.1271758, 122.9494604, text="GAHONONP6") 
            GAHONONP3R2 = map_widget.set_marker(14.1310673, 122.9508123, text="GAHONONP6") 
            GAHONONP3R3 = map_widget.set_marker(14.1342093, 122.9512629, text="GAHONONP6") 
            GAHONONP3R4 = map_widget.set_marker(14.1375429, 122.9560915, text="GAHONONP6") 
            GAHONONP3R5 = map_widget.set_marker(14.1387795, 122.9591514, text="GAHONONP6") 

            raw_coordinates.append([14.1242282, 122.9449436]) 
            raw_coordinates.append([14.1271758, 122.9494604]) 
            raw_coordinates.append([14.1310673, 122.9508123]) 
            raw_coordinates.append([14.1342093, 122.9512629]) 
            raw_coordinates.append([14.1375429, 122.9560915]) 
            raw_coordinates.append([14.1387795, 122.9591514]) 
            
            raw_routes.append(GAHONONP3)                
            raw_routes.append(GAHONONP3R1)                
            raw_routes.append(GAHONONP3R2)                
            raw_routes.append(GAHONONP3R3)                
            raw_routes.append(GAHONONP3R4)                
            raw_routes.append(GAHONONP3R5)                

        # MANTAGABAC
        if i == 'AWITANP3': 
            GAHONONP3R5 = map_widget.set_marker(14.1387795, 122.9591514, text="AWITANP3") 

            raw_coordinates.append([14.1387795, 122.9591514]) 
                           
            raw_routes.append(GAHONONP3R5)                

        # MANTAGABAC
        if i == 'AWITANP2': 
            GAHONONP3R5 = map_widget.set_marker(14.1387376, 122.9592433, text="AWITANP2") 
            GAHONONP3R1 = map_widget.set_marker(14.1393359, 122.9605952, text="AWITANP2") 

            raw_coordinates.append([14.1387376, 122.9592433]) 
            raw_coordinates.append([14.1393359, 122.9605952]) 
                           
            raw_routes.append(GAHONONP3R5)                
            raw_routes.append(GAHONONP3R1)                

        # MANTAGABAC
        if i == 'AWITANP1':   
            GAHONONP3R2 = map_widget.set_marker(14.1319742, 122.9647275, text="AWITANP1")  
            GAHONONP3R5 = map_widget.set_marker(14.1352107, 122.9654830, text="AWITANP1")
              
            raw_coordinates.append([14.1319742, 122.9647275])  
            raw_coordinates.append([14.1352107, 122.9654830])  
                                          
            raw_routes.append(GAHONONP3R2)                 
            raw_routes.append(GAHONONP3R5)

        # MANTAGABAC
        if i == 'BORABODP1':   
            GAHONONP3R2 = map_widget.set_marker(14.1256873, 122.9597612, text="BORABODP1") 
            GAHONONP3R1 = map_widget.set_marker(14.1266176, 122.9614055, text="BORABODP1")   
              
            raw_coordinates.append([14.1256873, 122.9597612])
            raw_coordinates.append([14.1266176, 122.9614055])   
                                          
            raw_routes.append(GAHONONP3R2)      
            raw_routes.append(GAHONONP3R1)                  

        # MANTAGABAC
        if i == 'BORABODP2':   
            GAHONONP3R2 = map_widget.set_marker(14.1280595, 122.9644176, text="BORABODP2") 
              
            raw_coordinates.append([14.1280595, 122.9644176])
                                          
            raw_routes.append(GAHONONP3R2)      


        # MANTAGABAC
        if i == 'BORABODP5':   
            GAHONONP3R2 = map_widget.set_marker(14.1306410, 122.9699107, text="BORABODP5") 
              
            raw_coordinates.append([14.1306410, 122.9699107])
                                          
            raw_routes.append(GAHONONP3R2) 

        # MANTAGABAC
        if i == 'BORABODP3':   
            GAHONONP3R2 = map_widget.set_marker(14.1246869, 122.9542130, text="BORABODP3") 
            GAHONONP3R1 = map_widget.set_marker(14.1280995, 122.9590624, text="BORABODP3") 
              
            raw_coordinates.append([14.1246869, 122.9542130])
            raw_coordinates.append([14.1280995, 122.9590624])
                                          
            raw_routes.append(GAHONONP3R2)      
            raw_routes.append(GAHONONP3R1)      


        # MANTAGABAC
        if i == 'BORABODP4':   
            GAHONONP3R1 = map_widget.set_marker(14.1263850, 122.9641594, text="BORABODP4") 
            GAHONONP3R2 = map_widget.set_marker(14.1255465, 122.9638268, text="BORABODP4") 
            GAHONONP3R3 = map_widget.set_marker(14.1250945, 122.9641006, text="BORABODP4") 
            GAHONONP3R4 = map_widget.set_marker(14.1246986, 122.9645349, text="BORABODP4") 
            GAHONONP3R5 = map_widget.set_marker(14.1245014, 122.9650052, text="BORABODP4") 
            GAHONONP3R6 = map_widget.set_marker(14.1244152, 122.9653460, text="BORABODP4") 
            GAHONONP3R7 = map_widget.set_marker(14.1235689, 122.9665824, text="BORABODP4") 
              
            raw_coordinates.append([14.1263850, 122.9641594])
            raw_coordinates.append([14.1255465, 122.9638268])
            raw_coordinates.append([14.1250945, 122.9641006])
            raw_coordinates.append([14.1246986, 122.9645349])
            raw_coordinates.append([14.1245014, 122.9650052])
            raw_coordinates.append([14.1244152, 122.9653460])
            raw_coordinates.append([14.1235689, 122.9665824])
                                          
            raw_routes.append(GAHONONP3R1)      
            raw_routes.append(GAHONONP3R2)      
            raw_routes.append(GAHONONP3R3)      
            raw_routes.append(GAHONONP3R4)      
            raw_routes.append(GAHONONP3R5)      
            raw_routes.append(GAHONONP3R6)      
            raw_routes.append(GAHONONP3R7)      


        # MANTAGABAC
        if i == 'BAGASBASP1':   
            GAHONONP3R1 = map_widget.set_marker(14.1366379, 122.9816975, text="BAGASGBASP1")  
            GAHONONP3R2 = map_widget.set_marker(14.1354310, 122.9822125, text="BAGASGBASP1")   
            GAHONONP3R3 = map_widget.set_marker(14.1324971, 122.9819335, text="BAGASGBASP1")    
              
            raw_coordinates.append([14.1366379, 122.9816975]) 
            raw_coordinates.append([14.1354310, 122.9822125]) 
            raw_coordinates.append([14.1324971, 122.9819335]) 
                                          
            raw_routes.append(GAHONONP3R1)       
            raw_routes.append(GAHONONP3R2)       
            raw_routes.append(GAHONONP3R3)       
        
        # MANTAGABAC
        if i == 'BAGASBASP2':   
            GAHONONP3R2 = map_widget.set_marker(14.1368689, 122.9811093, text="BAGASGBASP2")  
              
            raw_coordinates.append([14.1368689, 122.9811093]) 
                                          
            raw_routes.append(GAHONONP3R2)       

        # MANTAGABAC
        if i == 'BAGASBASP3':   
            GAHONONP3R2 = map_widget.set_marker(14.1372721, 122.9818710, text="BAGASGBASP3")  
              
            raw_coordinates.append([14.1372721, 122.9818710]) 
                                          
            raw_routes.append(GAHONONP3R2)       
            
        # MANTAGABAC
        if i == 'BAGASBASP4':   
            GAHONONP3R1 = map_widget.set_marker(14.1391137, 122.9813775, text="BAGASGBASP4")  
            GAHONONP3R3 = map_widget.set_marker(14.1395230, 122.9810503, text="BAGASGBASP4") 
            GAHONONP3R2 = map_widget.set_marker(14.1395386, 122.9810074, text="BAGASGBASP4")  
            GAHONONP3R4 = map_widget.set_marker(14.1394814, 122.9804119, text="BAGASGBASP4")    
              
            raw_coordinates.append([14.1391137, 122.9813775]) 
            raw_coordinates.append([14.1395230, 122.9810503]) 
            raw_coordinates.append([14.1395386, 122.9810074]) 
            raw_coordinates.append([14.1394814, 122.9804119])  
                                          
            raw_routes.append(GAHONONP3R1)     
            raw_routes.append(GAHONONP3R3)     
            raw_routes.append(GAHONONP3R2)     
            raw_routes.append(GAHONONP3R4)     

        # MANTAGABAC
        if i == 'BAGASBASP5':   
            GAHONONP3R1 = map_widget.set_marker(14.1395805, 122.9795810, text="BAGASGBASP5")
            GAHONONP3R2 = map_widget.set_marker(14.1397522, 122.9791304, text="BAGASGBASP5")  
            GAHONONP3R3 = map_widget.set_marker(14.1406705, 122.9782346, text="BAGASGBASP5")  
              
            raw_coordinates.append([14.1395805, 122.9795810]) 
            raw_coordinates.append([14.1397522, 122.9791304]) 
            raw_coordinates.append([14.1406705, 122.9782346]) 
                                          
            raw_routes.append(GAHONONP3R1)     
            raw_routes.append(GAHONONP3R2)     
            raw_routes.append(GAHONONP3R3) 

        # MANTAGABAC
        if i == 'BAGASBASP6':   
            GAHONONP3R1 = map_widget.set_marker(14.1426990, 122.9774406, text="BAGASGBASP6") 
              
            raw_coordinates.append([14.1395805, 122.9795810])  
                                          
            raw_routes.append(GAHONONP3R1)    

        #------------------------------------------------------------------------
        # BARANGAY 7
        if i == 'BRGY7P1':
            BRGY6P4R1 = map_widget.set_marker(14.1156730, 122.9559872, text="BRGY7P1") 
            BRGY7P1r1 = map_widget.set_marker(14.1155500, 122.9565347, text="BRGY7P1")

            raw_coordinates.append([14.1156730, 122.9559872]) 
            raw_coordinates.append([14.1155500, 122.9565347])

            raw_routes.append(BRGY6P4R1) 
            raw_routes.append(BRGY7P1r1)
        
        
        if i == 'BRGY7P2': 
            BRGY7P2 = map_widget.set_marker(14.1154379, 122.9579205, text="BRGY7P2")

            raw_coordinates.append([14.1154379, 122.9579205])

            raw_routes.append(BRGY7P2)

        if i == 'BRGY7P3':
            BRGY7P3 = map_widget.set_marker(14.1152921, 122.9603826, text="BRGY7P3")

            raw_coordinates.append([14.1152921, 122.9603826])

            raw_routes.append(BRGY7P3)

        if i == 'BRGY7P4':
            BRGY7P4 = map_widget.set_marker(14.1151505, 122.9618980, text="BRGY7P4")

            raw_coordinates.append([14.1151505, 122.9618980])

            raw_routes.append(BRGY7P4)

        if i == 'BRGY7P5':
            BRGY7P5 = map_widget.set_marker(14.1150048, 122.9642583, text="BRGY7P5")

            raw_coordinates.append([14.1150048, 122.9642583])

            raw_routes.append(BRGY7P5)

        if i == 'BRGY7P6':
            BRGY7P6 = map_widget.set_marker(14.1183077, 122.9559281, text="BRGY7P6")
            BRGY6P3 = map_widget.set_marker(14.1168914, 122.9612174, text="BRGY7P6")

            raw_coordinates.append([14.1183077, 122.9559281])
            raw_coordinates.append([14.1168914, 122.9612174])

            raw_routes.append(BRGY7P6)
            raw_routes.append(BRGY6P3)

        if i == 'BRGY7P7':
            BRGY7P7 = map_widget.set_marker(14.1175784, 122.9615304, text="BRGY7P7")

            raw_coordinates.append([14.1175784, 122.9615304])

            raw_routes.append(BRGY7P7)

        if i == 'BRGY7P7R1':
            BRGY7P7 = map_widget.set_marker(14.1170349, 122.9605477, text="BRGY7P7R1")

            raw_coordinates.append([14.1170349, 122.9605477])

            raw_routes.append(BRGY7P7)
        #------------------------------------------------------------------------
            # BARANGAY VIII
        if i == 'BRGY8P1':
            BRGY6P4R2 = map_widget.set_marker(14.1148785, 122.9564332, text="BRGY8P1") 

            raw_coordinates.append([14.1148785, 122.9564332]) 

            raw_routes.append(BRGY6P4R2) 

        if i == 'BRGY8P2':
            BRGY6P4R3 = map_widget.set_marker(14.1141362, 122.9563149, text="BRGY8P2")

            raw_coordinates.append([14.1141362, 122.9563149])

            raw_routes.append(BRGY6P4R3)

        if i == 'BRGY8P3':
            BRGY8P3 = map_widget.set_marker(14.1147034, 122.9578591, text="BRGY8P3")

            raw_coordinates.append([14.1147034, 122.9578591])

            raw_routes.append(BRGY8P3)

        if i == 'BRGY8P4':
            BRGY8P4 = map_widget.set_marker(14.1138955, 122.9576928, text="BRGY8P4")

            raw_coordinates.append([14.1138955, 122.9576928])

            raw_routes.append(BRGY8P4)

        if i == 'BRGY8P5':
            #BRGY8R1P5 = map_widget.set_marker(14.1145426, 122.9586826, text="")
            BRGY8P5 = map_widget.set_marker(14.1150408, 122.9588421, text="BRGY8P5")

            #raw_coordinates.append([14.1145426, 122.9586826])
            raw_coordinates.append([14.1150408, 122.9588421])

            #raw_routes.append(BRGY8R1P5)
            raw_routes.append(BRGY8P5)

        if i == 'BRGY7P3R1':
            BRGY8R1P5 = map_widget.set_marker(14.1153844, 122.9589417, text="BRGY7P3R1")
            
            raw_coordinates.append([14.1153844, 122.9589417])
            
            raw_routes.append(BRGY8R1P5)

        if i == 'BRGY8P6':
            BRGY8P6 = map_widget.set_marker(14.1145502, 122.9586828, text="BRGY8P6")

            raw_coordinates.append([14.1145502, 122.9586828])

            raw_routes.append(BRGY8P6)

        if i == 'BRGY8P7':
            BRGY8P7 = map_widget.set_marker(14.1135273, 122.9594461, text="BRGY8P7")

            raw_coordinates.append([14.1135273, 122.9594461])

            raw_routes.append(BRGY8P7)

        if i == 'BRGY8P8':
            BRGY8P8 = map_widget.set_marker(14.1135273, 122.9594461, text="BRGY8P8")

            raw_coordinates.append([14.1135273, 122.9594461])

            raw_routes.append(BRGY8P8)

        if i == 'BRGY8P9R1':
            BRGY8R1P5 = map_widget.set_marker(14.1145426, 122.9586826, text="BRGY8P9R1")
            
            raw_coordinates.append([14.1145426, 122.9586826])
            
            raw_routes.append(BRGY8R1P5)

        
        if i == 'BRGY8P9':
            BRGY8R1P5 = map_widget.set_marker(14.1137657, 122.9584353, text="BRGY8P9")
            
            raw_coordinates.append([14.1137657, 122.9584353])
            
            raw_routes.append(BRGY8R1P5)

        if i == 'BRGY8P9R3':
            BRGY8R1P5C = map_widget.set_marker(14.1135194, 122.9593563, text="BRGY8P9R3")
            BRGY8R1P5 = map_widget.set_marker(14.1134403, 122.9606674, text="BRGY8P9R3")
            
            raw_coordinates.append([14.1135194, 122.9593563])
            raw_coordinates.append([14.1134403, 122.9606674])
            
            raw_routes.append(BRGY8R1P5C)                
            raw_routes.append(BRGY8R1P5)                

        if i == 'BRGY8P10':
            BRGY8P10 = map_widget.set_marker(14.1133080, 122.9635932, text="BRGY8P10")

            raw_coordinates.append([14.1133080, 122.9635932])

            raw_routes.append(BRGY8P10)

        
        
        # GUBAT
        if i == 'BRGYGUBATP1GUYABANO':
            BRGYGUBATP1GUYABANO = map_widget.set_marker(14.1148391, 122.9666635, text="BRGYGUBATP1GUYABANO")

            raw_coordinates.append([14.1148391, 122.9666635])

            raw_routes.append(BRGYGUBATP1GUYABANO)

        if i == 'BRGYGUBATP2UBAS':
            BRGYGUBATP2UBAS = map_widget.set_marker(14.1156565, 122.9668052, text="BRGYGUBATP2UBAS")

            raw_coordinates.append([14.1156565, 122.9668052])

            raw_routes.append(BRGYGUBATP2UBAS)

        if i == 'BRGYGUBATP3BAYABAS':
            BRGYGUBATP3BAYABAS = map_widget.set_marker(14.1143594, 122.9737923, text="BRGYGUBATP3BAYABAS")

            raw_coordinates.append([14.1143594, 122.9737923])

            raw_routes.append(BRGYGUBATP3BAYABAS)

        if i == 'BRGYGUBATP4ATIS':
            BRGYGUBATP4ATIS = map_widget.set_marker(14.1141435, 122.9771149, text="BRGYGUBATP4ATIS")

            raw_coordinates.append([14.1141435, 122.9771149])

            raw_routes.append(BRGYGUBATP4ATIS)

        if i == 'BRGYGUBATP5TSIKO':
            BRGYGUBATP5TSIKO = map_widget.set_marker(14.1140174, 122.9793401, text="BRGYGUBATP5TSIKO")

            raw_coordinates.append([14.1140174, 122.9793401])

            raw_routes.append(BRGYGUBATP5TSIKO)

        if i == 'BRGY1P1':
            BRGYGUBATP5TSIKO = map_widget.set_marker(14.1129244, 122.9560431, text="BRGY1P1")

            raw_coordinates.append([14.1129244, 122.9560431])

            raw_routes.append(BRGYGUBATP5TSIKO)

        if i == 'BRGY1P2':
            BRGYGUBATP5TSIKO = map_widget.set_marker(14.1126172, 122.9570569, text="BRGY1P2")

            raw_coordinates.append([14.1126172, 122.9570569])

            raw_routes.append(BRGYGUBATP5TSIKO)

        if i == 'BRGY1P3':
            BRGYGUBATP5TSIKO = map_widget.set_marker(14.1124247, 122.9590096, text="BRGY1P3")

            raw_coordinates.append([14.1124247, 122.9590096])

            raw_routes.append(BRGYGUBATP5TSIKO)
        
        if i == 'BRGY1P6':
            BRGYGUBATP5TSIKO = map_widget.set_marker(14.1121643, 122.9598308, text="BRGY1P6")

            raw_coordinates.append([14.1121643, 122.9598308])

            raw_routes.append(BRGYGUBATP5TSIKO)
        
        if i == 'BRGY1P7':
            BRGYGUBATP5TSIKO = map_widget.set_marker(14.1117897, 122.9612256, text="BRGY1P7")

            raw_coordinates.append([14.1117897, 122.9612256])

            raw_routes.append(BRGYGUBATP5TSIKO)
        
        if i == 'BRGY1P8':
            BRGY1P8R1 = map_widget.set_marker(14.1120835, 122.9630928, text="BRGY1P8")
            BRGY1P8R2 = map_widget.set_marker(14.1121095, 122.9639192, text="BRGY1P8")

            raw_coordinates.append([14.1120835, 122.9630928])
            raw_coordinates.append([14.1121095, 122.9639192])

            raw_routes.append(BRGY1P8R1)
            raw_routes.append(BRGY1P8R2)

        if i == 'BRGY1P4':
            BRGY1P8R1 = map_widget.set_marker(14.1108720, 122.9559683, text="BRGY1P4") 

            raw_coordinates.append([14.1108720, 122.9559683]) 

            raw_routes.append(BRGY1P8R1) 
        
        if i == 'BRGY1P4R1':
            BRGY1P8R1 = map_widget.set_marker(14.1109171, 122.9570919, text="BRGY1P4R1") 

            raw_coordinates.append([14.1109171, 122.9570919]) 

            raw_routes.append(BRGY1P8R1) 
        
        if i == 'BRGY1P4R2':
            BRGY1P8R1 = map_widget.set_marker(14.1109067, 122.9590329, text="BRGY1P4R2") 

            raw_coordinates.append([14.1109067, 122.9590329]) 

            raw_routes.append(BRGY1P8R1) 
        
        
        if i == 'BRGY1P5':
            
            BRGY1P8R1 = map_widget.set_marker(14.1102728, 122.9560010, text="BRGY1P5") 

            raw_coordinates.append([14.1102728, 122.9560010]) 

            raw_routes.append(BRGY1P8R1) 
 
        if i == 'BRGY3P1':
            
            BRGY1P8R1 = map_widget.set_marker(14.1135220, 122.9546667, text="BRGY3P1") 

            raw_coordinates.append([14.1135220, 122.9546667]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY3P2':
            
            BRGY1P8R1 = map_widget.set_marker(14.1130538, 122.9546453, text="BRGY3P2") 

            raw_coordinates.append([14.1130538, 122.9546453]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY3P3':
            
            BRGY1P8R1 = map_widget.set_marker(14.1125486, 122.9546068, text="BRGY3P3") 

            raw_coordinates.append([14.1125486, 122.9546068]) 

            raw_routes.append(BRGY1P8R1) 
        
        if i == 'BRGY3P4':
            
            BRGY1P8R1 = map_widget.set_marker(14.1121865, 122.9546121, text="BRGY3P4") 

            raw_coordinates.append([14.1121865, 122.9546121]) 

            raw_routes.append(BRGY1P8R1) 
        
        if i == 'BRGY3P5':
            
            BRGY1P8R1 = map_widget.set_marker(14.1116163, 122.9546014, text="BRGY3P5") 

            raw_coordinates.append([14.1116163, 122.9546014]) 

            raw_routes.append(BRGY1P8R1) 


        if i == 'BRGY3P6':
            
            BRGY1P8R1 = map_widget.set_marker(14.1102289, 122.9545585, text="BRGY3P6") 

            raw_coordinates.append([14.1102289, 122.9545585]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY3P6R1':
            BRGY1P8R1 = map_widget.set_marker(14.1095002, 122.9545484, text="BRGY3P6R1") 
            BRGY1P8R2 = map_widget.set_marker(14.1094950, 122.9548247, text="BRGY3P6R1")  

            raw_coordinates.append([14.1095002, 122.9545484])
            raw_coordinates.append([14.1094950, 122.9548247]) 

            raw_routes.append(BRGY1P8R1) 
            raw_routes.append(BRGY1P8R2) 
        

        if i == 'BRGY2P1':
            
            BRGY1P8R1 = map_widget.set_marker(14.1081085, 122.9548783, text="BRGY2P1") 

            raw_coordinates.append([14.1081085, 122.9548783]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P2':
            
            BRGY1P8R1 = map_widget.set_marker(14.1074121, 122.9549725, text="BRGY2P2") 

            raw_coordinates.append([14.1074121, 122.9549725]) 

            raw_routes.append(BRGY1P8R1) 
            
        if i == 'BRGY2P3':
            
            BRGY1P8R1 = map_widget.set_marker(14.1068076, 122.9550122, text="BRGY2P3") 

            raw_coordinates.append([14.1068076, 122.9550122]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P4':
            
            BRGY1P8R1 = map_widget.set_marker(14.1061448, 122.9550633, text="BRGY2P4") 

            raw_coordinates.append([14.1061448, 122.9550633]) 

            raw_routes.append(BRGY1P8R1) 

        
        if i == 'BRGY2P5':
            
            BRGY1P8R1 = map_widget.set_marker(14.1055291, 122.9550575, text="BRGY2P5") 

            raw_coordinates.append([14.1055291, 122.9550575]) 

            raw_routes.append(BRGY1P8R1) 

        
        if i == 'BRGY2P6':
            
            BRGY1P8R1 = map_widget.set_marker(14.1050973, 122.9550599, text="BRGY2P6") 

            raw_coordinates.append([14.1050973, 122.9550599]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P8':
            
            BRGY1P8R1 = map_widget.set_marker(14.1081723, 122.9561043, text="BRGY2P8") 

            raw_coordinates.append([14.1081723, 122.9561043]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P8R1':
            
            BRGY1P8R1 = map_widget.set_marker(14.1074915, 122.9561317, text="BRGY2P8R1") 

            raw_coordinates.append([14.1074915, 122.9561317]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P8R2':
            
            BRGY1P8R1 = map_widget.set_marker(14.1068083, 122.9561336, text="BRGY2P8R2") 

            raw_coordinates.append([14.1068083, 122.9561336]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P8R3':
            
            BRGY1P8R1 = map_widget.set_marker(14.1062034, 122.9562125, text="BRGY2P8R3") 

            raw_coordinates.append([14.1062034, 122.9562125]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P7':
            
            BRGY1P8R1 = map_widget.set_marker(14.1056124, 122.9562488, text="BRGY2P7") 

            raw_coordinates.append([14.1056124, 122.9562488]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P7R1':
            
            BRGY1P8R1 = map_widget.set_marker(14.1051155, 122.9562776, text="BRGY2P7R1") 

            raw_coordinates.append([14.1051155, 122.9562776]) 

            raw_routes.append(BRGY1P8R1) 

        if i == 'BRGY2P7R2':
            
            BRGY1P8R1 = map_widget.set_marker(14.1045407, 122.9562882, text="BRGY2P7R2") 

            raw_coordinates.append([14.1045407, 122.9562882]) 

            raw_routes.append(BRGY1P8R1) 
        
        if i == 'SANISIDROP1':
            SANISIDROP1 = map_widget.set_marker(14.1119195, 122.9652880, text="San Isidro P-1")
            raw_coordinates.append([14.1119195, 122.9652880])
            raw_routes.append(SANISIDROP1)

        if i == 'SANISIDROP2':
            SANISIDROP2R1 = map_widget.set_marker(14.1117426, 122.9655275)
            SANISIDROP2 = map_widget.set_marker(14.1113692, 122.9663126, text="San Isidro P-2")

            raw_coordinates.append([14.1117426, 122.9655275])
            raw_coordinates.append([14.1113692, 122.9663126])

            raw_routes.append(SANISIDROP2R1)
            raw_routes.append(SANISIDROP2)


        if i == 'SANISIDROP3':
            SANISIDROP3R1 = map_widget.set_marker(14.1115162, 122.9664457)
            SANISIDROP3 = map_widget.set_marker(14.1096182, 122.9717979, text="San Isidro P-3")

            raw_coordinates.append([14.1115162, 122.9664457])
            raw_coordinates.append([14.1096182, 122.9717979])

            raw_routes.append(SANISIDROP3R1)
            raw_routes.append(SANISIDROP3)

        if i == 'SANISIDROP4':
            SANISIDROP4R1 = map_widget.set_marker(14.1108660, 122.9671934)
            SANISIDROP4R2 = map_widget.set_marker(14.1105119, 122.9673732)
            SANISIDROP4 = map_widget.set_marker(14.1083121, 122.9674512, text="San Isidro P-4")

            raw_coordinates.append([14.1108660, 122.9671934])
            raw_coordinates.append([14.1105119, 122.9673732])
            raw_coordinates.append([14.1083121, 122.9674512])

            raw_routes.append(SANISIDROP4R1)
            raw_routes.append(SANISIDROP4R2)
            raw_routes.append(SANISIDROP4)

        if i == 'SANISIDROP5':
            SANISIDROP5 = map_widget.set_marker(14.1076827, 122.9769609, text="San Isidro P-5")
            raw_coordinates.append([14.1076827, 122.9769609])
            raw_routes.append(SANISIDROP5)

        if i == 'SANISIDROP6':
            SANISIDROP6 = map_widget.set_marker(14.1064963, 122.9812528, text="San Isidro P-6")
            raw_coordinates.append([14.1064963, 122.9812528])
            raw_routes.append(SANISIDROP6)

        if i == 'COBANGBANGP2':
            
            SANISIDROP6 = map_widget.set_marker(14.1092086, 122.9591249, text="COBANGBANGP2")

            raw_coordinates.append([14.1092086, 122.9591249])

            raw_routes.append(SANISIDROP6)
        
        if i == 'COBANGBANGP2R1':
            
            SANISIDROP6 = map_widget.set_marker(14.1096594, 122.9592054, text="COBANGBANGP2")

            raw_coordinates.append([14.1096594, 122.9592054])
            
            raw_routes.append(SANISIDROP6)
    
        if i == 'COBANGBANGP1R1':
            SANISIDROP6 = map_widget.set_marker(14.1046383, 122.9574995, text="COBANGBANGP1R1")

            raw_coordinates.append([14.1046383, 122.9574995])
            
            raw_routes.append(SANISIDROP6)

        if i == 'COBANGBANGP1R2':
            SANISIDROP6 = map_widget.set_marker(14.1047580, 122.9581646, text="COBANGBANGP1R1")

            raw_coordinates.append([14.1047580, 122.9581646])
            
            raw_routes.append(SANISIDROP6)

            
        if i == 'COBANGBANGP1R3':
            SANISIDROP6 = map_widget.set_marker(14.1047528, 122.9586099, text="COBANGBANGP1R3")

            raw_coordinates.append([14.1047528, 122.9586099])
            
            raw_routes.append(SANISIDROP6)

        if i == 'COBANGBANGP1R4':
            SANISIDROP6 = map_widget.set_marker(14.1047008, 122.9593341, text="COBANGBANGP1R4")

            raw_coordinates.append([14.1047008, 122.9593341])
            
            raw_routes.append(SANISIDROP6)

        if i == 'COBANGBANGP1':
            SANISIDROP6 = map_widget.set_marker(14.1048829, 122.9597364, text="COBANGBANGP1")

            raw_coordinates.append([14.1048829, 122.9597364])
            
            raw_routes.append(SANISIDROP6)

        if i == 'COBANGBANGP3':
            SANISIDROP6 = map_widget.set_marker(14.1078154, 122.9599453, text="COBANGBANGP3")

            raw_coordinates.append([14.1078154, 122.9599453])
            
            raw_routes.append(SANISIDROP6)
        
        if i == 'COBANGBANGP3R1':
            SANISIDROP6 = map_widget.set_marker(14.1056944, 122.9609833, text="COBANGBANGP3R1")

            raw_coordinates.append([14.1056944, 122.9609833])
            
            raw_routes.append(SANISIDROP6)
            
        if i == 'COBANGBANGP4':
            SANISIDROP6 = map_widget.set_marker(14.1048668, 122.9616217, text="COBANGBANGP4")

            raw_coordinates.append([14.1048668, 122.9616217])
            
            raw_routes.append(SANISIDROP6)

        if i == 'COBANGBANGP5':
            SANISIDROP6 = map_widget.set_marker(14.1039537, 122.9634966, text="COBANGBANGP5")

            raw_coordinates.append([14.1039537, 122.9634966])
            
            raw_routes.append(SANISIDROP6)

            
        if i == 'COBANGBANGP6':
            SANISIDROP6 = map_widget.set_marker(14.1027849, 122.9657915, text="COBANGBANGP6")

            raw_coordinates.append([14.1027849, 122.9657915])
            
            raw_routes.append(SANISIDROP6)


        if i == 'MAMBALITEP1':
            MAMBALITEP1R1 = map_widget.set_marker(14.1016763, 122.9670235)
            MAMBALITEP1R2 = map_widget.set_marker(14.1015197, 122.9674307)
            MAMBALITEP1R3 = map_widget.set_marker(14.1005298, 122.9685157)
            MAMBALITEP1R4 = map_widget.set_marker(14.0975802, 122.9698995)
            MAMBALITEP1R5 = map_widget.set_marker(14.0948315, 122.9724051)
            MAMBALITEP1 = map_widget.set_marker(14.0940781, 122.9731535, text="Mambalite P-1")

            raw_coordinates.append([14.1016763, 122.9670235])
            raw_coordinates.append([14.1015197, 122.9674307])
            raw_coordinates.append([14.1005298, 122.9685157])
            raw_coordinates.append([14.0975802, 122.9698995])
            raw_coordinates.append([14.0948315, 122.9724051])
            raw_coordinates.append([14.0940781, 122.9731535])

            raw_routes.append(MAMBALITEP1R1)
            raw_routes.append(MAMBALITEP1R2)
            raw_routes.append(MAMBALITEP1R3)
            raw_routes.append(MAMBALITEP1R4)
            raw_routes.append(MAMBALITEP1R5)
            raw_routes.append(MAMBALITEP1)

        if i == 'MAMBALITEP2':
            MAMBALITEP2 = map_widget.set_marker(14.091017167536688, 122.97633666556318, text="Mambalite P-2")
            raw_coordinates.append([14.091017167536688, 122.97633666556318])
            raw_routes.append(MAMBALITEP2)

        if i == 'MAMBALITEP3':
            MAMBALITEP3 = map_widget.set_marker(14.091032540606854, 122.97907382189071, text="Mambalite P-3")
            raw_coordinates.append([14.091032540606854, 122.97907382189071])
            raw_routes.append(MAMBALITEP3)

        if i == 'MAMBALITEP4':
            MAMBALITEP4R1 = map_widget.set_marker(14.0911089, 122.9812879)
            MAMBALITEP4 = map_widget.set_marker(14.0908998, 122.9818873, text="Mambalite P-4")
            raw_coordinates.append([14.0911089, 122.9812879])
            raw_coordinates.append([14.0908998, 122.9818873])
            raw_routes.append(MAMBALITEP4R1)
            raw_routes.append(MAMBALITEP4)

        if i == 'MAMBALITEP5':
            MAMBALITEP5R1 = map_widget.set_marker(14.0898965, 122.9837384)
            MAMBALITEP5 = map_widget.set_marker(14.0908037, 122.9875669, text="Mambalite P-5")
            raw_coordinates.append([14.0898965, 122.9837384])
            raw_coordinates.append([14.0908037, 122.9875669])
            raw_routes.append(MAMBALITEP5R1)
            raw_routes.append(MAMBALITEP5)

        if i == 'MAMBALITEP6':
            MAMBALITEP6R1 = map_widget.set_marker(14.0943865, 122.9734913)
            MAMBALITEP6R2 = map_widget.set_marker(14.0942565, 122.9743711)
            MAMBALITEP6R3 = map_widget.set_marker(14.0947545, 122.9759155)
            MAMBALITEP6R4 = map_widget.set_marker(14.0954758, 122.9763176)
            MAMBALITEP6R5 = map_widget.set_marker(14.0949561, 122.9773978)
            MAMBALITEP6 = map_widget.set_marker(14.0965138, 122.9784053, text="Mambalite P-6")

            raw_coordinates.append([14.0943865, 122.9734913])
            raw_coordinates.append([14.0942565, 122.9743711])
            raw_coordinates.append([14.0947545, 122.9759155])
            raw_coordinates.append([14.0954758, 122.9763176])
            raw_coordinates.append([14.0949561, 122.9773978])
            raw_coordinates.append([14.0965138, 122.9784053])

            raw_routes.append(MAMBALITEP6R1)
            raw_routes.append(MAMBALITEP6R2)
            raw_routes.append(MAMBALITEP6R3)
            raw_routes.append(MAMBALITEP6R4)
            raw_routes.append(MAMBALITEP6R5)
            raw_routes.append(MAMBALITEP6)

        if i == 'MAMBALITEP7':
            MAMBALITEP7 = map_widget.set_marker(14.0890201, 122.9892342, text="Mambalite P-7")

            raw_coordinates.append([14.0890201, 122.9892342])

            raw_routes.append(MAMBALITEP7)




    return raw_routes, raw_coordinates

# ----> Algorithm Pang determine ng destination <-------------------

def Set(barangay, destination):
    global specific_routes_label, specific_routes_label, firetruck_icon

    index = get_index_by_purok(all_purok, destination)

    fetch_location = all_location[barangay]
    final_destination = fetch_location[index]

    all_path, shortest_path, route_only, shortest_path_details = GetShortestPath("BFP", final_destination)

    routes, coordinates = GetCoordinates(route_only)

    firetruck_icon = PhotoImage(file="firetruck.png")

    all_paths_btn['command'] = lambda:show_notifier(all_path, shortest_path_details, final_destination, shortest_path)
    view_btn['command'] = lambda:show_all_paths(all_path, shortest_path_details, destination, barangay)

    print(coordinates)

    for i in range(len(coordinates) - 1):
        path_1 = map_widget.set_path([routes[i].position, routes[i+1].position, coordinates[i]])

    for i, coordinate in enumerate(coordinates):
        root.after(500 * i, lambda i=i, coordinate=tuple(coordinate): update_firetruck_position(coordinate, firetruck_icon))


    view_btn['state'] = 'normal'
    all_paths_btn['state'] = 'normal'

# ----> Algorithm Pang reset ng lahat ng fields <-------------------

def RemoveCoordinates():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()

    purok_combo_var.set("")
    barangay_combo_var.set("")

    view_btn['state'] = "disabled"
    all_paths_btn['state'] = "disabled" 

    canvas.itemconfig(routes_label, text="")
    canvas.itemconfig(total_distance_label, text="")
    canvas.itemconfig(barangay_combo_var, text="")
    canvas.itemconfig(purok_combo_box, text="")

    for i in routes_label_list:
        canvas.itemconfig(i, text="")

# ----> Algorithm Pang determine kung nagfill up na sa barangay <-------------------
# ----> Dito rin maconditionals kung anong mga purok ng barangay <------------------

def update_purok_combobox(*args):
    # Enable the purok_combobox if a barangay is selected
    barangayDestination = barangay_combo_var.get()

    if barangayDestination in all_location:
        barangay_value = all_purok[barangayDestination]

        if barangay_value:
            purok_combo_box["state"] = "readonly"
            purok_combo_box["values"] = barangay_value
        else:
            purok_combo_box["state"] = "disabled"

    else:
        purok_combo_box.set("")  # Clear the selection
        purok_combo_box["state"] = "disabled"


def MainMenu():
    global my_label, root, canvas, map_widget, routes_label, total_distance_label, barangay_combo_var, purok_combo_box, purok_combo_var, view_btn, all_paths_btn
    root = Tk()
    root.title('Daet Map')
    root.geometry('1200x650+70+20')

    canvas = Canvas(root, width=1200, height=700, bg='red')
    canvas.pack()

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    # details
    text = "Details:"   
    canvas.create_text(100, 380, text=text, anchor='center', fill='white', font=('courier new', 12))
    routes_label = canvas.create_text(160, 390, text="", anchor='center', fill='white', font=('courier new', 10))
    total_distance_label = canvas.create_text(160, 420, text="", anchor='center', fill='white', font=('courier new', 10))

    map_widget = tkintermapview.TkinterMapView(my_label, width=1700, height=650, corner_radius=0)
    #map_widget.set_position(14.0996, 122.9550)

    canvas.create_window(850, 400, window=my_label)

    map_widget.set_address("Daet, Camarines Norte, Philippines")
    map_widget.set_zoom(14)
    map_widget.pack()

    # Get only the keys (names) from the dictionary
    all_barangay_names = list(all_location.keys())

    # Add a ComboBox to the canvas
    canvas.create_text(120, 25, text="Select barangay:", anchor='center', fill='white', font=('century gothic', 10))
    barangay_combo_var = StringVar()
    combo_box = ttk.Combobox(canvas, textvariable=barangay_combo_var, values=all_barangay_names, width=30, font=('century gothic', 10))
    canvas.create_window(160, 50, window=combo_box)

    canvas.create_text(420, 25, text="Select Purok:", anchor='center', fill='white', font=('century gothic', 10))
    purok_combo_var = StringVar()
    purok_combo_box = ttk.Combobox(canvas, textvariable=purok_combo_var, width=30, height=5, font=('century gothic', 10))
    canvas.create_window(420, 50, window=purok_combo_box)

    # Bind the function to the <<ComboboxSelected>> event
    combo_box.bind("<<ComboboxSelected>>", update_purok_combobox)

    search_btn = Button(canvas, text="Search", command=lambda:Set(barangay_combo_var.get(), purok_combo_var.get()), width=15)
    canvas.create_window(625, 50, window=search_btn)

    all_paths_btn = Button(canvas, text="Shortest Path Details", width=20, height=1)
    canvas.create_window(960, 50, window=all_paths_btn)

    view_btn = Button(canvas, text="View All", width=15, height=1)
    canvas.create_window(1115, 50, window=view_btn)

    remove_coordinates_button = Button(root, text="Reset", fg="black", width=11, height=2, bg="orange",
                                       command=RemoveCoordinates)
    canvas.create_window(1110, 600, window=remove_coordinates_button)

    canvas.create_window(1110, 600, window=remove_coordinates_button)
    create_firetruck_icon()
    root.mainloop()

MainMenu()