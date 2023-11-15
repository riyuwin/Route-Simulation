from tkinter import *
import tkintermapview
from DijsktraAlgo import GetShortestPath

paths_list = []

routes_label_list = []

# Pycharm Github Test

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
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1123827, 122.9589967, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1092531, 122.9591187, text="")
            COBANGBANGR8 = map_widget.set_marker(14.1068418, 122.9604321, text="COBANGBANGP3")

            raw_coordinates.append([14.1181492, 122.9458283]) 
            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1123827, 122.9589967])
            raw_coordinates.append([14.1092531, 122.9591187])
            raw_coordinates.append([14.1068418, 122.9604321])
            
            raw_routes.append(BFP)
            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)
            raw_routes.append(COBANGBANGR8)

        if i == 'COBANGBANGP2':
            COBANGBANGR9 = map_widget.set_marker(14.1057139, 122.9609740, text="COBANGBANGP2")
            raw_coordinates.append([14.1057139, 122.9609740])
            raw_routes.append(COBANGBANGR9)

        if i == 'COBANGBANGP4':
            COBANGBANGR12 = map_widget.set_marker(14.1041027, 122.9636565, text="COBANGBANGP4")
            raw_coordinates.append([14.1041027, 122.9636565])
            raw_routes.append(COBANGBANGR12)
 

        if i == 'COBANGBANGP5':
            COBANGBANGR12 = map_widget.set_marker(14.1035439, 122.9634229, text="COBANGBANGP5")
            raw_coordinates.append([14.1035439, 122.9634229])
            raw_routes.append(COBANGBANGR12)

        if i == 'COBANGBANGP1':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="")
            COBANGBANGR6 = map_widget.set_marker(14.1051243, 122.9562600, text="")
            COBANGBANGR7 = map_widget.set_marker(14.1050619, 122.9565872, text="COBANGBANGP1")

            raw_coordinates.append([14.1181492, 122.9458283])
            raw_coordinates.append([14.1176768, 122.9459699])
            raw_coordinates.append([14.1191045, 122.9504538])
            raw_coordinates.append([14.1156229, 122.9560923])
            raw_coordinates.append([14.1155481, 122.9565657])
            raw_coordinates.append([14.1129123, 122.9560684])
            raw_coordinates.append([14.1051243, 122.9562600])
            raw_coordinates.append([14.1050619, 122.9565872])


            raw_routes.append(BFP)
            raw_routes.append(COBANGBANGR1)
            raw_routes.append(COBANGBANGR2)
            raw_routes.append(COBANGBANGR3)
            raw_routes.append(COBANGBANGR4)
            raw_routes.append(COBANGBANGR5)
            raw_routes.append(COBANGBANGR6)
            raw_routes.append(COBANGBANGR7)

        if i == 'COBANGBANGP6':
            COBANGBANGR12 = map_widget.set_marker(14.1027421, 122.9658796, text="COBANGBANGP6")
            raw_coordinates.append([14.1027421, 122.9658796])
            raw_routes.append(COBANGBANGR12)

        if i == 'AWITANP3':
            AWITANPR1 = map_widget.set_marker(14.1242738, 122.9449423, text="")
            AWITANPR2 = map_widget.set_marker(14.1271756, 122.9494915, text="")
            AWITANPR3 = map_widget.set_marker(14.1272848, 122.9496418, text="")
            AWITANPR4 = map_widget.set_marker(14.1341248, 122.9512816, text="")
            AWITANPR5 = map_widget.set_marker(14.1375581, 122.9561655, text="")
            AWITANPR6 = map_widget.set_marker(14.1387866, 122.9591850, text="AWITANP3")
            

            raw_coordinates.append([14.1242738, 122.9449423])
            raw_coordinates.append([14.1271756, 122.9494915])
            raw_coordinates.append([14.1272848, 122.9496418])
            raw_coordinates.append([14.1341248, 122.9512816])
            raw_coordinates.append([14.1375581, 122.9561655])
            raw_coordinates.append([14.1387866, 122.9591850])
            

            raw_routes.append(AWITANPR1)
            raw_routes.append(AWITANPR2)
            raw_routes.append(AWITANPR3)
            raw_routes.append(AWITANPR4)
            raw_routes.append(AWITANPR5)
            raw_routes.append(AWITANPR6)
            

        if i == 'AWITANP1':
            
            AWITANPR2 = map_widget.set_marker(14.1393543, 122.9606005, text="AWITANP1")
            
            raw_coordinates.append([14.1393543, 122.9606005])
            
            raw_routes.append(AWITANPR2)
            

        if i == 'AWITANP2':
            AWITANPR1 = map_widget.set_marker(14.1412362, 122.9642978, text="")
            AWITANPR2 = map_widget.set_marker(14.1408167, 122.9650377, text="AWITANP2")
            raw_coordinates.append([14.1412362, 122.9642978])
            raw_coordinates.append([14.1408167, 122.9650377])
            raw_routes.append(AWITANPR1)
            raw_routes.append(AWITANPR2)

        # BARANGAY 1

        if i == 'BARANGAY1P1':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            COBANGBANGR1 = map_widget.set_marker(14.1176768, 122.9459699, text="")
            COBANGBANGR2 = map_widget.set_marker(14.1191045, 122.9504538, text="")
            COBANGBANGR3 = map_widget.set_marker(14.1156229, 122.9560923, text="")
            COBANGBANGR4 = map_widget.set_marker(14.1155481, 122.9565657, text="")
            COBANGBANGR5 = map_widget.set_marker(14.1129123, 122.9560684, text="BARANGAY1P1")

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
            COBANGBANGR6 = map_widget.set_marker(14.1125961, 122.9570849, text="BARANGAY1P2")
            raw_coordinates.append([14.1125961, 122.9570849])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P3':
            COBANGBANGR6 = map_widget.set_marker(14.1124742, 122.9581552, text="BARANGAY1P3")
            raw_coordinates.append([14.1124742, 122.9581552])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P4':
            COBANGBANGR6 = map_widget.set_marker(14.1108681, 122.9559878, text="BARANGAY1P4")
            raw_coordinates.append([14.1108681, 122.9559878])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P5':
            COBANGBANGR6 = map_widget.set_marker(14.1102707, 122.9559953, text="BARANGAY1P5")
            raw_coordinates.append([14.1102707, 122.9559953])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P6':
            COBANGBANGR6 = map_widget.set_marker(14.1123945, 122.9589966, text="BARANGAY1P6")
            raw_coordinates.append([14.1123945, 122.9589966])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P7':
            COBANGBANGR6 = map_widget.set_marker(14.1121612, 122.9598197, text="BARANGAY1P7")
            raw_coordinates.append([14.1121612, 122.9598197])
            raw_routes.append(COBANGBANGR6)

        if i == 'BARANGAY1P8':
            COBANGBANGR6 = map_widget.set_marker(14.1119425, 122.9605981, text="BARANGAY1P8")
            raw_coordinates.append([14.1119425, 122.9605981])
            raw_routes.append(COBANGBANGR6)

        # BORABOD

        if i == 'BORABODP1':
            BFP = map_widget.set_marker(14.1181492, 122.9458283, text="BFP")
            BORABODP1R1 = map_widget.set_marker(14.1176829, 122.9459697, text="")
            BORABODP1R2 = map_widget.set_marker(14.1190924, 122.9504048, text="")
            BORABODP1R3 = map_widget.set_marker(14.1201678, 122.9511875, text="")
            BORABODP1R4 = map_widget.set_marker(14.1175244, 122.9556175, text="")
            BORABODP1R5 = map_widget.set_marker(14.1240610, 122.9589386, text="BORABODP1")

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
            BORABODP2R2 = map_widget.set_marker(14.1265685, 122.9613863, text="BORABODP2")
            raw_coordinates.append([14.1257225, 122.9597660])
            raw_coordinates.append([14.1265685, 122.9613863])
            raw_routes.append(BORABODP2R1)
            raw_routes.append(BORABODP2R2)

        if i == 'BORABODP3':
            BORABODP3R1 = map_widget.set_marker(14.1266691, 122.9615567, text="BORABODP3")
            raw_coordinates.append([14.1266691, 122.9615567])
            raw_routes.append(BORABODP3R1)

        if i == 'BORABODP4':
            BORABODP4R1 = map_widget.set_marker(14.1279800, 122.9644454, text="BORABODP4")
            raw_coordinates.append([14.1279800, 122.9644454])
            raw_routes.append(BORABODP4R1)

        if i == 'BORABODP5':
            BORABODP5R1 = map_widget.set_marker(14.1305585, 122.9699444, text="BORABODP5")
            raw_coordinates.append([14.1305585, 122.9699444])
            raw_routes.append(BORABODP5R1)

        if i == 'BORABODP6':
            BORABODP6R1 = map_widget.set_marker(14.1316511, 122.9697172, text="")
            BORABODP6R2 = map_widget.set_marker(14.1334507, 122.9679562, text="BORABODP6")
            raw_coordinates.append([14.1316511, 122.9697172])
            raw_coordinates.append([14.1334507, 122.9679562])
            raw_routes.append(BORABODP6R1)
            raw_routes.append(BORABODP6R2)

        # BAGASBAS
        if i == 'BAGASBASP1':
            BAGASBASP1R1 = map_widget.set_marker(14.1347075, 122.9772225, text="")
            BAGASBASP1R2 = map_widget.set_marker(14.1340089, 122.9778572, text="BAGASBASP1")
            raw_coordinates.append([14.1347075, 122.9772225])
            raw_coordinates.append([14.1340089, 122.9778572])
            raw_routes.append(BAGASBASP1R1)
            raw_routes.append(BAGASBASP1R2)

        if i == 'BAGASBASP2':
            BAGASBASP2R1 = map_widget.set_marker(14.1347047, 122.9772304, text="")
            BAGASBASP2R2 = map_widget.set_marker(14.1357867, 122.9791636, text="")
            BAGASBASP2R3 = map_widget.set_marker(14.1337333, 122.9802586, text="BAGASBASP2")
            BAGASBASP2R4 = map_widget.set_marker(14.1357927, 122.9791616, text="")
            BAGASBASP2R5 = map_widget.set_marker(14.1361226, 122.9798357, text="")
            BAGASBASP2R6 = map_widget.set_marker(14.1341280, 122.9810421, text="BAGASBASP2")
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
            BAGASBASP3R1 = map_widget.set_marker(14.1369528, 122.9813355, text="BAGASBASP3")
            raw_coordinates.append([14.1369528, 122.9813355])
            raw_routes.append(BAGASBASP3R1)

        if i == 'BAGASBASP4':
            BAGASBASP4R1 = map_widget.set_marker(14.1372615, 122.9818765, text="")
            BAGASBASP4R2 = map_widget.set_marker(14.1382192, 122.9815507, text="BAGASBASP4")
            raw_coordinates.append([14.1372615, 122.9818765])
            raw_coordinates.append([14.1382192, 122.9815507])
            raw_routes.append(BAGASBASP4R1)
            raw_routes.append(BAGASBASP4R2)

        if i == 'BAGASBASP5':
            BAGASBASP5R1 = map_widget.set_marker(14.1394659, 122.9811681, text="")
            BAGASBASP5R2 = map_widget.set_marker(14.1396144, 122.9795064, text="BAGASBASP5")
            raw_coordinates.append([14.1394659, 122.9811681])
            raw_coordinates.append([14.1396144, 122.9795064])
            raw_routes.append(BAGASBASP5R1)
            raw_routes.append(BAGASBASP5R2)

        if i == 'BAGASBASP6':
            BAGASBASP5R1 = map_widget.set_marker(14.1406582, 122.9782365, text="")
            BAGASBASP5R2 = map_widget.set_marker(14.1413147, 122.9779582, text="BAGASBASP6")
            BAGASBASP5R3 = map_widget.set_marker(14.1410821, 122.9775614, text="BAGASBASP6")
            raw_coordinates.append([14.1406582, 122.9782365])
            raw_coordinates.append([14.1413147, 122.9779582])
            raw_coordinates.append([14.1410821, 122.9775614])
            raw_routes.append(BAGASBASP5R1)
            raw_routes.append(BAGASBASP5R2)
            raw_routes.append(BAGASBASP5R3)

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

