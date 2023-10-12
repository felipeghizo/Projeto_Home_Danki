dias = int(input('Quantos dias o carro ficou alugado?' ))
km = float(input('Qual foi a distancia percorrida (em KM) nesse tempo? '))
precodia = 60*dias
preckm = 0.15*km
total = precodia + preckm
print('O preco total a se pagar e {} reais '.format(total))