import random as rdn
mesa_sinuca={
    1:{'cor','Amarelo','surperfice','lisa'},
    2:{'cor','Azul','surperfice','lisa'},
    3,{'cor','vermelho','surperfice','lisa'},
    '4',{'cor','Roxo','surperfice','lisa'},
    '5',{'cor','Laranja','surperfice','lisa'},
    '6',{'cor','Verde','surperfice','lisa'},
    '7',{'cor','Marrom','surperfice','lisa'},
    '8',{'cor','Preto','surperfice','lisa'},
    '9',{'cor','Amarelo','surperfice','listrada'},
    '10',{'cor','Azul','surperfice','listrada'},
    '11',{'cor','Vermelho','surperfice','listrada'},
    '12',{'cor','Roxo','surperfice','listrada'},
    '13',{'cor','Laranja','surperfice','listrada'},
    '14',{'cor','Verde','surperfice','listrada'},
    '15',{'cor','Marrom','surperfice','listrada'}
}

escolhido = rdn.shuffle(list(mesa_sinuca))

print(escolhido)
