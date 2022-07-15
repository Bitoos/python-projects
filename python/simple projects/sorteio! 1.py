from random import randint 

print("escolha dois numeros para que o sorteio seja feito entre eles")
print("o primeiro numero deve ser menor que o segundo.")


num1 = int(input("insira o primeiro numero: "))
num2 = int(input("insira o segundo numero: "))
if num1 > num2:
  print(num1,"é maior que", num2,".invalido")
  exit()

certo = randint (num1,num2)
print("agora escolha um numero para ser sorteado, entre os numeros escolhidos acima")
sorteio = int(input("numero do sorteio: "))

if sorteio < num1:
  print("numero do sorteio, é menor que o intervalo, programa finalizado")
  exit()
if sorteio > num2:
  print("numero do sorteio maior que o intervalo,programa finalizado.")
  exit()

if sorteio == certo:
  print("Voce foi sorteado!!")
  exit()
elif sorteio != certo:
  if sorteio > certo:
    print("muito alto")
  else:
    print("muito baixo")
  exit()