from tkinter import *
from tkinter import ttk  # Import the ttk module for themed widgets
import tkintermapview
from DijsktraAlgo import GetShortestPath
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
    'Barangay1': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6","Purok 7","Purok 8"],
    'Barangay 6': ["Purok 1", "Purok 2", "Purok 3","Purok 4", "Purok 5"],
    'Barangay 7': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7'],
    'Barangay 8': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6', 'Purok 7', 'Purok 8', 'Purok 9', 'Purok 10'],
    'Barangay Gubat:': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5'],
    'Barangay Pasig': [ 'Purok 6', 'Purok 5', 'Purok 7', 'Purok 4', 'Purok 3', 'Purok 2', 'Purok 1', 'Purok 8', ],
    'Borabod': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6"],
    'Calasgasan': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
    'Camambugan': ["Purok 1", "Purok 2", "Purok 3","Purok 4", "Purok 5", "Purok 6","Purok 7"],
    'Cobangbang': ["Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6"],
    'Gahonon': ['Purok 1', 'Purok 2', 'Purok 3', 'Purok 4', 'Purok 5', 'Purok 6'],
    'Lagon': ["LAGON", "Purok 1","Purok 2","Purok 3","Purok 4","Purok 5","Purok 6","Purok 7"],
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
    'Bibirao': ['BIBIRAOP1', 'BIBIRAOP2', 'BIBIRAOP3', 'BIBIRAOP4', 'BIBIRAOP5'],
    'Dogongan': ['DOGONGANP1', 'DOGONGANP2','DOGONGANP3','DOGONGANP4','DOGONGANP5','DOGONGANP6'],
    'Barangay 6': ["BRGY6P1", "BRGY6P2", "BRGY6P3","BRGY6P4", "BRGY6P5"],
    'Bagasbas': ["BAGASBASP1","BAGASBASP2","BAGASBASP3", "BAGASBASP4","BAGASBASP5","BAGASBASP6"],
    'Barangay1': ["BARANGAY1P1","BARANGAY1P2","BARANGAY1P3","BARANGAY1P4","BARANGAY1P5","BARANGAY1P6","BARANGAY1P7","BARANGAY1P8"],
    'Borabod': ["BORABODP1","BORABODP2","BORABODP3","BORABODP4","BORABODP5","BORABODP6"],
    'Camambugan': ["CAMAMBUGANP1", "CAMAMBUGANP2", "CAMAMBUGANP3","CAMAMBUGANP4", "CAMAMBUGANP5", "CAMAMBUGANP6","CAMAMBUGANP7"],
    'Cobangbang': ["COBANGBANGP1","COBANGBANGP2","COBANGBANGP3","COBANGBANGP4","COBANGBANGP5","COBANGBANGP6"],
    'Lagon': ["LAGON", "LAGONP1","LAGONP2","LAGONP3","LAGONP4","LAGONP5","LAGONP6","LAGONP7"],
    'Mantagbac': ['MANTAGBACP1', 'MANTAGBACP2', 'MANTAGBACP3', 'MANTAGBACP4', 'MANTAGBACP5', 'MANTAGBACP6', 'MANTAGBACP7', 'MANTAGBACP8', 'MANTAGBACP9'],
    'Barangay 8': ['BRGY8P1', 'BRGY8P2', 'BRGY8P3', 'BRGY8P4', 'BRGY8P5', 'BRGY8P6', 'BRGY8P7', 'BRGY8P8', 'BRGY8P9', 'BRGY8P10'],
    'Barangay 7': ['BRGY7P1', 'BRGY7P2', 'BRGY7P3', 'BRGY7P4', 'BRGY7P5', 'BRGY7P6', 'BRGY7P7'],
    'Barangay Gubat:': ['BRGYGUBATP1GUYABANO', 'BRGYGUBATP2UBAS', 'BRGYGUBATP3BAYABAS', 'BRGYGUBATP4ATIS', 'BRGYGUBATP5TSIKO'],
    'Barangay Pasig': [ 'BRGY2PASIGP6', 'BRGY2PASIGP5', 'BRGY2PASIGP7', 'BRGY2PASIGP4', 'BRGY2PASIGP3', 'BRGY2PASIGP2', 'BRGY2PASIGP1', 'BRGY2PASIGP8', ],
    'Magang': ['MAGANGP1', 'MAGANGP2', 'MAGANGP3', 'MAGANGP4', 'MAGANGP5', 'MAGANGP6'],
    'Pamorangon': ['PAMORANGONP1', 'PAMORANGONP2', 'PAMORANGONP3', 'PAMORANGONP4', 'PAMORANGONP5', 'PAMORANGONP6'],
    'Mancruz': ['MANCRUZP1', 'MANCRUZP2', 'MANCRUZP3', 'MANCRUZP4'],
    'San Isidro': ['SANISIDROP1', 'SANISIDROP2', 'SANISIDROP3', 'SANISIDROP4', 'SANISIDROP5', 'SANISIDROP6'],
    'Mambalite': ['MAMBALITEP1', 'MAMBALITEP2', 'MAMBALITEP3', 'MAMBALITEP4', 'MAMBALITEP5', 'MAMBALITEP6', 'MAMBALITEP7'],
    'Calasgasan': ['CALASGASANP1', 'CALASGASANP2', 'CALASGASANP3', 'CALASGASANP4', 'CALASGASANP5', 'CALASGASANP6'],
    'Gahonon': ['GAHONONP1', 'GAHONONP2', 'GAHONONP3', 'GAHONONP4', 'GAHONONP5', 'GAHONONP6'],
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

def show_notifier(message,shortest_distance_path, result_string):
    notifier_window = Toplevel(root)
    notifier_window.title("Details")
    notifier_window.geometry("500x500+400+300")  # Adjust the size and position as needed

    full_message = ' -> '.join(message)

    label1 = Label(notifier_window, text='Route details:', font=('century gothic', 12, 'bold'))
    label1.pack(pady=20, padx=10)

    label = Label(notifier_window, text=full_message, font=('century gothic', 12))
    label.pack(pady=20)

    distance_label = Label(notifier_window, text=f'Total Distance:',
                              font=('century gothic', 12, 'bold'))
    distance_label.pack(pady=20)

    distance_details = Label (notifier_window, text= f'{shortest_distance_path} meters', font=('century gothic', 12))
    distance_details.pack(pady=20)

    shortest_traffic_label = Label(notifier_window, text=f'Expected Traffic:',
                                      font=('century gothic', 12, 'bold'))
    shortest_traffic_label.pack(pady=20)

    shortest_traffic_details = Label(notifier_window, text= result_string,
                                      font=('century gothic', 12))
    shortest_traffic_details.pack(pady=20)

    ok_button = ttk.Button(notifier_window, text="OK", command=notifier_window.destroy)
    ok_button.pack()

