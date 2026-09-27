excelente=0.0#contadores de opnião#
bom=0.0
ruim=0.0
for i in range(1,51):#entrada com o loop em for,usei o métrica de opniões com números facilitando o trabalho#
    nome=input(f"Seu nome aqui cliente {i} por favor==>")
    idade=float(input("Sua idade aqui por favor==>"))
    opn=float(input("Qual sua opnião sobre o nosso atendimento entre:1 para excelenete,2 para bom ou 3 para ruim?"))
    if opn==1:#estrutura de decisão para o contador, aq apanhei um pouco pois, esqueci de coloca la dentro do loop, ai saía o print tudo errado#
        excelente+=1
    elif opn==2:
        bom+=1
    elif opn==3:
        ruim+=1
    
print(f"Resultado da pesquisa foi de {excelente} excelente e {ruim} ruim.")#Saída#