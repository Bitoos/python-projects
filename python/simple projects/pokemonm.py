from random import randint
nome = input("qual o seu nome?")
while len(nome) == 0:
    print("voce não preencheu o nome") 
    nome = input("qual o seu nome?")

print("Bem vindo",nome," a arena pokemon\n aqui temos os seguintes pokemons para a sua escolha\n(1)<charmander>\n(2)<bulbasauro>\n(3)<squirtle>")
pokeescolhido = (int(input("escolha o numero do seu pokemon para a batalha ")))
inimigo = randint(1,3)

charmander = 1
bulbasauro = 2
squirtle = 3 
if pokeescolhido == 1:
    print("o escolhido é charmander") 
    if inimigo == 1:
        print("e ele batalhará contra um charmander, empate!!!""")
    elif inimigo == 2:
        print("e ele batalhará contra um bulbasauro, o seu pokemon derrotou o bulbasauro!!")
    elif inimigo == 3:
        print("e ele batalhará contra um squirtle, o seu pokemon perdeu!!!")
elif pokeescolhido == 2:
    print("o escolhido é o bulbasauro")
    if inimigo == 1:
        print("e ele batalhará contra um charmander, o seu pokemon perdeu!!!""")
    elif inimigo == 2:
        print("e ele batalhará contra um bulbasauro, empate!!")
    elif inimigo == 3:
        print("e ele batalhará contra um squirtle, o seu pokemon derrotou o squirtle!!!")
    
elif pokeescolhido == 3:
    print("o escolhido é o squirtle") 
    if inimigo == 1:
        print("e ele batalhará contra um charmander, o seu pokemon derrotou o charmander!!!""")
    elif inimigo == 2:
        print("e ele batalhará contra um bulbasauro, o seu pokemon perdeu!!")
    elif inimigo == 3:
        print("e ele batalhará contra um squirtle, empate!!!")
else:
    print("pokemon invalido!!")
    exit()







