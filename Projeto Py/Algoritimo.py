conj_1 = set()
conj_2 = set()
conj_3 = set()
lista_conj = ["Grupo A", "Grupo B", "Grupo C"]
nome = "sem"
grupo = 100
while grupo != 0:
    print('V- Escolha número da opção...')
    print ('0 - Sair')
    print ('1 - Grupo A')
    print ('2 - Grupo B')
    print ('3 - Grupo C')
    print ('4 - Imprimir Membros')
    print ('5 - Verificar grupos')
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
        inter_a = conj_1 & conj_2
        inter_b = conj_1 & conj_3
        inter_c = conj_2 & conj_3
        inter_res = conj_1 & conj_2 & conj_3
        if inter_res:
            print('Nome(s) Repetido(s) nos conjuntos A, B e C: ', inter_res)
            res = input('Em qual conjunto o nome deve ficar [A, B ou C]? ')
            if res == 'A':
                conj_2 = conj_2 - conj_1
                conj_3 = conj_3 - conj_1
                print('Feito!')
            elif res == 'B':
                conj_1 = conj_1 - conj_2
                conj_3 = conj_3 - conj_2
                print('Feito!')
            elif res == 'C':
                conj_1 = conj_1 - conj_3
                conj_2 = conj_2 - conj_3
                print('Feito!')
            else:
                print('valor errado')

        if inter_a:
            print('Essas desgraça(s) estão no grupo A e B: ', inter_a)
            a = input('Em qual grupo essa desgraça deve ficar A ou B? ')
            if a ==  'A':
                conj_2 = conj_2 - conj_1
                print('Feito')
            elif a == 'B':
                conj_1 = conj_1 - conj_2
                print('Feito!')
            else:
                print('valor errado')
        if inter_b:
            print('Essas desgraça(s) estão no grupo A e C: ', inter_b)
            b = input('Em qual grupo essa desgraça deve ficar A ou C?')
            if b == 'A':
                conj_3 = conj_3 - conj_1
                print('Feito!')
            elif b == 'C':
                conj_1 = conj_1 - conj_3
                print('Feito!')
            else:
                print('valor errado')
        if inter_c:
            print('Essas desgraça(s) estão no grupo B e C: ', inter_c)
            c = input('Em qual grupo essa desgraça deve ficar B ou C? ')
            if c == 'B':
                conj_3 = conj_3 - conj_2
                print('Feito!')
            elif c == 'C':
                conj_2 = conj_2 - conj_3
                print('Feito!')
            else:
                print('valor errado')
    else:
        print ('Bye!')