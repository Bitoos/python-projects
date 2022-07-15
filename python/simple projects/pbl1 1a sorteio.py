troco = 8.65


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
real005 = troco4 // 0.05
 
print(real1, real05, real01, real005)
print(troco, troco2, troco3, troco4)
exit()
troco = 8.75

moeda1 = troco // 1     #m1 é 8.00
troco2 = troco - moeda1 #fexo  troco é 0.75

moeda05 = troco2 // 0.50   #m2 é 1.00
troco3 = moeda05 * 0.50 - troco2

moeda01 = troco3 // 0.1
troco4 = moeda01 * 0.1 - troco3

moeda005 = troco4 //0.05











print(moeda1 ,moeda05 ,moeda01 ,moeda005)
print(troco, troco2, troco3, troco4)