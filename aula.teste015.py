dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodado?'))
pago = (dias * 60) + (km * 0.15)
print ('O tatal a pagar é de R$ {:.2f}'.format(pago))
