num = int(input("Qual é o que numero voce deseja realizar a tabuada? "))
comeco = int(input("Onde você quer que comece? "))
fim  = int(input("Onde você quer que termine? "))
# num = 2
# comeco = 2
# fim = 20

sequencia = range( comeco, fim  +1,)
for intem in sequencia:
    tabuada = num * intem
    print(f"{num} x {intem} = {tabuada}")