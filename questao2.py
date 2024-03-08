valorBuscar = int(input("Digite um número: "))
sequencia = [0,1]

for x in range(15):
    soma = sequencia[-1] + sequencia[-2]
    sequencia.append(soma)
print(sequencia)
    
if valorBuscar in sequencia:
    print("O número digitado pertence a sequência de Fibonacci")
else:
    print("O número digitado não pertence a sequência de Fibonacci")


