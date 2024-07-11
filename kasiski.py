
# LOSIENTOPERONOQUIEROSEREMPERADORESENOESMIOFIOSINOAYUDARATODOSSIFUERAPOSIBLEBLANCOSONEGROSJUDIOSOGENTILESTENEMOSQUEAYUDARNOSLOSUNOSALOSOTROSLOSSERESHUMANOSSOMOSASIQUEREMOSHACERFELICESALOSDEMASNOHACERNOSDESGRACIADOSNOQUEREMOSODIARNIDESPRECIARANADIENESTEMUNDOHAYSITIOPARATODOSYLABUENATIERRAESRICAYPUEDEALIMENTARATODOSLOSSERESELCAMINODELAVIDAPUEDESERLIBREYHERMOSOPERDIDOLACODICIAHAENVENENADOLASARMASHALEVANTADOBARRERASDEODIONOSHAEMPUJADOHACIALASMISERIASYLASMATANZAS
# WWCMPQGIOIJAUYUGMQLÑWVDMVTPVNWÑVVEMWSPWYBÑJZAARQAELÑCEJMBYHAWFBEYVDIZSEMÑEDFCMUMSESZXFVGEQEHTSFIFIEFPUIEXQGDPGEYEIMCHWZVEAAUSEYZIRECAAYXDSFEÑWKPZÑWSYYTMSKEWVSEEFBPYVDMVSELNVDVWPSRGPWNEÑWUPTKWYSTTBIJYWCHPWSLZGZMLYWYSDÑDVVXWCSOMNLMMUPAZVPGUTQEEMLRIYIFNDPMYLYLMCFBSMGBIBEFSPIRCCMJEIYEGBDVJMMCVTGNROYVOMKOTPQGSEJMBYHAWXIRWVDMCIWGNFHQGOMUEHMPTOYVOMCIDOUUQIPSMBPAWBJDVUTLYOMGBWHGZMOKIYZQGDQROWUEEEEFZWYMSÑZMQGTCSSMZBIDEFWDSUTWWSELNXLTMUINSSEOBZORETRWPVUTRCCMAVEFEZSZW
# mikementzer
alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


encrypted=input("Mensaje encriptado> ")
intervals=input("Intervalo de digitos de la clave p.e 2-8> ")

intervals=[int(intervals.split("-")[0]), int(intervals.split("-")[1])]


for interval in range(intervals[0], intervals[1]+1):
    monoalphabetic=[]
    for position in range(0, interval):
        part=[]
        for i in range(position, len(encrypted), interval):
            part.append(encrypted[i])
        monoalphabetic.append(part)
    print("Clave de {} Caracteres".format(interval))
    input()
    for kasiskisegment in monoalphabetic:
        
        diff=[0,0]
        
        average=0
        typicaldeviation=0
        for letter in alphabet:
            if diff[0]< (kasiskisegment.count(letter)/len(kasiskisegment))*100:
                diff[0]=(kasiskisegment.count(letter)/len(kasiskisegment))*100
            if diff[1] > (kasiskisegment.count(letter)/len(kasiskisegment))*100:
                diff[1]=(kasiskisegment.count(letter)/len(kasiskisegment))*100
                
        print(diff[0]-diff[1])
        for letter in alphabet:
            
            print("{}: {}".format(letter, (kasiskisegment.count(letter)/len(kasiskisegment))*100, end= ","))
        print("\n")
        
            
        
    
    
