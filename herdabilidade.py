def calc_herdabilidade(table):
    # Total GERAL
    G = 0

    # R numero de reprodutores
    r = len(table)

    # K numero de filhos por reprodutor
    k = len(table['A'])

    # Total de elementos
    N = r * k

    soma_quadrados = 0
    # Somamos os elementos das tabela
    for i in table:
        for j in table[i]:
            G += j
            soma_quadrados += (j * j)


    # Fator de correção
    C = (G * G) / (r * k)
    SQtotal = soma_quadrados - C

    print('G é o total geral')    
    print(f'G = {G}')
    print(f'r = {r}\nk = {k}')
    print(f'C = ({G} * {G}) / ({r} * {k}) = {C}')
    print(f'SQTotal => {soma_quadrados} - {C} = {SQtotal}\n')

    SQRep = 0

    soma_linha = 0

    for i in table:
        # quadrado das somas dos reprodutores
        soma_linha += pow(sum(table[i]), 2) 
        print(f'soma dos quadrados do reprodutor {i} = {sum(table[i])}² = {pow(sum(table[i]), 2)}')

    # Soma dos quadrados dos reprodutores
    SQRep = ((1 / k) * soma_linha) - C

    # Sqe soma do quadrado do erro
    SQE = SQtotal - SQRep

    # Quadrado medio dos reprodutores
    QMR = SQRep / (r - 1)

    # Quadrado medio do erro
    QME = SQE / (N - r)

    # estimar componentes da variancia
    sigmaE = QME
    sigmaR = (QMR - QME) / k

    # herdabilidade
    herdabilidade = (4 * sigmaR) / (sigmaR + sigmaE) 


    print(f'\nSQRep = 1/{k} * {soma_linha} - {C} = {SQRep}')
    print(f'SQE = {SQtotal} - {SQRep} = {SQE}')
    print(f'QMR = {SQRep} / ({r} - 1) = {QMR}')
    print(f'QME = {SQE} / ({N} - {r}) = {QME}')
    print(f'sigmaE = QME = {sigmaE}')
    print(f'sigmaR = (QMR - QME) / k = {sigmaR}')
    print(f'\nh² = (4 * {sigmaR}) / ({sigmaR} + {sigmaE}) = {herdabilidade}')
    print(f'herdabilidade = {herdabilidade}')