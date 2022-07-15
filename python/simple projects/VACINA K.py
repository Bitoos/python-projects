ast = 0 #'astrazaneca'
pfi = 0 #'pfizer'
cvc = 0 #'coronavac'
jan = 0 #'jansenn'
n = False
s = True
contador = 0
cqi = []
cqd = []
cqc = []
cqv = []
qtd = 21
dose =   [1,1,1,1,1,2,1,2,2,2,1,1,1,2,1,1,1,2,1,1,1]
idade =  [67,76,19,43,69,42,32,30,32,22,21,78,64,56,57,28,35,53,89,29,17]
como =   [n,n,n,n,s,n,n,n,s,n,n,s,n,n,s,n,n,n,n,s,s]
vacina = ['','','','','','c','','p','a','c','','','','a','','','','a','a','a','a']
while contador < qtd :
    cqi = idade [(int(contador))] 
    cqd = dose  [(int(contador))]
    cqc = como  [(int(contador))]
    cqv = vacina[(int(contador))]
    print(cqi,cqd,cqc,cqv)
    if cqv != '':
        if cqv == 'c':
            cvc = cvc +1
        elif cqv == 'p':
            pfi = pfi +1
        elif cqv == 'a':
            ast = ast +1
        elif cqv == 'j':
            jan = jan +1
    elif cqc is True:
        pfi = pfi + 1
    elif cqi >=60:
        pfi = pfi + 1
    elif cqi >= 18 and cqi <= 30:
        if jan <= cvc:
            jan = jan +1
        elif jan >= cvc:
            cvc = cvc +1
    else:
        jan = jan +1
    contador= contador + 1
print (ast,pfi,cvc,jan)
print (ast + pfi + cvc + jan)
print("o numero de vacinas que a prefeitura terá que comprar é de:\n<{}>Astra Zaneca\n<{}>Pfizer\n<{}>CoronaVac\n<{}>Janssen".format(ast,pfi,cvc,jan))