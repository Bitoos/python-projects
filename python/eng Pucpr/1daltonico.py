#esse programa eu fiz para ajudar um amigo, e tive que fazer meio "quebrado (exesso de if)" para poder passar, pois senão ficaria obvio que não era ele que havia feito
f = open('arquivo.txt','r')
i = 0
cont = 0
primaria = []
matriz = []
cont = 0
numero = ''
for i in f:
    cont = cont + 1
    for e in range(len(i)):
        
        if i[e] != ',':
            numero = numero + i[e]
        elif i[e] == ',':
            primaria.append(numero)
            numero = ''
        if e == len(i) - 1:
            numero = numero[0]
            primaria.append(numero)
            numero = ''
    matriz.append(primaria)
    primaria = []
#len de f = cont
# exemplo : 173,1.51321,13.00,0.00,3.02,70.70,6.21,6.93,0.00,0.00,5
#e1
Informacao = matriz
identificacao = ''
MaiorCalcio = 0
for calcio in range(len(Informacao)):
    if float(Informacao[calcio][7]) >= MaiorCalcio:
        MaiorCalcio = float(Informacao[calcio][7])
        identificacao = Informacao[calcio][0]
    else:
        ()
#e1
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
cont7=0
med1=0
med2=0
med3=0
med4=0
med5=0
med6=0
med7=0
contmed1 = 0
contmed2 = 0
contmed3 = 0
contmed4 = 0
contmed5 = 0
contmed6 = 0
contmed7 = 0
for coluna in range(len(Informacao)):
    if Informacao[coluna][10] == '1':
        cont1 = cont1 + 1
        med1 = med1 + float(Informacao[coluna][5])
        contmed1 = contmed1 + 1
    elif Informacao[coluna][10] =='2':
        cont2 = cont2 + 1
        med2 = med2 + float(Informacao[coluna][5])
        contmed2 = contmed2 + 1
    elif Informacao[coluna][10] =='3':
        cont3 = cont3 + 1
        med3 = med3 + float(Informacao[coluna][5])
        contmed3 = contmed3 + 1
    elif Informacao[coluna][10] =='4':
        cont4 = cont4 + 1
        med4 = med4 + float(Informacao[coluna][5])
        contmed4 = contmed4 + 1
    elif Informacao[coluna][10] =='5':
        cont5 = cont5 + 1
        med5 = med5 + float(Informacao[coluna][5])
        contmed5 = contmed5 + 1
    elif Informacao[coluna][10] =='6':
        cont6 = cont6 + 1
        med6 = med6 + float(Informacao[coluna][5])
        contmed6 = contmed6 + 1
    elif Informacao[coluna][10] =='7':
        cont7 = cont7 + 1
        med7 = med7 + float(Informacao[coluna][5])
        contmed7 = contmed7 + 1
#e2
if med1 != 0:
    med1 = med1/cont1
    med1 = round(med1,2)
    med1 = str(med1)
if med2 != 0:
    med2 = med2/cont2
    med2 = round(med2,2)
    med2 = str(med2)
if med3 != 0:
    med3 = med3/cont3
    med3 = round(med3,2)
    med3 = str(med3)
if med4 != 0:
    med4 = med4/cont4
    med4 = round(med4,2)
    med4 = str(med4)
if med5 != 0:
    med5 = med5/cont5
    med5 = round(med5,2)
    med5 = str(med5)
if med6 != 0:
    med6 = med6/cont6
    med6 = round(med6,2)
    med6 = str(med6)
if med7 != 0:
    med7 = med7/cont7
    med7 = round(med7,2)
    med7 = str(med7)
#E2
#e3
refracao = 0
aluminio = ''
for coluna in range(len(Informacao)):
    if float(Informacao[coluna][1]) > refracao:
        refracao = float(Informacao[coluna][1])
        aluminio = Informacao[coluna][4]
    else:
        ()