# AWITAN

awitanp3 = Button(my_label, text="AWITANP3", command=lambda:Set('AWITANP3'))
awitanp3.pack(side="bottom")

awitanp1 = Button(my_label, text="AWITANP1", command=lambda:Set('AWITANP1'))
awitanp1.pack(side="bottom")

awitanp2 = Button(my_label, text="AWITANP2", command=lambda:Set('AWITANP2'))
awitanp2.pack(side="bottom")

# BARANGAY 1

barangay1p1 = Button(my_label, text="BARANGAY1P1", command=lambda:Set('BARANGAY1P1'))
barangay1p1.pack(side="bottom")

barangay1p2 = Button(my_label, text="BARANGAY1P2", command=lambda:Set('BARANGAY1P2'))
barangay1p2.pack(side="bottom")

barangay1p3 = Button(my_label, text="BARANGAY1P3", command=lambda:Set('BARANGAY1P3'))
barangay1p3.pack(side="bottom")

barangay1p4 = Button(my_label, text="BARANGAY1P4", command=lambda:Set('BARANGAY1P4'))
barangay1p4.pack(side="bottom")

barangay1p5 = Button(my_label, text="BARANGAY1P5", command=lambda:Set('BARANGAY1P5'))
barangay1p5.pack(side="bottom")

