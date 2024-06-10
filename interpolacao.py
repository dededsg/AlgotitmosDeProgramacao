carro = 'civic'
ano = 1994
preco = 150000.0

# interpolação de texto

print("Carro: " + carro + ", Preço:" + str(preco))

# forma antiga de interpolação
print("Carro:  %s, ano: %d, preço: %f" % (carro, ano, preco))

print("Carro: {0}, ano:{1}, preço: {2}".format(carro, ano, preco))

print(f'Carro: {carro}, ano: {ano}, preço: {preco}')

print("Carro: ",carro,"ano: ",ano,"preço: ",preco)