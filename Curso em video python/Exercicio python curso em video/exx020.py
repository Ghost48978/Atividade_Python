import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

ordem = random.shuffle(alunos)

print("1. " + alunos[0])
print("2. " + alunos[1])
print("3. " + alunos[2])
print("4. " + alunos[3])