def GetCoordinates(routes):

    raw_routes = []
    raw_coordinates = []


    for i in routes:

        if i == 'BFP':

            if routes[1] == "LAGONP4":
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")

                raw_coordinates.append([14.1181492, 122.9458283])

                raw_routes.append(BFP)
            elif routes[1] == "LAGONP4R1":
                BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
                BFPR1 = map_widget.set_marker(14.1176889, 122.9459710, text="")
                BFPR2 = map_widget.set_marker(14.1191091, 122.9504383, text="LAGONP4")

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
            LAGONP2R3 = map_widget.set_marker(14.1178483, 122.9406330, text="LAGONP2")
            LAGONP2R4 = map_widget.set_marker(14.1179370, 122.9402085, text="LAGONP2")
            LAGONP2R5 = map_widget.set_marker(14.1184001, 122.9398437, text="LAGONP2")
            LAGONP2R6 = map_widget.set_marker(14.1207033, 122.9392599, text="LAGONP2")
            LAGONP2R7 = map_widget.set_marker(14.1224618, 122.9390640, text="LAGONP2")
            LAGONP2R8 = map_widget.set_marker(14.1232970, 122.9386402, text="LAGONP2")

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

            LAGONP5R1 = map_widget.set_marker(14.1161958, 122.9407131, text="LAGONP5")
            LAGONP5R2 = map_widget.set_marker(14.1150188, 122.9389632, text="LAGONP5")
            LAGONP5R3 = map_widget.set_marker(14.1147849, 122.9381085, text="LAGONP5")
            LAGONP5R4 = map_widget.set_marker(14.1144514, 122.9350615, text="LAGONP5")

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

        if i == 'COBANGBANGP3':
            COBANGBANGR7 = map_widget.set_marker(14.1092531, 122.9591187, text="COBANGBANG P-3")
            COBANGBANGR8 = map_widget.set_marker(14.1068418, 122.9604321, text="COBANGBANG P-3")

            raw_coordinates.append([14.1092531, 122.9591187])
            raw_coordinates.append([14.1068418, 122.9604321])

            raw_routes.append(COBANGBANGR7)
            raw_routes.append(COBANGBANGR8)

        if i == 'COBANGBANGP2':
            COBANGBANGR9 = map_widget.set_marker(14.1057139, 122.9609740, text="COBANGBANG P-2")
            raw_coordinates.append([14.1057139, 122.9609740])
            raw_routes.append(COBANGBANGR9)

        if i == 'COBANGBANGP4':
            COBANGBANGR1 = map_widget.set_marker(14.1048467, 122.9616517, text="COBANGBANG P-4")
            raw_coordinates.append([14.1048467, 122.9616517])
            raw_routes.append(COBANGBANGR1)

            COBANGBANGR2 = map_widget.set_marker(14.1039683, 122.9634498, text="COBANGBANG P-4")
            raw_coordinates.append([14.1039683, 122.9634498])
            raw_routes.append(COBANGBANGR2)

        if i == 'COBANGBANGP5':
            COBANGBANGR1 = map_widget.set_marker(14.1039417, 122.9635213, text="")
            raw_coordinates.append([14.1039417, 122.9635213])
            raw_routes.append(COBANGBANGR1)

            COBANGBANGR2 = map_widget.set_marker(14.1035439, 122.9634229, text="COBANGBANG P-5")
            raw_coordinates.append([14.1035439, 122.9634229])
            raw_routes.append(COBANGBANGR2)

        if i == 'COBANGBANGP1':
            COBANGBANGR6 = map_widget.set_marker(14.1051243, 122.9562600, text="COBANGBANG P-1")
            COBANGBANGR7 = map_widget.set_marker(14.1049981, 122.9573857, text="COBANGBANG P-1")
            raw_coordinates.append([14.1051243, 122.9562600])
            raw_coordinates.append([14.1049981, 122.9573857])
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)

        if i == 'COBANGBANGP6':
            COBANGBANGR12 = map_widget.set_marker(14.1027421, 122.9658796, text="COBANGBANG P-6")
            raw_coordinates.append([14.1027421, 122.9658796])
            raw_routes.append(COBANGBANGR12)

        if i == 'AWITANP3':
            AWITANPR1 = map_widget.set_marker(14.1242738, 122.9449423, text="AWITAN P-3")
            AWITANPR2 = map_widget.set_marker(14.1271756, 122.9494915, text="AWITAN P-3")
            AWITANPR3 = map_widget.set_marker(14.1272848, 122.9496418, text="AWITAN P-3")
            AWITANPR4 = map_widget.set_marker(14.1341248, 122.9512816, text="AWITAN P-3")
            AWITANPR5 = map_widget.set_marker(14.1375581, 122.9561655, text="AWITAN P-3")
            AWITANPR6 = map_widget.set_marker(14.1387407, 122.9592159, text="AWITAN P-3")
            AWITANPR7 = map_widget.set_marker(14.1396597, 122.9587151, text="AWITAN P-3")
            AWITANPR8 = map_widget.set_marker(14.1387407, 122.9592159, text="")

            raw_coordinates.append([14.1242738, 122.9449423])
            raw_coordinates.append([14.1271756, 122.9494915])
            raw_coordinates.append([14.1272848, 122.9496418])
            raw_coordinates.append([14.1341248, 122.9512816])
            raw_coordinates.append([14.1375581, 122.9561655])
            raw_coordinates.append([14.1387407, 122.9592159])
            raw_coordinates.append([14.1396597, 122.9587151])
            raw_coordinates.append([14.1387407, 122.9592159])

            raw_routes.append(AWITANPR1)
            raw_routes.append(AWITANPR2)
            raw_routes.append(AWITANPR3)
            raw_routes.append(AWITANPR4)
            raw_routes.append(AWITANPR5)
            raw_routes.append(AWITANPR6)
            raw_routes.append(AWITANPR7)
            raw_routes.append(AWITANPR8)

        if i == 'AWITANP1':
            AWITANPR1 = map_widget.set_marker(14.1393551, 122.9606063, text="AWITAN P-1")
            raw_coordinates.append([14.1393551, 122.9606063])
            raw_routes.append(AWITANPR1)
            AWITANPR2 = map_widget.set_marker(14.1389172, 122.9611049, text="AWITAN P-1")
            raw_coordinates.append([14.1389172, 122.9611049])
            raw_routes.append(AWITANPR2)
            AWITANPR3 = map_widget.set_marker(14.1380432, 122.9616521, text="AWITAN P-1")
            raw_coordinates.append([14.1380432, 122.9616521])
            raw_routes.append(AWITANPR3)
            AWITANPR5 = map_widget.set_marker(14.1389172, 122.9611049, text="AWITAN P-1")
            raw_coordinates.append([14.1389172, 122.9611049])
            raw_routes.append(AWITANPR5)
            AWITANPR4 = map_widget.set_marker(14.1393551, 122.9606063, text="AWITAN P-1")
            raw_coordinates.append([14.1393551, 122.9606063])
            raw_routes.append(AWITANPR4)

        if i == 'AWITANP2':
            AWITANPR0 = map_widget.set_marker(14.1407872, 122.9637454, text="AWITAN P-2")
            AWITANPR1 = map_widget.set_marker(14.1412362, 122.9642978, text="AWITAN P-2")
            AWITANPR2 = map_widget.set_marker(14.1410226, 122.9648445, text="AWITAN P-2")
            raw_coordinates.append([14.1407872, 122.9637454])
            raw_coordinates.append([14.1412362, 122.9642978])
            raw_coordinates.append([14.1410226, 122.9648445])
            raw_routes.append(AWITANPR0)
            raw_routes.append(AWITANPR1)
            raw_routes.append(AWITANPR2)

        # BARANGAY 1

        if i == 'BARANGAY1P1':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="BARANGAY 1 P-1")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="BARANGAY 1 P-1")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="BARANGAY 1 P-1")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="BARANGAY 1 P-1")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="BARANGAY 1 P-1")

            raw_coordinates.append([14.1181492, 122.9458283])
            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])

            raw_routes.append(BFP)
            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)

        if i == 'BARANGAY1P2':
            COBANGBANGR6 = map_widget.set_marker(14.1125961, 122.9570849, text="BARANGAY 1 P-2")
            raw_coordinates.append([14.1125961, 122.9570849])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P3':
            COBANGBANGR6 = map_widget.set_marker(14.1124742, 122.9581552, text="BARANGAY 1 P-3")
            raw_coordinates.append([14.1124742, 122.9581552])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P4':
            COBANGBANGR6 = map_widget.set_marker(14.1108681, 122.9559878, text="BARANGAY 1 P-4")
            raw_coordinates.append([14.1108681, 122.9559878])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P5':
            COBANGBANGR6 = map_widget.set_marker(14.1102707, 122.9559953, text="BARANGAY 1 P-5")
            raw_coordinates.append([14.1102707, 122.9559953])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P6':
            COBANGBANGR6 = map_widget.set_marker(14.1123945, 122.9589966, text="BARANGAY 1P-6")
            raw_coordinates.append([14.1123945, 122.9589966])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P7':
            COBANGBANGR6 = map_widget.set_marker(14.1121612, 122.9598197, text="BARANGAY 1 P-7")
            raw_coordinates.append([14.1121612, 122.9598197])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P8':
            COBANGBANGR6 = map_widget.set_marker(14.1119425, 122.9605981, text="BARANGAY 1 P-8")
            raw_coordinates.append([14.1119425, 122.9605981])
            raw_routes.append(COBANGBANGR6)

        # BORABOD

        if i == 'BORABODP1':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            BORABODP1R1 = map_widget.set_marker(14.1176829, 122.9459697, text="BORABOD P-1")
            BORABODP1R2 = map_widget.set_marker(14.1190924, 122.9504048, text="BORABOD P-1")
            BORABODP1R3 = map_widget.set_marker(14.1201678, 122.9511875, text="BORABOD P-1")
            BORABODP1R4 = map_widget.set_marker(14.1175244, 122.9556175, text="BORABOD P-1")
            BORABODP1R5 = map_widget.set_marker(14.1240610, 122.9589386, text="BORABOD P-1")

            raw_coordinates.append([14.1181492, 122.9458283])
            raw_coordinates.append([14.1176829, 122.9459697])
            raw_coordinates.append([14.1190924, 122.9504048])
            raw_coordinates.append([14.1201678, 122.9511875])
            raw_coordinates.append([14.1175244, 122.9556175])
            raw_coordinates.append([14.1240610, 122.9589386])

            raw_routes.append(BFP)
            raw_routes.append(BORABODP1R1)
            raw_routes.append(BORABODP1R2)
            raw_routes.append(BORABODP1R3)
            raw_routes.append(BORABODP1R4)
            raw_routes.append(BORABODP1R5)

        if i == 'BORABODP2':
            BORABODP2R1 = map_widget.set_marker(14.1257225, 122.9597660, text="")
            BORABODP2R2 = map_widget.set_marker(14.1265685, 122.9613863, text="BORABOD P-2")
            raw_coordinates.append([14.1257225, 122.9597660])
            raw_coordinates.append([14.1265685, 122.9613863])
            raw_routes.append(BORABODP2R1)
            raw_routes.append(BORABODP2R2)

        if i == 'BORABODP3':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            BORABODP3R1 = map_widget.set_marker(14.1176829, 122.9459697, text="")
            BORABODP3R2 = map_widget.set_marker(14.1190924, 122.9504048, text="")
            BORABODP3R3 = map_widget.set_marker(14.1201678, 122.9511875, text="")
            BORABODP3R4 = map_widget.set_marker(14.1197876, 122.9517884, text="")
            BORABODP3R5 = map_widget.set_marker(14.1231490, 122.9528594, text="")
            BORABODP3R6 = map_widget.set_marker(14.1230840, 122.9536640, text="")
            BORABODP3R7 = map_widget.set_marker(14.1247080, 122.9542479, text="")
            BORABODP3R8 = map_widget.set_marker(14.1306064, 122.9628158, text="BORABOD P-3")
            raw_coordinates.append([14.1181492, 122.9458283])
            raw_coordinates.append([14.1176829, 122.9459697])
            raw_coordinates.append([14.1190924, 122.9504048])
            raw_coordinates.append([14.1201678, 122.9511875])
            raw_coordinates.append([14.1197876, 122.9517884])
            raw_coordinates.append([14.1231490, 122.9528594])
            raw_coordinates.append([14.1230840, 122.9536640])
            raw_coordinates.append([14.1247080, 122.9542479])
            raw_coordinates.append([14.1306064, 122.9628158])

            raw_routes.append(BFP)
            raw_routes.append(BORABODP3R1)
            raw_routes.append(BORABODP3R2)
            raw_routes.append(BORABODP3R3)
            raw_routes.append(BORABODP3R4)
            raw_routes.append(BORABODP3R5)
            raw_routes.append(BORABODP3R6)
            raw_routes.append(BORABODP3R7)
            raw_routes.append(BORABODP3R8)

        if i == 'BORABODP4':
            BORABODP4R1 = map_widget.set_marker(14.1279800, 122.9644454, text="BORABOD P-4")
            raw_coordinates.append([14.1279800, 122.9644454])
            raw_routes.append(BORABODP4R1)

        if i == 'BORABODP5':
            BORABODP5R1 = map_widget.set_marker(14.1305585, 122.9699444, text="BORABOD P-5")
            raw_coordinates.append([14.1305585, 122.9699444])
            raw_routes.append(BORABODP5R1)

        if i == 'BORABODP6':
            BORABODP6R1 = map_widget.set_marker(14.1316511, 122.9697172, text="")
            BORABODP6R2 = map_widget.set_marker(14.1334507, 122.9679562, text="BORABOD P-6")
            raw_coordinates.append([14.1316511, 122.9697172])
            raw_coordinates.append([14.1334507, 122.9679562])
            raw_routes.append(BORABODP6R1)
            raw_routes.append(BORABODP6R2)

        # BAGASBAS
        if i == 'BAGASBASP1':
            BAGASBASP1R1 = map_widget.set_marker(14.1347075, 122.9772225, text="")
            BAGASBASP1R2 = map_widget.set_marker(14.1340089, 122.9778572, text="BAGASBAS P-1")
            raw_coordinates.append([14.1347075, 122.9772225])
            raw_coordinates.append([14.1340089, 122.9778572])
            raw_routes.append(BAGASBASP1R1)
            raw_routes.append(BAGASBASP1R2)

        if i == 'BAGASBASP2':
            BAGASBASP2R1 = map_widget.set_marker(14.1347047, 122.9772304, text="")
            BAGASBASP2R2 = map_widget.set_marker(14.1357867, 122.9791636, text="")
            BAGASBASP2R3 = map_widget.set_marker(14.1337333, 122.9802586, text="BAGASBAS P-2")
            BAGASBASP2R4 = map_widget.set_marker(14.1357927, 122.9791616, text="")
            BAGASBASP2R5 = map_widget.set_marker(14.1361226, 122.9798357, text="")
            BAGASBASP2R6 = map_widget.set_marker(14.1341280, 122.9810421, text="BAGASBAS P-2")
            BAGASBASP2R7 = map_widget.set_marker(14.1361226, 122.9798357, text="")
            raw_coordinates.append([14.1347047, 122.9772304])
            raw_coordinates.append([14.1357867, 122.9791636])
            raw_coordinates.append([14.1337333, 122.9802586])
            raw_coordinates.append([14.1357927, 122.9791616])
            raw_coordinates.append([14.1361226, 122.9798357])
            raw_coordinates.append([14.1341280, 122.9810421])
            raw_coordinates.append([14.1361226, 122.9798357])
            raw_routes.append(BAGASBASP2R1)
            raw_routes.append(BAGASBASP2R2)
            raw_routes.append(BAGASBASP2R3)
            raw_routes.append(BAGASBASP2R4)
            raw_routes.append(BAGASBASP2R5)
            raw_routes.append(BAGASBASP2R6)
            raw_routes.append(BAGASBASP2R7)

        if i == 'BAGASBASP3':
            BAGASBASP3R1 = map_widget.set_marker(14.1368455, 122.9811729, text="BAGASBAS P-3")
            raw_coordinates.append([14.1368455, 122.9811729])
            raw_routes.append(BAGASBASP3R1)

        if i == 'BAGASBASP4':
            BAGASBASP4R1 = map_widget.set_marker(14.1372615, 122.9818765, text="")
            BAGASBASP4R2 = map_widget.set_marker(14.1382192, 122.9815507, text="BAGASBAS P-4")
            raw_coordinates.append([14.1372615, 122.9818765])
            raw_coordinates.append([14.1382192, 122.9815507])
            raw_routes.append(BAGASBASP4R1)
            raw_routes.append(BAGASBASP4R2)

        if i == 'BAGASBASP5':
            BAGASBASP5R1 = map_widget.set_marker(14.1391814, 122.9813583, text="")
            BAGASBASP5R2 = map_widget.set_marker(14.1395615, 122.9809399, text="")
            BAGASBASP5R3 = map_widget.set_marker(14.1394731, 122.9805521, text="")
            BAGASBASP5R4 = map_widget.set_marker(14.1396144, 122.9795064, text="BAGASBAS P-5")
            raw_coordinates.append([14.1391814, 122.9813583])
            raw_coordinates.append([14.1395615, 122.9809399])
            raw_coordinates.append([14.1394731, 122.9805521])
            raw_coordinates.append([14.1396144, 122.9795064])
            raw_routes.append(BAGASBASP5R1)
            raw_routes.append(BAGASBASP5R2)
            raw_routes.append(BAGASBASP5R3)
            raw_routes.append(BAGASBASP5R4)

        if i == 'BAGASBASP6':
            BAGASBASP5R1 = map_widget.set_marker(14.1397425, 122.9791444, text="")
            BAGASBASP5R0 = map_widget.set_marker(14.1406582, 122.9782365, text="")
            BAGASBASP5R2 = map_widget.set_marker(14.1412681, 122.9779479, text="BAGASBAS P-6")
            BAGASBASP5R3 = map_widget.set_marker(14.1410821, 122.9775614, text="BAGASBAS P-6")
            raw_coordinates.append([14.1397425, 122.9791444])
            raw_coordinates.append([14.1406582, 122.9782365])
            raw_coordinates.append([14.1412681, 122.9779479])
            raw_coordinates.append([14.1410821, 122.9775614])
            raw_routes.append(BAGASBASP5R1)
            raw_routes.append(BAGASBASP5R0)
            raw_routes.append(BAGASBASP5R2)
            raw_routes.append(BAGASBASP5R3)

        # MANTABAC
        # MANTAGABAC
        if i == 'MANTAGBACP9':
            MANTAGBACP9 = map_widget.set_marker(14.1177123, 122.9460971, text="")
            MANTAGBACP9R1 = map_widget.set_marker(14.1169254, 122.9463036, text="")
            MANTAGBACP9R2 = map_widget.set_marker(14.1167239, 122.9462821, text="")
            MANTAGBACP9R3 = map_widget.set_marker(14.1166536, 122.9468052, text="")
            MANTAGBACP9R4 = map_widget.set_marker(14.1159503, 122.9472847, text="")
            MANTAGBACP9R5 = map_widget.set_marker(14.1157874, 122.9475779, text="")
            MANTAGBACP9R6 = map_widget.set_marker(14.1154143, 122.9475733, text="")
            MANTAGBACP9R7 = map_widget.set_marker(14.1153250, 122.9477136, text="")
            MANTAGBACP9R8 = map_widget.set_marker(14.1152331, 122.9476906, text="")
            MANTAGBACP9R9 = map_widget.set_marker(14.1150695, 122.9482564, text="MANTAGBACP9")

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

        if i == 'MANTAGBACP8':
            MANTAGBACP8 = map_widget.set_marker(14.1169987, 122.9496214, text="")
            MANTAGBACP8R1 = map_widget.set_marker(14.1163912, 122.9505200, text="MANTAGBACP8")

            raw_coordinates.append([14.1169987, 122.9496214])
            raw_coordinates.append([14.1163912, 122.9505200])

            raw_routes.append(MANTAGBACP8)
            raw_routes.append(MANTAGBACP8R1)

        if i == 'MANTAGBACP7':
            MANTAGBACP7 = map_widget.set_marker(14.1167328, 122.9506844, text="MANTAGBACP7")

            raw_coordinates.append([14.1167328, 122.9506844])

            raw_routes.append(MANTAGBACP7)

        if i == 'MANTAGBACP6':
            MANTAGBACP6 = map_widget.set_marker(14.1164964, 122.9512647, text="")
            MANTAGBACP6R1 = map_widget.set_marker(14.1164586, 122.9516573, text="")
            MANTAGBACP6R2 = map_widget.set_marker(14.1164936, 122.9518366, text="MANTAGBACP6")

            raw_coordinates.append([14.1164964, 122.9512647])
            raw_coordinates.append([14.1164586, 122.9516573])
            raw_coordinates.append([14.1164936, 122.9518366])

            raw_routes.append(MANTAGBACP6)
            raw_routes.append(MANTAGBACP6R1)
            raw_routes.append(MANTAGBACP6R2)

        if i == 'MANTAGBACP5':
            MANTAGBACP5 = map_widget.set_marker(14.1164964, 122.9512647, text="")
            MANTAGBACP5R1 = map_widget.set_marker(14.1164586, 122.9516573, text="")
            MANTAGBACP5R2 = map_widget.set_marker(14.1164936, 122.9518366, text="MANTAGBACP5")

            raw_coordinates.append([14.1164964, 122.9512647])
            raw_coordinates.append([14.1164586, 122.9516573])
            raw_coordinates.append([14.1164936, 122.9518366])

            raw_routes.append(MANTAGBACP5)
            raw_routes.append(MANTAGBACP5R1)
            raw_routes.append(MANTAGBACP5R2)

        if i == 'MANTAGBACP4':
            MANTAGBACP4 = map_widget.set_marker(14.1164964, 122.9512647, text="")
            MANTAGBACP4R1 = map_widget.set_marker(14.1164586, 122.9516573, text="")
            MANTAGBACP4R2 = map_widget.set_marker(14.1164936, 122.9518366, text="MANTAGBACP4")

            raw_coordinates.append([14.1164964, 122.9512647])
            raw_coordinates.append([14.1164586, 122.9516573])
            raw_coordinates.append([14.1164936, 122.9518366])

            raw_routes.append(MANTAGBACP4)
            raw_routes.append(MANTAGBACP4R1)
            raw_routes.append(MANTAGBACP4R2)

        if i == 'MANTAGBACP3':
            MANTAGBACP3 = map_widget.set_marker(14.1153356, 122.9522397, text="MANTAGBACP3")

            raw_coordinates.append([14.1153356, 122.9522397])

            raw_routes.append(MANTAGBACP3)

        if i == 'MANTAGBACP2':
            MANTAGBACP2 = map_widget.set_marker(14.1146878, 122.9533740, text="MANTAGBACP2")

            raw_coordinates.append([14.1146878, 122.9533740])

            raw_routes.append(MANTAGBACP2)

        if i == 'MANTAGBACP1':
            MANTAGBACP1 = map_widget.set_marker(14.1145124, 122.9543546, text="MANTAGBACP1")

            raw_coordinates.append([14.1145124, 122.9543546])

            raw_routes.append(MANTAGBACP1)

        # BARANGAY VI
        if i == 'BRGY6P3':
            BRGY6P3 = map_widget.set_marker(14.1175173, 122.9556059, text="")

            raw_coordinates.append([14.1175173, 122.9556059])

            raw_routes.append(BRGY6P3)

        if i == 'BRGY6P4':
            BRGY6P4 = map_widget.set_marker(14.1163238, 122.9549512, text="")

            raw_coordinates.append([14.1163238, 122.9549512])

            raw_routes.append(BRGY6P4)

        if i == 'BRGY6P2':
            BRGY6P2 = map_widget.set_marker(14.1188769, 122.9561232, text="")
            BRGY6P3 = map_widget.set_marker(14.1194950, 122.9566621, text="")

            raw_coordinates.append([14.1188769, 122.9561232])
            raw_coordinates.append([14.1194950, 122.9566621])

            raw_routes.append(BRGY6P2)
            raw_routes.append(BRGY6P3)
        if i == 'BRGY6P5':
            BRGY6P5R1 = map_widget.set_marker(14.1205877, 122.9572032, text="")

            raw_coordinates.append([14.1205877, 122.9572032])

            raw_routes.append(BRGY6P5R1)

        if i == 'BRGY6P1':
            BRGY6P5R1 = map_widget.set_marker(14.1214089, 122.9576172, text="")

            raw_coordinates.append([14.1214089, 122.9576172])

            raw_routes.append(BRGY6P5R1)

        if i == 'BRGY6P4R1':
            BRGY6P4R1 = map_widget.set_marker(14.1156730, 122.9559872, text="")
            BRGY6P4R2 = map_widget.set_marker(14.1155325, 122.9565719, text="")

            raw_coordinates.append([14.1156730, 122.9559872])
            raw_coordinates.append([14.1155325, 122.9565719])

            raw_routes.append(BRGY6P4R1)
            raw_routes.append(BRGY6P4R2)

            # BARANGAY VIII
        if i == 'BRGY8P1':
            BRGY6P4R2 = map_widget.set_marker(14.1148785, 122.9564332, text="")
            BRGY8P1 = map_widget.set_marker(14.1148224, 122.9568969, text="BRGY8P1")

            raw_coordinates.append([14.1148785, 122.9564332])
            raw_coordinates.append([14.1148224, 122.9568969])

            raw_routes.append(BRGY6P4R2)
            raw_routes.append(BRGY8P1)

        ''' BFP = map_widget.set_marker(14.1181476, 122.9458182, text="BFP")
        BRGY8P1 = map_widget.set_marker(14.1176880, 122.9459791, text="")
        BRGY8P1R1 = map_widget.set_marker(14.1188031, 122.9495429, text="Bok's Kinalas")
        BRGY8P1R2 = map_widget.set_marker(14.1191171, 122.9504186, text="")
        BRGY8P1R3 = map_widget.set_marker(14.1174605, 122.9531266, text="SM Hypermart")
        BRGY8P1R4 = map_widget.set_marker(14.1156273, 122.9560826, text="Jollibee")
        BRGY8P1R5 = map_widget.set_marker(14.1155496, 122.9565470, text="")
        BRGY8P1R6 = map_widget.set_marker(14.1148785, 122.9564332, text="")
        BRGY8P1R7 = map_widget.set_marker(14.1148224, 122.9568969, text="BRGY8P1")

        raw_coordinates.append([14.1181476, 122.9458182])
        raw_coordinates.append([14.1176880, 122.9459791])
        raw_coordinates.append([14.1188031, 122.9495429])
        raw_coordinates.append([14.1191171, 122.9504186])
        raw_coordinates.append([14.1174605, 122.9531266])
        raw_coordinates.append([14.1156273, 122.9560826])
        raw_coordinates.append([14.1155496, 122.9565470])
        raw_coordinates.append([14.1148785, 122.9564332])
        raw_coordinates.append([14.1148224, 122.9568969])

        raw_routes.append(BFP)
        raw_routes.append(BRGY8P1)
        raw_routes.append(BRGY8P1R1)
        raw_routes.append(BRGY8P1R2)
        raw_routes.append(BRGY8P1R3)
        raw_routes.append(BRGY8P1R4)
        raw_routes.append(BRGY8P1R5)
        raw_routes.append(BRGY8P1R6)
        raw_routes.append(BRGY8P1R7)'''

        if i == 'BRGY8P2':
            BRGY6P4R2 = map_widget.set_marker(14.1148785, 122.9564332, text="")
            BRGY6P4R3 = map_widget.set_marker(14.1141362, 122.9563149, text="")
            BRGY8P2 = map_widget.set_marker(14.1140385, 122.9568769, text="BRGY8P2")

            raw_coordinates.append([14.1148785, 122.9564332])
            raw_coordinates.append([14.1141362, 122.9563149])
            raw_coordinates.append([14.1140385, 122.9568769])

            raw_routes.append(BRGY6P4R2)
            raw_routes.append(BRGY6P4R3)
            raw_routes.append(BRGY8P2)
            '''BRGY8P2 = map_widget.set_marker(14.1176880, 122.9459791, text="")
            BRGY8P2R1 = map_widget.set_marker(14.1188031, 122.9495429, text="Bok's Kinalas")
            BRGY8P2R2 = map_widget.set_marker(14.1191171, 122.9504186, text="")
            BRGY8P2R3 = map_widget.set_marker(14.1174605, 122.9531266, text="SM Hypermart")
            BRGY8P2R4 = map_widget.set_marker(14.1156273, 122.9560826, text="Jollibee")
            BRGY8P2R5 = map_widget.set_marker(14.1155496, 122.9565470, text="")

            raw_coordinates.append([14.1176880, 122.9459791])
            raw_coordinates.append([14.1188031, 122.9495429])
            raw_coordinates.append([14.1191171, 122.9504186])
            raw_coordinates.append([14.1174605, 122.9531266])
            raw_coordinates.append([14.1156273, 122.9560826])
            raw_coordinates.append([14.1155496, 122.9565470])

            raw_routes.append(BRGY8P2)
            raw_routes.append(BRGY8P2R1)
            raw_routes.append(BRGY8P2R2)
            raw_routes.append(BRGY8P2R3)
            raw_routes.append(BRGY8P2R4)
            raw_routes.append(BRGY8P2R5)'''

        if i == 'BRGY8P3':
            BRGY8R1P3 = map_widget.set_marker(14.1147994, 122.9570564, text="Leon D. Hernandez Hospital")
            BRGY8P3 = map_widget.set_marker(14.1146392, 122.9582024, text="BRGY8P3")

            raw_coordinates.append([14.1147994, 122.9570564])
            raw_coordinates.append([14.1146392, 122.9582024])

            raw_routes.append(BRGY8R1P3)
            raw_routes.append(BRGY8P3)

        if i == 'BRGY8P4':
            BRGY8P4 = map_widget.set_marker(14.1138253, 122.9580020, text="BRGY8P4")

            raw_coordinates.append([14.1138253, 122.9580020])

            raw_routes.append(BRGY8P4)

        if i == 'BRGY8P5':
            BRGY8R1P5 = map_widget.set_marker(14.1145426, 122.9586826, text="")
            BRGY8P5 = map_widget.set_marker(14.1150408, 122.9588421, text="BRGY8P5")

            raw_coordinates.append([14.1145426, 122.9586826])
            raw_coordinates.append([14.1150408, 122.9588421])

            raw_routes.append(BRGY8R1P5)
            raw_routes.append(BRGY8P5)

        if i == 'BRGY8P6':
            BRGY8P6 = map_widget.set_marker(14.1142710, 122.9596514, text="BRGY8P6")

            raw_coordinates.append([14.1142710, 122.9596514])

            raw_routes.append(BRGY8P6)

        if i == 'BRGY8P7':
            BRGY8P7 = map_widget.set_marker(14.1135273, 122.9594461, text="BRGY8P7")

            raw_coordinates.append([14.1135273, 122.9594461])

            raw_routes.append(BRGY8P7)

        if i == 'BRGY8P8':
            BRGY8P8 = map_widget.set_marker(14.1135273, 122.9594461, text="BRGY8P8")

            raw_coordinates.append([14.1135273, 122.9594461])

            raw_routes.append(BRGY8P8)

        if i == 'BRGY8P9':
            BRGY8P9 = map_widget.set_marker(14.1133808, 122.9620273, text="BRGY8P9")

            raw_coordinates.append([14.1133808, 122.9620273])

            raw_routes.append(BRGY8P9)

        if i == 'BRGY8P10':
            BRGY8P10 = map_widget.set_marker(14.1133080, 122.9635932, text="BRGY8P10")

            raw_coordinates.append([14.1133080, 122.9635932])

            raw_routes.append(BRGY8P10)

        # BARANGAY 7
        if i == 'BRGY7P1':
            BRGY6P4R1 = map_widget.set_marker(14.1156730, 122.9559872, text="")
            BRGY7P1 = map_widget.set_marker(14.1160692, 122.9553302, text="BRGY7P1")

            raw_coordinates.append([14.1156730, 122.9559872])
            raw_coordinates.append([14.1160692, 122.9553302])

            raw_routes.append(BRGY6P4R1)
            raw_routes.append(BRGY7P1)

        if i == 'BRGY7P2':
            BRGY6P4R1 = map_widget.set_marker(14.1156730, 122.9559872, text="")
            BRGY7P2 = map_widget.set_marker(14.1154326, 122.9580293, text="BRGY7P2")

            raw_coordinates.append([14.1156730, 122.9559872])
            raw_coordinates.append([14.1154326, 122.9580293])

            raw_routes.append(BRGY6P4R1)
            raw_routes.append(BRGY7P2)

        if i == 'BRGY7P3':
            BRGY7P3 = map_widget.set_marker(14.1152903, 122.9601384, text="BRGY7P3")

            raw_coordinates.append([14.1152903, 122.9601384])

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
            BRGY7P6 = map_widget.set_marker(14.1188769, 122.9561232, text="BRGY7P6")
            BRGY6P3 = map_widget.set_marker(14.1194950, 122.9566621, text="BRGY6P3")

            raw_coordinates.append([14.1188769, 122.9561232])
            raw_coordinates.append([14.1194950, 122.9566621])

            raw_routes.append(BRGY7P6)
            raw_routes.append(BRGY6P3)

        if i == 'BRGY7P7':
            BRGY7P7 = map_widget.set_marker(14.1152903, 122.9601384, text="BRGY7P7")

            raw_coordinates.append([14.1152903, 122.9601384])

            raw_routes.append(BRGY7P7)

        # GUBAT
        if i == 'BRGYGUBATP1GUYABANO':
            BRGYGUBATP1GUYABANO = map_widget.set_marker(14.1148391, 122.9666635, text="BRGYGUBATP1GUYABANO")

            raw_coordinates.append([14.1148391, 122.9666635])

            raw_routes.append(BRGYGUBATP1GUYABANO)

        if i == 'BRGYGUBATP2UBAS':
            BRGYGUBATP2UBAS = map_widget.set_marker(14.1148391, 122.9666635, text="BRGYGUBATP2UBAS")

            raw_coordinates.append([14.1148391, 122.9666635])

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

        # BRGY 2 PASIG
        if i == 'BRGY2PASIGP6':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            LAGONP1 = map_widget.set_marker(14.1168800, 122.9432159, text="LAGONP1")
            LAGON = map_widget.set_marker(14.1156366, 122.9409842, text="LAGON")
            BRGY2PASIGP6 = map_widget.set_marker(14.1031818, 122.9525520, text="BRGY2PASIGP6")

            raw_coordinates.append([14.1181492, 122.9458283])
            raw_coordinates.append([14.1168800, 122.9432159])
            raw_coordinates.append([14.1156366, 122.9409842])
            raw_coordinates.append([14.1031818, 122.9525520])

            raw_routes.append(BFP)
            raw_routes.append(LAGONP1)
            raw_routes.append(LAGON)
            raw_routes.append(BRGY2PASIGP6)

        if i == 'BRGY2PASIGP5':
            BRGY2PASIGP5 = map_widget.set_marker(14.1056096, 122.9562315, text="BRGY2PASIGP5")

            raw_coordinates.append([14.1056096, 122.9562315])

            raw_routes.append(BRGY2PASIGP5)

        if i == 'BRGY2PASIGP7':
            BRGY2PASIGP7R8 = map_widget.set_marker(14.1056096, 122.9562315, text="BRGY2PASIGP7")

            raw_coordinates.append([14.1056096, 122.9562315])

            raw_routes.append(BRGY2PASIGP7R8)

        if i == 'BRGY2PASIGP4':
            BRGY2PASIGP4 = map_widget.set_marker(14.1061997, 122.9561878, text="BRGY2PASIGP4")

            raw_coordinates.append([14.1061997, 122.9561878])

            raw_routes.append(BRGY2PASIGP4)

        if i == 'BRGY2PASIGP3':
            BRGY2PASIGP3 = map_widget.set_marker(14.1068290, 122.9561473, text="BRGY2PASIGP3")

            raw_coordinates.append([14.1068290, 122.9561473])

            raw_routes.append(BRGY2PASIGP3)

        if i == 'BRGY2PASIGP2':
            BRGY2PASIGP2 = map_widget.set_marker(14.1074794, 122.9561044, text="BRGY2PASIGP2")

            raw_coordinates.append([14.1074794, 122.9561044])

            raw_routes.append(BRGY2PASIGP2)

        if i == 'BRGY2PASIGP1':
            BRGY6P4R2 = map_widget.set_marker(14.1148785, 122.9564332, text="")
            BRGY6P4R3 = map_widget.set_marker(14.1141362, 122.9563149, text="")
            BRGY2P8R1 = map_widget.set_marker(14.1129875, 122.9560712, text="")
            BRGY2PASIGP1 = map_widget.set_marker(14.1081609, 122.9560615, text="BRGY2PASIGP1")

            raw_coordinates.append([14.1148785, 122.9564332])
            raw_coordinates.append([14.1141362, 122.9563149])
            raw_coordinates.append([14.1129875, 122.9560712])
            raw_coordinates.append([14.1081609, 122.9560615])

            raw_routes.append(BRGY6P4R2)
            raw_routes.append(BRGY6P4R3)
            raw_routes.append(BRGY2P8R1)
            raw_routes.append(BRGY2PASIGP1)

        if i == 'BRGY2PASIGP8':
            BRGY6P4R2 = map_widget.set_marker(14.1148785, 122.9564332, text="")
            BRGY6P4R3 = map_widget.set_marker(14.1141362, 122.9563149, text="")
            BRGY2P8R1 = map_widget.set_marker(14.1129875, 122.9560712, text="")
            BRGY2PASIGP8 = map_widget.set_marker(14.1081609, 122.9560615, text="BRGY2PASIGP8")

            raw_coordinates.append([14.1148785, 122.9564332])
            raw_coordinates.append([14.1141362, 122.9563149])
            raw_coordinates.append([14.1129875, 122.9560712])
            raw_coordinates.append([14.1081609, 122.9560615])

            raw_routes.append(BRGY6P4R2)
            raw_routes.append(BRGY6P4R3)
            raw_routes.append(BRGY2P8R1)
            raw_routes.append(BRGY2PASIGP8)

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
            CAMAMBUGANP3R1 = map_widget.set_marker(14.1064892, 122.9495115, text="")

            raw_coordinates.append([14.1064892, 122.9495115])

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
            CAMAMBUGANP6R1 = map_widget.set_marker(14.1132455, 122.9518581, text="")

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
            MAGANGP1 = map_widget.set_marker(14.1014259, 122.9541984, text="Magang P-1")
            raw_coordinates.append([14.1014259, 122.9541984])

            raw_routes.append(MAGANGP1)

        if i == 'MAGANGP2':
            MAGANGP2R1 = map_widget.set_marker(14.1008177, 122.9548042)
            MAGANGP2 = map_widget.set_marker(14.0991605, 122.9523294, text="Magang P-2")

            raw_coordinates.append([14.1008177, 122.9548042])
            raw_coordinates.append([14.0991605, 122.9523294])

            raw_routes.append(MAGANGP2R1)
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

            raw_coordinates.append([14.1013062, 122.9506929])

            raw_routes.append(MAGANGP5)

        if i == 'MAGANGP6':
            MAGANGP6 = map_widget.set_marker(14.093771429391841, 122.94453425116983, text="Magang P-6")

            raw_coordinates.append([14.093771429391841, 122.94453425116983])

            raw_routes.append(MAGANGP6)

        if i == 'PAMORANGONP1':
            PAMORANGONP1R2 = map_widget.set_marker(14.09918256873587, 122.95653512316036)
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
            PAMORANGONPR1 = map_widget.set_marker(14.0904744, 122.9579470)
            PAMORANGONPR2 = map_widget.set_marker(14.0909216, 122.9579904)
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
            PAMORANGONP6R1 = map_widget.set_marker(14.0903762, 122.9580091)
            PAMORANGONP6R2 = map_widget.set_marker(14.0903363, 122.9583052)
            PAMORANGONP6 = map_widget.set_marker(14.086770677594686, 122.96323398578951, text="Pamorangon P-6")

            raw_coordinates.append([14.0903762, 122.9580091])
            raw_coordinates.append([14.0903363, 122.9583052])
            raw_coordinates.append([14.086770677594686, 122.96323398578951])

            raw_routes.append(PAMORANGONP6R1)
            raw_routes.append(PAMORANGONP6R2)
            raw_routes.append(PAMORANGONP6)

        if i == 'MANCRUZP4':
            MANRCRUZP4R1 = map_widget.set_marker(14.0992103, 122.9563215)
            MANRCRUZP4R2 = map_widget.set_marker(14.0986662, 122.9565453)

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
            MANRCRUZP3R1 = map_widget.set_marker(14.0912982, 122.9564243)
            MANRCRUZP3R2 = map_widget.set_marker(14.0915791, 122.9563653)
            MANRCRUZP3R3 = map_widget.set_marker(14.0920940, 122.9551532)
            MANCRUZP3 = map_widget.set_marker(14.091702085263828, 122.95445844588974, text="Mancruz P-3")

            raw_coordinates.append([14.0912982, 122.9564243])
            raw_coordinates.append([14.0915791, 122.9563653])
            raw_coordinates.append([14.0920940, 122.9551532])
            raw_coordinates.append([14.091702085263828, 122.95445844588974])

            raw_routes.append(MANRCRUZP3R1)
            raw_routes.append(MANRCRUZP3R2)
            raw_routes.append(MANRCRUZP3R3)
            raw_routes.append(MANCRUZP3)

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
            SANISIDROP3R1 = map_widget.set_marker(14.1107597, 122.9682556)
            SANISIDROP3 = map_widget.set_marker(14.1096182, 122.9717979, text="San Isidro P-3")

            raw_coordinates.append([14.1107597, 122.9682556])
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


        
        if i == 'GAHONONP1':

            GAHONONP1 = map_widget.set_marker(14.1270539, 122.9374078, text="Gahonon P-1")

            raw_coordinates.append([14.1270539, 122.9374078])

            raw_routes.append(GAHONONP1)

        if i == 'GAHONONP2':

            GAHONONP2 = map_widget.set_marker(14.1230131, 122.9536979, text="Gahonon P-2")

            raw_coordinates.append([14.1230131, 122.9536979])

            raw_routes.append(GAHONONP2)

        if i == 'GAHONONP3':

            GAHONONP3 = map_widget.set_marker(14.1191182, 122.9504007, text="Gahonon P-3")

            raw_coordinates.append([14.1191182, 122.9504007])

            raw_routes.append(GAHONONP3)

        if i == 'GAHONONP4':

            GAHONONP4 = map_widget.set_marker(14.1261811, 122.9601951, text="Gahonon P-4")

            raw_coordinates.append([14.1261811, 122.9601951])

            raw_routes.append(GAHONONP4)

        if i == 'GAHONONP5':

            GAHONONP5 = map_widget.set_marker(14.1300438, 122.9689899, text="Gahonon P-5")

            raw_coordinates.append([14.1300438, 122.9689899])

            raw_routes.append(GAHONONP5)

        if i == 'GAHONONP6':

            GAHONONP6 = map_widget.set_marker(14.1322409, 122.9509966, text="Gahonon P-6")

            raw_coordinates.append([14.1322409, 122.9509966])

            raw_routes.append(GAHONONP6)


    return raw_routes, raw_coordinates

