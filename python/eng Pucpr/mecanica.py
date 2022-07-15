dados = []
dados = []
arquivo=open('mecanica.txt','r')
LINHA = []
celula = ''
for linhas in arquivo:
    for individual in range(len(linhas)):
        if linhas[individual]!=',' and linhas[individual]!="\n":
            celula=celula+linhas[individual]
        elif linhas[individual]==',' or linhas[individual] == '\n':
            LINHA.append(celula)
            celula=''
            continue
    dados.append(LINHA)
    LINHA = []
#marca   combust    asp  porta carroc cavalo rpm cidade estrada preço 
#e1 variaveis
mdaudi=0
mdbmw=0
mddodge=0
mdhonda=0
marca = dados[0][0]
mediamarca = 0
marcapast = []
mediapast = []
contador = 0
#e2 variaveis
marca2 = []
estilo2 = []
cavalo2 = []
batata = 0
#e3 variaveis
diesel = 0
marcadiesel = []
marcadiesel1 = dados[0][0]
contador2 = 0
#só funcionará se a matriz estivesse organizada com o sort na dados[a1][0], para que as marcas fiquem perto das semelhantes
#porém como a matriz já está organizada, eu pulei esse passo.
for a1 in range(len(dados)):
    #a1 = linhas
    for i in range(1):
        #"for" feito para ser quebrado com o continue, e não bugar o resto do codigo
        if dados[a1][2] == marca:
            mediamarca += float(dados[a1][25])
            contador +=1
            continue
        elif dados[a1][2] != marca:
            marcapast.append(marca)
            mediamarca = mediamarca / contador
            contador = 0
            mediapast.append(mediamarca)
            marca = dados[a1][2]
            mediamarca = 0
        if dados[a1][2] == marca:
            mediamarca += float(dados[a1][25])
            contador +=1
            continue
    for i in range(1):
        if float(dados[a1][24]) - float(dados[a1][23]) < 2:
            marca2.append(dados[a1][2])
            estilo2.append(dados[a1][6])
            cavalo2.append(dados[a1][21])
            continue
        else:
            continue
    for i in range(1):
        if marcadiesel1 == dados[a1][2]:
            if dados[a1][3] == 'diesel':
                diesel =+ 1
            contador2 =+1 
        elif marcadiesel1 != dados[a1][2]:
            if diesel != 0:
                diesel = diesel / contador2
                if diesel > 0.5:
                    marcadiesel.append(marcadiesel1)
            marcadiesel1 = dados[a1][0]
            diesel = 0
            contador2 = 0
print('\nespecificação de automoveis\n')
media = mediapast[1]
marcamedia = ''
for i in range(len(marcapast)):
    if mediapast[i] <= media:
        media = mediapast[i]
        marcamedia = marcapast[i]
print('a marca com a menor media de preço entre os veicúlos é a {}, a qual a media é de US${}'.format(marcamedia,media))
print('\n')
print('os carros que apresentam uma media de milhas por galão (estrada-cidade) inferior a 2 são:')
for i in range(len(cavalo2)):
    print(marca2[i],estilo2[i],'com',cavalo2[i],'cavalos de potencia')
print('\nas marcas que utilizam o diesel como principal (ou mais usado) combustível são:')
for i in range(len(marcadiesel)):
    print(marcadiesel[i])
