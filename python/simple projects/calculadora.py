import math 

print("escolha uma opção de operação para que seja calculada")
print("""as opções de operações são:
<1> sen (x)
<2> cos(x)
<3> tg(x)
<4> cossec(x)
<5> sec(x)
<6> cotg(x)
<0> Sair do programa
""")

opcao = int(input("escolha o numero da operação"))


if opcao == 0:
  print("Finalizando o programa.")
elif opcao == 1:
  batata = int(input("insira o Valor do Seno a ser calculada:"))
  print("o seno de", batata, "é", math.sin(batata))
elif opcao == 2:
  batata = int(input("insira o valor do Cosseno a ser calculada:"))
  print("o cosseno de", batata, "é " , math.cos(batata))
elif opcao == 3:
  batata = int(input("insira o valor da Tangente a ser calculada:"))
  print("a tangente de", batata , "é", math.tan(batata))
elif opcao == 4:
 batata = int(input("insira o valor da Cossecante a ser calculada:"))
 print("a cossecante de", batata, "é", math.cosh(batata))
elif opcao == 5:
  batata = int(input("insira o valor da Secante a ser calculada:"))
  print("a secante de", batata , "é", math.sinh(batata))
elif opcao == 6:
 batata = int(input("insira o valor da Cotangente a ser calculada:"))
 print("o valor da cotangente de", batata , "é", math.cosh(batata))