# ----> Algorithm Pang determine ng destination <-------------------

def Set(barangay, destination):
    global specific_routes_label, specific_routes_label, firetruck_icon

    index = get_index_by_purok(all_purok, destination)

    fetch_location = all_location[barangay]
    final_destination = fetch_location[index]

    destination_routes, shortest_distance_path, result_string = GetShortestPath("BFP", final_destination)

    routes, coordinates = GetCoordinates(destination_routes)

    firetruck_icon = PhotoImage(file="firetruck.png")

    view_btn['command'] = lambda:show_notifier(destination_routes,shortest_distance_path, result_string)

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

    for i, coordinate in enumerate(coordinates):
        root.after(500 * i, lambda i=i, coordinate=tuple(coordinate): update_firetruck_position(coordinate, firetruck_icon))


    view_btn['state'] = 'normal'

# ----> Algorithm Pang reset ng lahat ng fields <-------------------

def RemoveCoordinates():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()

    purok_combo_var.set("")
    barangay_combo_var.set("")

    view_btn['state'] = "disabled"
    purok_combo_box['state'] = "disabled"

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
    global my_label, root, canvas, map_widget, routes_label, total_distance_label, barangay_combo_var, purok_combo_box, purok_combo_var, view_btn
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

    view_btn = Button(canvas, text="View", command=lambda:show_notifier(" "), width=10, height=1)
    canvas.create_window(1115, 50, window=view_btn)

    remove_coordinates_button = Button(root, text="Reset", fg="black", width=11, height=2, bg="orange",
                                       command=RemoveCoordinates)
    canvas.create_window(1110, 600, window=remove_coordinates_button)

    canvas.create_window(1110, 600, window=remove_coordinates_button)
    create_firetruck_icon()
    root.mainloop()

MainMenu()