# Algoritmo para inclusão de membros em grupo, cada membro poderá
# participar de apenas um grupo.
# O objetivo da atividade será implementar a opção 5 do menu, a qual
# consiste em verificar se há membros em mais de um grupo, caso isso
# ocorra, o conflito deverá ser resolvido excluindo o membro de um
# dos grupos (a escolha dever ser feito via menu!).
conj_1 = set()
conj_2 = set()
conj_3 = set()
lista_conj = ["Grupo A", "Grupo B", "Grupo C"]
nome = "sem"
grupo = 100
while grupo != 0:
 print("V- Escolha número da opção...")
 print("0- Sair")
 print("1- Grupo A")
 print("2- Grupo B")
 print("3- Grupo C")
 print("4- Imprimir Membros")
 print("5- Verificar grupos")
 grupo = int(input(">>"))
 if grupo in range(1, 4):
  nome = input("Nome do membro do grupo: ")
 if grupo == 1:
  conj_1.add(nome)
 elif grupo == 2:
  conj_2.add(nome)
 elif grupo == 3:
  conj_3.add(nome)
 if grupo == 4:
  for i in range(1, 4):
   print(lista_conj[i - 1])
  for m in eval("conj_{0}".format(i)):
   print(m)
  if grupo == 5:
   print("...")
  else:
   print("Bye!")