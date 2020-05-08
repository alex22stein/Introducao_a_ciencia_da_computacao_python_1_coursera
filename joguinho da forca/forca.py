import string
import secrets
import numpy as np

palavras = ['arroz', 'orelha', 'estojo', 'teclado', 'fone', 'tablet', 'livro', 'jornal', 'carteira', 'pedra']

palavra = np.random.choice(palavras)
letras = list(palavra)
certas = []
lcertas = []
erradas = []
lerradas = []
for i in letras:
    certas.append("_")
print(palavra)

print('!-----------!')
print('            !')                       
print('            !')   
print('            !')   
print('          ----')   

print('palavra:' + '_\n '*len(palavra))

print('letras erradas:')

print('letras certas:')



for t in range(1000):

    x = input('chuta uma letra: ')
    if  x in letras:
        print('palavra:') 
        for i in range(len(letras)):
            if letras[i] == x:
                certas[i] = x
                lcertas.append(x)
                print(certas[i])
            else:
                print(certas[i])
        
        
        print('letras certas:' + str(lcertas))
        print('letras erradas:' + str(lerradas))


    else:
        print('palavra:') 
        for i in range(len(letras)):
            if letras[i] == x:
                certas[i] = x
                lcertas.append(x)
                print(certas[i])
            else:
                
                print('_ ')
        lerradas.append(x)
        print('letras certas:' + str(lcertas))
        print('letras erradas:' + str(lerradas))

    if len(lerradas) == 0:
        print(' !----------!')
        print('            !')                       
        print('            !')   
        print('            !')   
        print('          ----')  

    if len(lerradas) == 1:
        print(' !----------!')
        print(' o          !')                       
        print('            !')   
        print('            !')   
        print('          ----') 

    if len(lerradas) == 2:
        print(' !----------!')
        print(' o          !')                       
        print(' I          !')   
        print('            !')   
        print('          ----') 

    if len(lerradas) == 3:
        print(' !----------!')
        print(' o          !')                       
        print('/I          !')   
        print('            !')   
        print('          ----') 

    if len(lerradas) == 4:
        print(' !----------!')
        print(' o          !')                       
        print('/I\         !')   
        print('            !')   
        print('          ----') 
 
    if len(lerradas) == 5:
        print(' !----------!')
        print(' o          !')                       
        print('/I\         !')   
        print('/           !')   
        print('          ----') 

    if len(lerradas) == 6:
        print(' !----------!')
        print(' o          !')                       
        print('/I\         !')   
        print('/ \         !')   
        print('          ----') 
        print('GAME OVER!') 
        break
        end


    if certas == letras:
        print('Parabéns!') 
        break   
        end






