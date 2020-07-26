import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    diferenca = 0
    i = 0
    while i < len(as_a):
        diferenca = diferenca + abs(as_a[i] - as_b[i])
        i = i + 1
    return (diferenca/6)


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    soma = 0 
    soma2 = 0 
    soma3 = 0
    #sentenças
    texto_sent = []
    #frases
    texto_fr_sent = []
    #palavras
    texto_pal_fr_sent = []
    #nª palavras diferentes
    texto_paldif = 0
    #nª palavras iguais
    texto_palig = 0
    #começo codigos
    texto_sent = separa_sentencas(texto)
    for i in texto_sent:
        texto_fr_sent = texto_fr_sent + separa_frases(i)
    for i in texto_fr_sent:
        texto_pal_fr_sent = texto_pal_fr_sent + separa_palavras(i)
    texto_paldif = n_palavras_diferentes(texto_pal_fr_sent)
    texto_palig= n_palavras_unicas(texto_pal_fr_sent)
    #caracteres por palavra (soma) > wal
    for i in texto_pal_fr_sent:
        soma = soma + len(i)
    wal = soma/len(texto_pal_fr_sent)
    #caracteres por sentença (soma2) > sal
    for i in texto_sent:
        soma2 = soma2 + len(i)
    ttr= texto_paldif/len(texto_pal_fr_sent)
    hlr = texto_palig/len(texto_pal_fr_sent)
    sal = soma2/len(texto_sent)
    sac = len(texto_fr_sent)/len(texto_sent)
    for i in texto_fr_sent:
        soma3 = soma3 + len(i)
    pal = soma3/len(texto_fr_sent)
    '''print('wal: ',wal)      
    print('ttr: ',ttr)
    print('hlr: ',hlr)
    print('sal: ',sal)
    print('sac: ',sac)
    print('pal: ',pal)'''
    assinatura = [wal,ttr,hlr,sal,sac,pal]
    return assinatura




def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    difassinaturas = []
    for i in textos:
        x = calcula_assinatura(i)
        assinaturas.append(x)
    for i in assinaturas:
        x = compara_assinatura(i, ass_cp)
        difassinaturas.append(x)
    menor = (difassinaturas.index(min(difassinaturas))+1)
    return menor



texto = 'Lorem ipsum dolor sit amet consectetur adipiscing elit nam, pulvinar morbi nostra fusce fermentum nullam in scelerisque sollicitudin, iaculis cursus integer suscipit nec vivamus sed. Litora cursus aliquam velit consectetur venenatis sociosqu finibus, ex malesuada urna vulputate scelerisque phasellus risus, lectus gravida curabitur orci tristique aliquet. Lacinia consequat metus maecenas non himenaeos integer habitant tempus amet, proin justo lorem nisl augue nunc primis inceptos, mus phasellus elit rutrum dis aliquet interdum eleifend. Est facilisis amet venenatis fermentum ullamcorper cras feugiat hac efficitur, aenean leo vehicula ad sapien sagittis finibus mattis, platea suspendisse auctor sodales gravida fames eros fringilla. Penatibus magnis laoreet dignissim consequat nec adipiscing cursus elementum ornare imperdiet, elit nam libero sem quisque massa ligula nibh. Amet in consectetur nibh pharetra habitant curabitur eleifend odio adipiscing, tincidunt sodales magna netus iaculis eu vivamus. Elementum tristique at congue cras magna proin nibh interdum vitae, curae varius id placerat vestibulum iaculis consectetur risus, sociosqu taciti magnis eget velit viverra urna aptent'

ass_cp = le_assinatura()
textos = le_textos()
menor = avalia_textos(textos, ass_cp)
print('O autor do texto ', menor,' está infectado com COH-PIAH')

