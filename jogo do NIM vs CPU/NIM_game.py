import sys
def computador_escolhe_jogada(n,m):
    if (n%(m+1))==0:
        n = n - m
        print('Computador tirou ' + str(m))
    else:
        i = m
        while i>0:
            if (n-i)%(m+1)==0:
                n = n - i
                break
            i = i - 1
        print('Computador tirou ' + str(i))
    if n == 0:
        print(n)
        print('Computador ganhou')
        sys.exit(0)
    return n


def usuario_escolhe_jogada(n,m):
    x = input('Sua vez, escolha um numero de 1 até m: ')
    x = int(x)
    while x>n or x>m:
        print('esse número não serve')
        x = input('Escolhe outro: ')
        x = int(x)
    n = n - x
    print('Você tirou ' + str(x))
    if n == 0:
        print('Você ganhou')
        sys.exit(0)
    return n
    
def partida():
    n = input('Escolha o valor de n: ')
    n = int(n)
    m = input('Escolha o valor de m: ')
    m = int(m)
    if n%(m+1)==0:
        print('Usuario começa :)') 
        while n>0:
            n = usuario_escolhe_jogada(n,m)
            print(n)
            ('Vez do computador: ')
            n = computador_escolhe_jogada(n,m)
            print(n)
        print('Acabou')
    else: 
        print('Computador começa :)')
        while n>=1:
            ('Vez do computador: ')
            n = computador_escolhe_jogada(n,m)
            print(n)
            n = usuario_escolhe_jogada(n,m)
            print(n)
        print('Acabou')




