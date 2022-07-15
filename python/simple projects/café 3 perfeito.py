print("""Seja bem vindo a maquina de café P.UDIM
temos os seguintes produtos a disposição
<tipo de café>       <Nº>      <preço>
Café normal            1       R$ 2.50
Café expresso          2       R$ 2.75
Capuccino              3       R$ 3.50
Mocaccino              4       R$ 3.25

Digite abaixo o Nº do café desejado
""")

cafe = int(input("numero do café:"))

if cafe == 1:
    valor = int(input("coloque uma nota inteira na maquina com o valor do café desejado, não aceitamos moedas:"))
    if valor < 2.50:
        print("valor abaixo do necessario para o café, a maquina reiniciará e seu dinheiro será estornado")
        exit()
    elif valor == 2.50:
        print("Muito obrigado pela preferencia, o seu café está sendo servido")
    elif valor > 2.50:
        troco = valor - 2.50
        print("Muito obrigado pela preferencia, o seu café normal está sendo servido e há um valor de R$",troco, "em haver, que será pago imediatamente.")

if cafe == 2:
    valor = int(input("coloque uma nota inteira na maquina com o valor do café desejado, não aceitamos moedas:"))
    if valor < 2.75:
        print("valor abaixo do necessario para o café, a maquina reiniciará e seu dinheiro será estornado")
        exit()
    elif valor == 2.75:
        print("Muito obrigado pela preferencia, o seu café expresso está sendo servido")
    elif valor > 2.75:
        troco = valor - 2.75
        print("Muito obrigado pela preferencia, o seu café expresso está sendo servido e há um valor de R$",troco, "em haver, que será pago imediatamente.")

if cafe == 3:

    valor = int(input("coloque uma nota inteira na maquina com o valor do café desejado, não aceitamos moedas:"))
    if valor < 3.50:
        print("valor abaixo do necessario para o Capuccino, a maquina reiniciará e seu dinheiro será estornado")
        exit()
    elif valor == 3.50:
        print("Muito obrigado pela preferencia, o seu Capuccino está sendo servido")
    elif valor > 3.50:
        troco = valor - 3.50
        print("Muito obrigado pela preferencia, o seu Capuccino está sendo servido e há um valor de R$",troco, "em haver, que será pago imediatamente.")

if cafe == 4:
    valor = int(input("coloque uma nota inteira na maquina com o valor do café desejado, não aceitamos moedas:"))
    if valor < 3.25:
        print("valor abaixo do necessario para o Mocaccino, a maquina reiniciará e seu dinheiro será estornado")
        exit()
    elif valor == 3.25:
        print("Muito obrigado pela preferencia, o seu Mocaccino está sendo servido")
    elif valor > 3.25:
        troco = valor - 3.25
        print("Muito obrigado pela preferencia, o seu Mocaccino está sendo servido e há um valor de R$",troco, "em haver, que será pago imediatamente.")
elif cafe ==0:
    print("comando invalido, programa finalizado.")
    exit()
elif cafe >=5:
    print("comando invalido, programa finalizado")
    exit()

real1 = troco // 1   #ex: 8.65 // 1 = 8 moedas de 1 real
real1 #quantidade de moeda de 1 real
troco2 = troco % 1 #é o que sobrou do 1  ex: 8.65 // 1 = 0.65
real05 = troco2 // 0.5 # 0.65 // 0.5 = 1 moeda de 0.50
real05 #quantidades de moedas de 0.50
troco3 = troco2 % 0.5 
troco3  #resto da do troco, 0.65 % 0.50 = 0.15
real01 = troco3 // 0.1 #ex: 0.15 // 0.10 = 1
real01 #quantidade de moedas de 0.10
troco4 = troco3 % 0.1 #resto
real005 = troco4 // 0.048

print(""" sairam as seguintes moedas no fundo da maquina""")
print(real1, """moedas de 1 real""")
print(real05, """moedas de 50 centavos""")
print(real01, """moedas de 10 centavos""")
print(real005, """moedas de 5 centavos""")
exit()