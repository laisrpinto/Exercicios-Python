dias = int(input('Quantos dias vc ficou com o carro?'))
km = float(input('Quantos km vc rodou?'))
preco = (dias*60) + (km*0.15)
print('O total a pagar é de R${:.2f}'.format(preco))