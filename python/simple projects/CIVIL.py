matriz = [['1413','212','0','2035','0','9718','7485','28','2989'],
['1689','422','1243','1583','108','10808','7962','14','2351'],
['250','0','957','1874','55','9569','8612','28','2922'],
['266','114','0','228','0','932','670','28','4585'],
['1548','1834','0','1933','91','10474','6967','28','1829'],
['255','0','0','192','0','8898','945','90','2186'],
['1668','2502','0','2035','0','9756','6926','7','1575'],
['2514','0','1183','1885','64','10284','7577','56','3664'],
['296','0','0','192','0','1085','765','28','2165'],
['155','184','143','194','9','880','699','28','2899'],
['1518','1781','1387','1675','183','944','6946','28','3635'],
['173','116','0','192','0','9468','8568','3','694'],
['385','0','0','186','0','966','763','14','2792'],
['2375','2375','0','228','0','932','594','7','2626'],
['167','187','195','185','7','898','636','28','2389'],
['2138','981','245','1817','67','1066','7855','100','4997'],
['2375','2375','0','228','0','932','594','28','3008'],
['336','0','0','182','3','986','817','28','4486'],
['1907','0','1254','1621','78','1090','804','3','1504'],
['3127','0','0','1781','8','9997','8222','28','251'],
['2297','0','1182','1952','61','10281','7576','3','1336'],
['228','3421','0','1857','0','9558','6743','7','2192'],
['236','157','0','192','0','9726','7491','7','2042'],
['132','207','161','179','5','867','736','28','333']]
#mpa = i(8)
#idade = (7)
#superplastico = i(4)
#agua = i(3)
MaiorMPA = int(matriz[0][8])
idadeMPA = ''
for i in range(len(matriz)):
    if MaiorMPA <= int(matriz[i][8]):
        idadeMPA = int(matriz[i][7])
        MaiorMPA = int(matriz[i][8])
    else:
        ()
#print(idadeMPA,MaiorMPA)
print('A Mistura que tem o maior valor de MPA possui {} dias de Idade'.format(idadeMPA))
#-------------------------------------
mediaSuper = 0
contador = 0
for i in range(len(matriz)):
    if int(matriz[i][7]) >= 20 and int(matriz[i][7]) <=30:
        mediaSuper = mediaSuper + int(matriz[i][4])
        contador = contador + 1

mediaSuper = mediaSuper/contador
print('A media do super plastico usado em misturas entre 20 e 30 dias de idade é de {}kg/m3'.format(round(mediaSuper)))
#-------------------------------------
aguaMedia= 0
aguaSoma = 0
for i in range(len(matriz)):
    aguaSoma = aguaSoma + int(matriz[i][3])
    final = i + 1
aguaMedia = aguaSoma / final
#print(aguaMedia)
aguaVariante = 0
VarianteSoma = 0
for i in range(len(matriz)):
    aguaVariante = aguaMedia - int(matriz[i][3])
    if aguaVariante < 0:
        aguaVariante = aguaVariante*-1
        #print(aguaVariante)
    else:
        ()
    #print(aguaVariante)
    aguaVariante = aguaVariante**2
    #print(aguaVariante)
    VarianteSoma = aguaVariante + VarianteSoma
aguaVariante = VarianteSoma / final
print('A variancia nas quantidades de agua usadas nas misturas é de {}'.format(round(aguaVariante)))

