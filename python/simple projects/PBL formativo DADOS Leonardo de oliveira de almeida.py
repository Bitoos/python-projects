DADOS = [["Argentina",44270440,45.4,34.26,8.59,2.64,8.4,0.44,0.21,0.06],
["Armênia", 2931568, 29.0, 46.3 ,12.0 ,5.6 ,2.0 ,3.7, 1.0, 0.4],
["Austrália", 24642693, 40.0, 31.0 ,8.0 ,2.0 ,9.0 ,7.0, 2.0 ,1.0],
["Áustria", 8592470, 30.0 ,33.0 ,12.0 ,6.0 ,7.0, 8.0, 3.0, 1.0],
["Barém", 1418695, 48.48, 19.35 ,22.61 ,3.67 ,3.27 ,1.33 ,1.04, 0.25],
["Bangladesh", 164833667 ,31.18 ,21.44 ,34.58, 8.85 ,1.39, 0.96 ,0.96, 0.64],
["Bélgica", 11444053 ,38.0 ,34.0 ,8.6 ,4.1 ,7.0, 6.0, 1.5 ,0.8],
["Bolívia", 11053376 ,51.53 ,29.45 ,10.11 ,1.15, 4.39, 2.73, 0.54,0.1],
["Bósnia e Herzegovina", 3792730, 31.0 ,36.0 ,12.0 ,6.0 ,5.0 ,7.0, 2.0 ,1.0],
["Brasil", 211248418, 36.0 ,34.0 ,8.0 ,2.5 ,9.0 ,8.0 ,2.0, 0.5],
["Bulgária", 7045097, 28.0, 37.0, 13.0 ,7.0, 5.0 ,7.0, 2.0 ,1.0],
["Camboja", 16077172 ,46.7 ,27.2 ,18.5 ,4.9 ,1.3, 0.8, 0.5, 0.1],
["Camarões", 24515533, 42.8, 38.8 ,12.0 ,3.3, 1.4, 1.2, 0.4, 0.1],
["Canadá", 36627140 ,39.0 ,36.0, 7.6, 2.5, 7.0, 6.0 ,1.4 ,0.5],
["Chile", 18314060 ,85.5 ,8.7, 3.35, 1.0, 1.2, 0.1 ,0.05, 0.1],
["China", 1388251023 ,47.7 ,27.8 ,18.9, 5.0, 0.28, 0.19, 0.1, 0.03],
["Colômbia", 49069267 ,61.3 ,26.11, 2.28, 1.47 ,5.13 ,2.7 ,0.7, 0.31],
["Costa do Marfim", 23869656 ,46.5 ,22.5 ,22.5, 4.3 ,2.0 ,1.0 ,1.0, 0.2],
["Croácia", 4207355, 29.0 ,36.0 ,15.0 ,5.0 ,5.0 ,6.0, 3.0, 1.0],
["Cuba", 11486750, 45.8, 33.5 ,10.2 ,2.9 ,3.6 ,2.8 ,1.0 ,0.2],
["Chipre", 1189395, 35.22 ,40.35 ,11.11, 4.72 ,3.85, 3.48, 0.87 ,0.40]]
matriza=[]
matrizb=[]
matrizc=[]
maior = 0
tabelaprint = []
for a1 in range(len(DADOS[0])):
    if a1 == 0 or a1 == 1:
        continue
    for a2 in range(len(DADOS)):
        if DADOS[a2][a1] >= maior:
            if int(DADOS[a2][a1]) == maior and pop > DADOS[a2][1]:
                ()
            else:
                maior = DADOS[a2][a1]
                nome = DADOS[a2][0]
                pop = DADOS[a2][1]
    if nome in tabelaprint:
        tabelaprint.append(maior)
    else:
        tabelaprint.append(nome)
        tabelaprint.append(maior)  
    entry = 0
    maior = 0
    '''fim primeira tabela'''
somaa=0
somab=0
somac=0
for a1 in range(len(DADOS)):
    if DADOS[a1][0][0] == 'A' or DADOS[a1][0][0] == 'Á':
        matriza.append(DADOS[a1])
    elif DADOS[a1][0][0] == 'B': 
        matrizb.append(DADOS[a1])
    elif DADOS[a1][0][0] == 'C': 
        matrizc.append(DADOS[a1])
    else:
        ()       
matrizafinal = []
matrizbfinal = []
matrizcfinal = []
for b1 in range(len(DADOS[0])):
    somaa = 0
    somab = 0
    somac = 0
    if b1 == 0 or b1 == 1:
        continue
    else:
        for b2 in range(len(matriza)):
            somaa = matriza[b2][b1] + somaa
        for b2 in range(len(matrizb)):
            somab = matrizb[b2][b1] + somab
        for b2 in range(len(matrizc)):
            somac = matrizc[b2][b1] + somac
    somaa = somaa / len(matriza)
    somab = somab / len(matrizb)
    somac = somac / len(matrizc)
    matrizafinal.append(round(somaa,2))
    matrizbfinal.append(round(somab,2))
    matrizcfinal.append(round(somac,2))
print("Tabela de Pais Lider em cada tipo de sangue e valor percentual")
print('''
________________________________________________________________________
:País\tTO+\tTA+\tTB+\tAB+\tTO-\tTA-\tTB-\tAB-\t|
:{}\t{}\t\t\t\t\t\t\t\t|
:{}\t{}\t\t\t\t\t\t\t|
:{}\t\t{}\t{}\t\t\t\t\t|
:{}\t\t\t\t\t{}\t{}\t\t\t|
:{}\t\t\t\t\t\t{}\t\t|
:{}\t\t\t\t\t\t\t{}\t|
________________________________________________________________________|\n
'''.format(tabelaprint[0],tabelaprint[1],tabelaprint[2],tabelaprint[3],tabelaprint[4],tabelaprint[5],tabelaprint[6],tabelaprint[7],tabelaprint[8],tabelaprint[9],tabelaprint[10],tabelaprint[11],tabelaprint[12],tabelaprint[13]))
print("media de cada tipo de sangue por paises, divididos pela sua letra inicial")

print('''
____________________________________________________________________________
:Grupo de Países\tTO+\tTA+   TB+    AB+   TO-  TA-   TB-  AB-      |     
A\t\t\t{}   |
B\t\t\t{} |
C\t\t\t{}   |
____________________________________________________________________________|
'''.format(matrizafinal,matrizbfinal,matrizcfinal))
poptop = 0
paistop = ''
paismenor = ''
listapop = []
entry = 0
print('paises com maior população em ordem crescente!\n')
for c1 in range(len(DADOS)):
    popmenor = 1388251023
    for c2 in range(len(DADOS)):

        if poptop < DADOS[c2][1]:
            poptop = DADOS[c2][1]
            paistop = DADOS[c2][0]
        elif poptop > DADOS[c2][1]:
            entry = DADOS[c2][1]
            paisentry = DADOS[c2][0]
            if popmenor > entry and paisentry not in listapop:
                paisprint = DADOS[c2][0]
                popmenor = entry
    listapop.append(paisprint)
    print(paisprint)
print(paistop)