#e3
#parte 2 estatistica
vidrosparajanelas = contmed1 + contmed2 + contmed3 + contmed4
vidrosfloat = contmed1 + contmed3
naousados = contmed5 + contmed6 + contmed7 
naofloat = contmed2 + contmed4
total = contmed1 + contmed2 + contmed3 + contmed4 + contmed5 + contmed6 + contmed7 + vidrosparajanelas + vidrosfloat+ naousados + naofloat
participacaonaofloat = naofloat / total * 100
participacaoconstnao = contmed2 /total * 100
participacaovfloat = vidrosfloat    /total *100
participacaoconstfloat = contmed1   /total *100
participacaofloatveiculo = contmed3 /total * 100
participacaonaousados = naousados /total * 100
participacaoconteiner = contmed5/total *100 
participacaotableware = contmed6/total*100
participacaofarois = contmed7/total *100
participacaoveinao = contmed4  /total*100
participacaojanelas = vidrosparajanelas/total*100
#estatistica
f.close()
#gerar o arquivo "estatistica.txt"
batata = open('estatistica.txt','w')
batata.write('O vidro que apresenta o maior valor de calcio tem a indicacao pelo numero ')
batata.write(str(identificacao) + '\n\n')
batata.write('o valor medio do silicio em cada tipo de vidro e de: \n')
batata.write('tipo 1: ' + str(med1) + '\n' + 'tipo 2: '+ str(med2) +'\n' + 'tipo 3: ' + str(med3) + '\n' + 'tipo 4: '+ str(med4)+'\n' + 'tipo 5: ' + str(med5) + '\n' + 'tipo 6: '+ str(med6)+'\n'+ 'tipo 7: ' + str(med7)+ '\n\n')
batata.write('o vidro que apresenta o maior indice de refracao, tem ' + str(aluminio)+ ' de aluminio')
batata.write('\n\n\n\n\t\tconjuntos\t\t\t\t\t\t\t\tquantitades\t\tparticipacao\nVidros para janelas (construcoes e veiculos)\t\t' + str(vidrosparajanelas) + '\t\t\t\t' + str(round(participacaojanelas)) + '%\n')
batata.write('Vidros Float para janelas\t\t\t\t\t\t\t' + str(vidrosfloat) + '\t\t\t\t'+ str(round(participacaovfloat)) +'%\nvidros Float para janelas\t\t\t\t\t\t\t' + str(contmed1) + '\t\t\t\t' + str(round(participacaoconstfloat)) + '%\n' )
batata.write('Vidros Float para janelas de veiculos\t\t\t\t'+str(contmed3)+'\t\t\t\t'+str(round(participacaofloatveiculo))+'%\n'+'Vidros nao-float para janelas\t\t\t\t\t\t'+str(naofloat)+'\t\t\t\t'+str(round(participacaonaofloat))+'%\nVidros nao-float para janelas de construcao\t\t\t'+str(contmed2)+'\t\t\t\t'+str(round(participacaoconstnao))+'%')
batata.write('\nVidros nao-Float para veiculos\t\t\t\t\t\t'+str(contmed4)+'\t\t\t\t'+str(round(participacaoveinao))+'%\nVidros nao usados para janelas\t\t\t\t\t\t'+str(naousados)+'\t\t\t\t'+ str(round(participacaonaousados))+'%\nContainers\t\t\t\t\t\t\t\t\t\t\t'+ str(contmed5)+'\t\t\t\t'+str(round(participacaoconteiner))+'%')
batata.write('\nTableware\t\t\t\t\t\t\t\t\t\t\t'+str(contmed6) +'\t\t\t\t'+str(round(participacaotableware))+'%\nFarois\t\t\t\t\t\t\t\t\t\t\t\t'+str(contmed7)+'\t\t\t\t'+str(round(participacaofarois))+'%')
batata.write('\nTOTAL\t\t\t\t\t\t\t\t\t\t\t\t'+str(total)+'\t\t\t\t100%')
batata.close
print('os resultados foram salvos como: estatistica.txt')