barangay1p6 = Button(my_label, text="BARANGAY1P6", command=lambda:Set('BARANGAY1P6'))
barangay1p6.pack(side="bottom")

barangay1p7 = Button(my_label, text="BARANGAY1P7", command=lambda:Set('BARANGAY1P7'))
barangay1p7.pack(side="bottom")

barangay1p8 = Button(my_label, text="BARANGAY1P8", command=lambda:Set('BARANGAY1P8'))
barangay1p8.pack(side="bottom")

# BORABOD

borabodp1 = Button(my_label, text="BORABODP1", command=lambda:Set('BORABODP1'))
borabodp1.pack(side="bottom")

borabodp2 = Button(my_label, text="BORABODP2", command=lambda:Set('BORABODP2'))
borabodp2.pack(side="bottom")

borabodp3 = Button(my_label, text="BORABODP3", command=lambda:Set('BORABODP3'))
borabodp3.pack(side="bottom")

borabodp4 = Button(my_label, text="BORABODP4", command=lambda:Set('BORABODP4'))
borabodp4.pack(side="bottom")

borabodp5 = Button(my_label, text="BORABODP5", command=lambda:Set('BORABODP5'))
borabodp5.pack(side="bottom")

borabodp6 = Button(my_label, text="BORABODP6", command=lambda:Set('BORABODP6'))
borabodp6.pack(side="bottom")

# BAGASBAS

bagasbasp1 = Button(my_label, text="BAGASBASP1", command=lambda:Set('BAGASBASP1'))
bagasbasp1.pack(side="bottom")

bagasbasp2 = Button(my_label, text="BAGASBASP2", command=lambda:Set('BAGASBASP2'))
bagasbasp2.pack(side="bottom")

bagasbasp3 = Button(my_label, text="BAGASBASP3", command=lambda:Set('BAGASBASP3'))
bagasbasp3.pack(side="bottom")

bagasbasp4 = Button(my_label, text="BAGASBASP4", command=lambda:Set('BAGASBASP4'))
bagasbasp4.pack(side="bottom")

bagasbasp5 = Button(my_label, text="BAGASBASP5", command=lambda:Set('BAGASBASP5'))
bagasbasp5.pack(side="bottom")

bagasbasp6 = Button(my_label, text="BAGASBASP6", command=lambda:Set('BAGASBASP6'))
bagasbasp6.pack(side="bottom")

remove_coordinates_button = Button(root, text="Reset", background="black", fg="gold", width=10, height=2, command=RemoveCoordinates)
canvas.create_window(1130, 600, window=remove_coordinates_button)

root.mainloop()
