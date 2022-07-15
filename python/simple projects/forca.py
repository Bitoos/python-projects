
palavra = []
palavra = ('g','e','l','a','d','e','i','r','a')
lista = []
erros = 0
g = ('_')
e = ('_')
l = ('_')
a = ('_')
d = ('_')
i = ('_')
r = ('_')

print("bem vindo ao jogo de forca, você deve inserir uma letra para tentar adivinhar a palavra secreta.\n voce pode errar somente 3 vezes")
letra = input("qual a letra? ")

while erros < 3:
    if letra in lista:
        print("essa letra já foi escolhida, foi adicionado mais um erro para o contador")
        erros +=1 
    elif letra in palavra:
        print("essa letra está correta!\n")
    elif letra not in palavra:
        erros +=1 
        print("essa letra está incorreta, você errou {} vez.\n".format(erros))
    elif letra in lista:
        print("essa letra já foi escolhida, foi adicionado mais um erro para o contador\n")
        erros +=1 


    lista.append(letra)
    if letra in palavra:
        if letra == ('g'):
            g = ('g')
        if letra == ('e'):
            e = ('e')
        if letra == ('l'):
            l = ('l')
        if letra == ('a'):
            a = ('a')
        if letra == ('d'):
            d = ('d')
        if letra == ('i'):
            i = ('i')
        if letra == ('r'):
            r = ('r')
        
        
    print("a palavra até agora é {} {} {} {} {} {} {} {} {}".format(g,e,l,a,d,e,i,r,a))
    print("a(s) letras escolhidas até agora são {}.\n".format(lista))

    if g and e and l and a and d and i and r in lista:
        print("voce acertou a palavra!!! é G E L A D E I R A..\n Parabéns!!!!")
        exit()
    letra = input("qual é a proxima letra desejada?")

    

if erros >= 3:
    print("você errou muitas vezes, o programa será fechado!!")
    exit()


