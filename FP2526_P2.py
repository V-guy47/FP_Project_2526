ABC = 'ABCÇDEFGHIJLMNOPQRSTUVXZ'

pontuacao = {'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8}

occ = {'A': 14,'B': 3,'C': 4,'Ç': 2,'D': 5,'E': 11,'F': 2,'G': 2,'H': 2,'I': 10,'J': 2,'L': 5,'M': 6,'N': 4,'O': 10,'P': 4,'Q': 1,'R': 6,'S': 8,'T': 5,'U': 7,'V': 2,'X': 1,'Z': 1}


# PARTE 2 DO PROJETO

#### AUXILIARES ######

def gera_numero_aleatorio(estado:int): # Xorshift (Gerador de números)
    """
    Gerador tipo Xorshift que, por permutação bit a bit, transforma números noutros números
    """
    if estado < 0 or not isinstance(estado, int):
        raise ValueError('gera_numero_aleatório: argumentos inválidos')
    estado ^= ( estado << 13 ) & 0xFFFFFFFF
    estado ^= ( estado >> 17 ) & 0xFFFFFFFF
    estado ^= ( estado << 5 ) & 0xFFFFFFFF
    return estado

def permuta_letras(letras, seed):
    n = len(letras)
    for i in range(n-1, 0, -1):
        seed = gera_numero_aleatorio(seed)
        j = seed % (i+1)
        letras[i], letras[j] = letras[j], letras[i]


def implode(n:list): # Transformador de Listas em Strings 
    """
    Função adaptada dos exercícios de FP (LAB06-07) que transforma uma lista de caracteres em string
    """
    cont = 0
    res = ''
    while cont < len(n):
        res = res + str(n[cont])
        cont += 1
    return res

def casa_no_tabuleiro(casa:tuple): #Transforma a casa no tabuleiro num número "listável"
    """
    Recebe um tuplo representando a casa e transforma-a numa casa 'listável'
    """
    casa = [casa[0] - 1, casa[1] - 1]
    return casa

def obtem_sequencia(tab:list, casa:tuple, direcao:str, tamanho:int):
    """
    Recebe um tabuleiro, casa, direcao e tamanho e retorna o conjunto de letras da respetiva casa, com o tamanho e orientação descritos
    """
    res = ''   # O resultado virá sob forma de string
    casa = casa_no_tabuleiro(casa)
    if direcao == 'H':
        for i in range(tamanho):
            res = res + tab[casa[0]][casa[1] + i]
    elif direcao == 'V':
        for i in range(tamanho):
            res = res + tab[casa[0] + i][casa[1]]
    return res

def ordena_letras(let):
    """
    Recebe um conjunto de letras (str, lst ou tuplo) e retorna um tuplo com as letras ordenadas
    """
    res = []
    n = len(let)
    for c in ABC:
        for i in range(n):
            if let[i] == c:
                res += [c,]
    return res


################################################################################################

### TAD CASA
def testa_casa(lin, col):
    """
    Recebe linha e coluna da casa, testa se é casa no tabuleiro, retornando True ou False.
    """
    return lin > 0 and lin <= 15 and col > 0 and col <= 15

def cria_casa(lin, col):
    """
    Recebe linha e coluna da casa. Se or casa do tabuleiro, retorna a própria casa. Senão, levanta ValueError
    """
    if testa_casa(lin, col):
        return (lin,col)
    else:
        raise ValueError('cria_casa: argumentos inválidos')
    
def obtem_col(c):
    """
    Recebe a casa e retorna a coluna respetiva
    """
    return c[1]

def obtem_lin(c):
    """
    Recebe a casa e retorna a linha respetiva
    """
    return c[0]

def eh_casa(arg):
    """
    Retorna True se o argumento for do tipo casa e False em caso contrário.
    """
    return (isinstance(arg, tuple) or isinstance(arg, list)) and len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int) and 0 < arg[0] <= 15 and 0 < arg[1] <= 15
        
    
def casas_iguais(c1, c2):
    """
    Retorna True se as duas casas atribuídas forem iguais e False em caso contrário.
    """
    return c1 == c2

def casa_para_str(c):
    """
    Transforma a variável casa em tipo string
    """
    casa = str(c)
    casa = casa.replace(" ", "")
    return casa

def str_para_casa(s:str):
    """
    Transforma a string casa em tuplo.
    """
    s = s.strip('()').split(',')
    s[0] = int(s[0])
    s[1] = int(s[1]) 
    s = tuple(s)   
    return s

## TAD ALTO NIVEL
def incrementa_casa(c, d, s):
    """
    Recebe uma casa, uma direção e uma distância e retorna a casa, seguindo essas instruções
    """
    c_copia = ()
    c_copia = c
    c = list(c)
    if not eh_casa(c):
        c = tuple(c)
        return c
    if d == 'H':
        c[1] += s
    if d == 'V':
        c[0] += s
    if eh_casa((c[0], c[1])):
        return tuple(c)
    else:
        return c_copia

#TAD JOGADOR

#Construtores

def cria_humano(nome):
    """
    Recebe um nome e cria um jogador Humano com esse nome.
    """
    if not isinstance(nome, str) or nome == '':
        raise ValueError('cria_humano: argumento inválido')
    jog = {}
    jog['jogador'] = 'jogador'
    jog['id'] = nome
    jog['pontos'] = 0
    jog['letras'] = []
    return jog


def cria_agente(nivel):
    """
    Recebe um nível (FACIL, MEDIO, ou DIFICIL) e retorna um jogador agente com essas características.
    """
    if nivel != 'FACIL' and nivel != 'MEDIO' and nivel != 'DIFICIL':
        raise ValueError('cria_agente: argumento inválido')
    agente = {}
    agente['nivel'] = nivel
    agente['jogador'] = 'agente'
    agente['id'] = f"BOT({nivel})"
    agente['pontos'] = 0
    agente['letras'] = []
    return agente

#Seletores

def jogador_identidade(j):
    """
    Recebe um jogador e devolve o seu nome.
    """
    return j['id']
def jogador_pontos(j):
    """
    Recebe um jogador e devolve a sua pontuação.
    """
    return j['pontos']
def jogador_letras(j):
    """
    Recebe um jogador e devolve as suas letras.
    """
    j['letras'] = ordena_letras(j['letras'])
    return ''.join(j['letras'])

#Modificador

def recebe_letra(j, l):
    """
    Modifica o jogador, acrescentando a letra l ao seu conjunto de letras
    """
    j['letras'].append(l)
    return j


def usa_letra(j, l):
    """
    Modifica o jogador, retirando a letra l do seu conjundo de letras
    """
    if l in j['letras']:
        j['letras'].remove(l)
    return j

def soma_pontos(j, p):
    """
    Soma os pontos das letras e devolve o jogador.
    """
    j['pontos'] += p
    return j

#Reconhecedor

def eh_jogador(arg):
    """
    Retorna True se o argumento for a representação de um jogador. False em caso contrário.
    """
    if not isinstance(arg, str):
        return False
    if 'pontos' not in arg or 'letras' not in arg or 'id' not in arg:
        return False
    elif arg['jogador'] != 'agente':
        return True
    
def eh_humano(arg):
    """
    Retorna True se o argumento for a representação de um jogador Humano. False em caso contrário.
    """
    if 'letras' in arg and 'pontos' in arg:
        if arg['jogador'] != 'agente':
            return True
    elif isinstance(arg, str) and arg[0] != '@':
        return True
    else: 
        return False
    
def eh_agente(arg):
    """
    Retorna True se o argumento for a representação de um jogador Agente. False em caso contrário.
    """
    if 'letras' in arg and 'pontos' in arg:
        if arg['jogador'] == 'agente':
            return True
    else:
        return False
    
def jogadores_iguais(j1, j2):
    """
    Retorna True se os dois jogadores testados forem iguais
    """
    if eh_humano(j1) and eh_humano(j2):
        if j1 == j2:
            return True
        else:
            return False
    elif eh_agente(j1) and eh_agente(j2):
        if j1 == j2:
            return True
        else:
            return False
        
                
def jogador_para_str(t):
    """
    Representação "para os nossos olhos" do jogador dado.
    """
    letras = jogador_letras(t) ## MUDANÇA 
    letras_f = ' '
    for i in range(len(letras)):
        letras_f += letras[i] + ' '
    letras_f = letras_f.rstrip(' ')
    return "{i} ({pontos:>3}):{letras}".format(i = jogador_identidade(t), pontos = jogador_pontos(t), letras = letras_f) # MUDANÇA

## FUNCAO ALTO NIVEL
def distribui_letras(jog, saco:list, num):
    """
    Retira um número máximo de letras do saco e adiciona-as ao conjunto de letras do jogador
    """
    for _ in range(num):
        if saco == []:
            break
        
        jog['letras'].append(saco.pop())
    return jog ## TENHO DE DAR FIX

### TAD VOCABULARIO

#Construtor

def cria_vocabulario(v): ## ORGANIZAR POR LETRA E COMPRIMENTO
    """
    Devolve o vocabulario que contém as palavras no tuplo dado. (Aplicam-se termos e condições)
    """
    if len(v) <= 1:
        raise ValueError('cria_vocabulario: argumento inválido')
    for i in v:
        if len(i) > 15 or len(i) < 2:
            raise ValueError('cria_vocabulario: argumento inválido')
        for j in i:
            if j not in ABC:
                raise ValueError('cria_vocabulario: argumento inválido')
    
    vocab = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[]}
    for i in v:
        vocab[len(i)] += [i,]
    for j in (2, 15):
        vocab[j] = sorted(vocab[j], key= lambda x: tuple(ABC.index(letra) for letra in x))
    return vocab

## Seletores

def obtem_pontos(vocabulario, palavra):
    """
    Recebe o vocabulário e uma palavra e calcula os pontos que essa palavra tem, por soma individual dos pontos das letras.
    """
    res = 0
    if palavra in vocabulario[len(palavra)]:
        for i in palavra:
            res += pontuacao[i]
    return res

def obtem_palavras(vocabulario, comp, letra): ## JA ESTA CERTO
    """
    Recebe um vocabulário, comprimento e letra e calcula, para aquele comprimento, e a começar por aquela letra, calcula a pontuação de todos.
    Devolve um tuplo de tuplos com cada palavra, seguida da sua pontuação.
    """
    res = ()
    vocabulario_OP = vocabulario[comp]
    for i in vocabulario_OP:
        if i[0] == letra:
            pontos = obtem_pontos(vocabulario, i)
            res += ((i, pontos),)
    res_ordenado = sorted(res, key=lambda x: (-x[1], tuple(ABC.index(letra) for letra in x[0])))
    return tuple(res_ordenado)


### Teste

def testa_palavra_padrao(vocabulario, palavra, padrao, letras):
    """
    Recebe vocabulário, palavra, um padrão (sequencia de palavras no tabuleiro) e letras.
    Se for possível adicionar a palavra ao tabuleiro usando as letras para cobrir os espaços em branco, retorna True.
    Falso em contrário.
    """
    if isinstance(letras, str):
        letras_fantasma = []
        for i in letras:
            letras_fantasma += [i,]
    elif isinstance(letras, list):
        letras_fantasma = letras.copy()
    palavra_lista = list(palavra)
    padrao_lista = list(padrao)
    res = []
    if palavra not in vocabulario[len(palavra)]:
        return False
    if len(padrao_lista) != len(palavra_lista):
        return False

        
    for i in range(len(palavra_lista)):
        if padrao_lista[i] == '.':
            if palavra_lista[i] not in letras_fantasma:
                return False
            res.append(palavra_lista[i])
            letras_fantasma.remove(palavra_lista[i])
        elif padrao_lista[i] == palavra_lista[i]:
            res.append(palavra_lista[i])
    res = implode(res)

    return res == palavra



def ficheiro_para_vocabulario(nome_fich):
    """
    Retorna uma lista todas as palavras de um ficheiro que passaram nos filtros de comprimento 
    """
    with open(nome_fich, 'r', encoding='utf-8') as ficheiro_texto:
        conteudo = ficheiro_texto.read()
        conteudo = conteudo.upper()
        conteudo = conteudo.split()
        conteudo_final = []
        for i in range(len(conteudo)):
            palavra_teste = True
            palavra = conteudo[i]
            if len(palavra) > 15 or len(palavra) < 2:
                palavra_teste = False
            for j in palavra:
                if j not in ABC:
                    palavra_teste = False
            if palavra_teste:
                conteudo_final.append(palavra)
    return cria_vocabulario(conteudo_final)



def vocabulario_para_str(vocabulario): 
    """
    Transforma o vocabulário dado em string.
    """
    vocabulario_fantasma = []
    for i in range(2, 15):
        for l in ABC:
            vocabulario_fantasma += obtem_palavras(vocabulario, i, l)
    
    vocab_str = ''
    for j in range(len(vocabulario_fantasma)):
        vocab_str += str(vocabulario_fantasma[j][0]) + '\n' 
    vocab_str = vocab_str.rstrip('\n')
    return vocab_str


### FUNCAO ALTO NIVEL

def procura_palavra_padrao(vocabulario, padrao, letras, min_pontos):
    """
    Procura a palavra no vocabulário que é possível ser formada, com maior pontuação, através do padrao, letras, e que satisfazem o minímo de pontos requisitado.
    """
    palavra_final = ''
    pontos_final = 0
    vocab_ultilizar = []
    casas_padrao = ()
    vocab_teste = vocabulario[len(padrao)]
    if padrao[0] in ABC:

        vocab_teste = list(filter(lambda x: (x[0] == padrao[0]), vocab_teste)) 

    if padrao[0] == '.':
        
        ## VER QUE CASAS TEM PALAVRAS
        for i in range(len(padrao)):
            if padrao[i] in ABC:
                casas_padrao += (i,)
        
        vocab_teste = list(filter(lambda x: all(x[i] == padrao[i] for i in casas_padrao), vocab_teste))

    for j in range(len(vocab_teste)):
        if testa_palavra_padrao(vocabulario, vocab_teste[j], padrao, letras):
            vocab_ultilizar += [vocab_teste[j],]

    if len(vocab_ultilizar) == 1 and obtem_pontos(vocabulario, vocab_ultilizar[0]) >= min_pontos:
        return (vocab_ultilizar[0], obtem_pontos(vocabulario, vocab_ultilizar[0]))
    else:
        for i in vocab_ultilizar:
            ponto_teste = obtem_pontos(vocabulario, i)
            if ponto_teste > min_pontos:
                min_pontos = ponto_teste
                pontos_final = ponto_teste
                palavra_final = i

    return (palavra_final, pontos_final)


######

#TAD TABULEIRO

#CONSTRUTOR

def cria_tabuleiro():
    """
    Cria um tabuleiro em back-end para ser utilizado no jogo.
    """
    tab = []
    line = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    num_linhas = 15 # Constantes tem de ser maiúsculas?
    for i in range(num_linhas):
        newline = line[:]
        tab.append(newline)
    return tab

## SELETOR

def obtem_letra(t,c):
    """
    Obtem a letra correspondente à casa do jogo.
    """
    c = casa_no_tabuleiro(c)
    return t[c[0]][c[1]]

### MODIFICADOR

def insere_letra(t, c, l):
    """
    Insere a letra na casa especificada.
    """
    c = casa_no_tabuleiro(c)
    t[c[0]][c[1]] = l
    return t

def eh_tabuleiro(arg):
    """
    Retorna True se o argumento for do tipo Tabuleiro. False em caso contrário.
    """
    if len(arg) != 15:
        return False
    for i in range(len(arg)):
        if len(arg[i]) != 15:
            return False
    return True

def eh_tabuleiro_vazio(arg):
    """
    Retorna True se o argumento for um tabuleiro vazio. False em caso contrário.
    """
    arg_teste = cria_tabuleiro()
    if arg == arg_teste:
        return True
    else:
        return False
    
def tabuleiros_iguais(t1, t2):
    """
    Retorna True se o dois tabuleiros forem iguais. False em caso contrário
    """
    if isinstance(t1, list) and isinstance(t2, list): ## MUDANÇA = TESTEI SE SAO LISTAS
        return t1 == t2
    else:
        return False

def tabuleiro_para_str(t):
    """
    Representação "para os nossos olhos" das listas de listas que representam o tabuleiro.
    """
    N_linhas = 15
    N_colunas = 15
    res = ''
    for i in range(N_linhas + 1):
        if i == 0:
            res +='             '
        dezena = i // 10
        if dezena >= 1 and i != N_linhas:
            res += f'{dezena}'
        if i == N_linhas:
            res += f'{dezena}\n'
            break
        else:
            res +=' '
    res += '   '
    for j in range(1, N_colunas + 1):
        unidade = j % 10
        if unidade == 1 and j == 1:
            res += '  {unidade} '.format(unidade = unidade)
        elif j == N_colunas:
            res += '{unidade}\n'.format(unidade = unidade)
        else:
            res += '{unidade} '.format(unidade = unidade)
    res += '   +-------------------------------+\n'
    for i in range(N_colunas):
        i_str = ' '.join(t[i])
        if i < 9:
            res += ' {a} | '.format(a = i + 1) + i_str + ' |\n'
        else:
            res += '{b} | '.format(b = i + 1) + i_str + ' |\n'
    res += '   +-------------------------------+'
    return res

def obtem_padrao(t, i, f):
    """
    Obtem a sequencia de palavras desde a casa inicial até à casa final (inclusive). 
    """
    res = ''
    if f[1] == i[1]: # VERTICAL
        direcao = 'V'
        tamanho = f[0] - i[0] + 1
    elif f[0] == i[0]: # HORIZONTAL
        direcao = 'H'
        tamanho = f[1] - i[1] + 1
    res = obtem_sequencia(t, i, direcao, tamanho)
    return res

### ALTO NIVEL

def insere_palavra(t, c, d, p):
    """
    Insere a palavra (p) no tabuleiro (t), a começar na casa (c) iniciale prosseguindo na direção (d) desejada.
    """
    casa = casa_no_tabuleiro(c)
    if d == 'H':
        for i in range(len(p)):
            t[casa[0]][casa[1] + i] = p[i]
    elif d == 'V':
        for i in range(len(p)):
            t[casa[0] + i][casa[1]] = p[i]
    return t

def obtem_subpadroes(t, i, f, l):
    """
    Obtém os subpadrões do tabuleiro (t) que podem ser formados entre a casa inicial (i) e a casa final (f) com o comprimento desejado (l).
    """
    if f[1] == i[1]: # VERTICAL
        direcao = 'V'
    elif f[0] == i[0]: # HORIZONTAL
        direcao = 'H'

    padrao_orig = obtem_padrao(t, i, f)
    
    sub_ = []
    pos_ = []

    for p in range(len(padrao_orig)):
        for j in range(len(padrao_orig) + 1, p + 1, -1):
            subpadroes_adicionar = padrao_orig[p:j]
            cont = 0

            for k in subpadroes_adicionar:
                if k == '.':
                    cont += 1
            if cont <= l:   
                if all(w == '.' for w in subpadroes_adicionar):
                    continue
                if '.' not in subpadroes_adicionar:
                    continue
                if (p == 0 and j == len(padrao_orig)) or (p == 0 and j < len(padrao_orig) and padrao_orig[j] == '.') or (p > 0 and j < len(padrao_orig) and padrao_orig[p - 1] == '.' and padrao_orig[j] == '.') or (p > 0 and j == len(padrao_orig) and padrao_orig[p - 1] == '.'):
                    ## FAZER POSICAO INICIAL E ADICIONAR
                    if direcao == 'H':
                        pos_inicial = (i[0], i[1] + p)
                    else:
                        pos_inicial = (i[0] + p, i[1])
                    sub_.append(subpadroes_adicionar)
                    pos_.append(pos_inicial)
                
    return tuple(sub_), tuple(pos_)
        
        
def gera_todos_padroes(t, l): ## EU ACHO QUE ESTE ESTÁ CERTO
    """
    Gera TODOS os padroes e subpadroes que podem ser formados pelo tabuleiro (Horizontal ou Verticalmente), que tenham comprimento máximo desejado (l).
    """

    # VAR (experimentar com tipo de var antes do nome)
    lst_sub_padroes = []
    lst_casas_inicio = []
    lst_direcoes = []
   
    # PARA HORIZONTAL:
    for i in range(len(t)):
        casa_inicial = cria_casa(i + 1, 1)
        casa_final = cria_casa(i + 1, len(t))
        sub_padroes, pos = obtem_subpadroes(t, casa_inicial, casa_final, l)

        if sub_padroes != () and pos != ():
            lst_sub_padroes += sub_padroes
            lst_casas_inicio += pos
            for _ in range(len(sub_padroes)):
                lst_direcoes += 'H'

    # PARA VERTICAL
    for i in range(15): 

        casa_inicial = cria_casa(1, i + 1)
        casa_final = cria_casa(15, i + 1)
        sub_padroes, pos = obtem_subpadroes(t, casa_inicial, casa_final, l)

        if sub_padroes != () and pos != ():
            lst_sub_padroes += sub_padroes
            lst_casas_inicio += pos
            for _ in range(len(sub_padroes)):
                lst_direcoes += 'V'

    return tuple(lst_sub_padroes), tuple(lst_casas_inicio), tuple(lst_direcoes)



### FUNCOES ADICIONAIS ###

def baralha_saco(seed):
    """
    Baralha o saco, consoante o gerador Xorshift e com base na seed imposta.
    """
    res = []
    for i in occ:
        for _ in range(occ[i]):
            res += i 
    permuta_letras(res, seed) # REORGANIZA A LISTA
    return res


def jogada_humano(tab:list, jog:dict, vocab:dict, pilha:list):
    """
    Processa o turno completo da uma jogada HUMANA:
    P - passa o seu turno
    T <seq> - Troca de letras (<seq>) por outras
    J - Jogar 
    """

    
    while True:
        mensagem = str(input('Jogada {player}: '.format(player = jogador_identidade(jog))))
        mensagem = mensagem.split()
        if mensagem == []:
            continue

        if mensagem[0] == 'P': # SE PASSAR A VEZ
            if len(mensagem) == 1:
                return False
            else:
                continue

        elif mensagem[0] == 'T' and len(pilha) >= 7: # TROCAR DE LETRAS
            letras_a_trocar = []

            for i in range(1, len(mensagem)): # buscar as letras 
                letras_a_trocar += [mensagem[i],]

            
            for i in letras_a_trocar: # remover as letras
                jog['letras'].remove(i)

            distribui_letras(jog, pilha, len(mensagem) - 1)
            
            return True
            
        elif mensagem[0] == 'J':
            if len(mensagem) == 5:
                linha_tab = int(mensagem[1])
                col_tab = int(mensagem[2])
                direcao = str(mensagem[3])
                palavra = str(mensagem[4])
            else:

                continue
            cont = 0
            letras_a_remover = []
            casa = cria_casa(linha_tab, col_tab)
            padrao = obtem_sequencia(tab, casa, direcao, len(palavra))

            pode_continuar = eh_casa(casa)
            pode_continuar = eh_humano(jog)

            for i in padrao:
                if i == '.':
                    cont += 1
            if pode_continuar:
                if eh_tabuleiro_vazio(tab):
                    if (direcao == 'H' and ((col_tab <= 8) and col_tab + len(palavra) > 8 and linha_tab == 8)) or (direcao == 'V' and ((linha_tab <= 8) and linha_tab + len(palavra) > 8 and col_tab == 8)):
                        if testa_palavra_padrao(vocab, palavra, padrao, jogador_letras(jog)):
                            tab = insere_palavra(tab, casa, direcao, palavra)
                            jog['pontos'] += obtem_pontos(vocab, palavra)
                            for i in palavra:
                                jog['letras'].remove(i)
                            distribui_letras(jog, pilha, cont)
                            return True
                        else:
                            continue
                    else:
                        continue
                else:
                    if '.' in padrao and any(w in ABC for w in padrao):
                        if testa_palavra_padrao(vocab, palavra, padrao, jogador_letras(jog)):
                            tab = insere_palavra(tab, casa, direcao, palavra)
                            jog['pontos'] += obtem_pontos(vocab, palavra)
                            for i in range(len(padrao)):
                                if padrao[i] == '.' and palavra[i] in ABC:
                                    letras_a_remover.append(palavra[i])
                            for i in letras_a_remover:
                                jog['letras'].remove(i)
                            distribui_letras(jog, pilha, cont)
                            return True
                        else:
                            continue
                    else:
                        continue       

def jogada_agente(tab, jog, vocab, pilha):
    """
    Função que processa o turno completo de um agente.
    Recebe tabuleiro, agente, vocabulário e saco de letras, calcula a melhor palavra a utilizar dependendo do nivel e aplica-a ao tabuleiro.
    """
    while True:
        consegue_jogar = True
        consegue_trocar = True
        ### JOGAR
        if consegue_jogar and not eh_tabuleiro_vazio(tab):
            todos_padroes, casas_iniciais, direcoes = gera_todos_padroes(tab, len(jogador_letras(jog)))
            if jog['nivel'] == 'FACIL':
                N = 100
                alg_padroes = todos_padroes[::N]
                alg_casas_iniciais = casas_iniciais[::N]
                alg_direcoes = direcoes[::N]
            elif jog['nivel'] == 'MEDIO':
                N = 50
                alg_padroes = todos_padroes[::N]
                alg_casas_iniciais = casas_iniciais[::N]
                alg_direcoes = direcoes[::N]
            elif jog['nivel'] == 'DIFICIL':
                N = 10
                alg_padroes = todos_padroes[::N]
                alg_casas_iniciais = casas_iniciais[::N]
                alg_direcoes = direcoes[::N]

            if alg_padroes == ():
                consegue_jogar = False
            else:
                padr_casa_pos_alinhados = []
                padr_pal_pontos_pos_dir = []
                for i in range(len(alg_padroes)):
                    padr_casa_pos_alinhados.append((alg_padroes[i], alg_casas_iniciais[i], alg_direcoes[i]))
            
                for i in range(len(padr_casa_pos_alinhados)):
                    padrao = padr_casa_pos_alinhados[i][0]
                    posicao = padr_casa_pos_alinhados[i][1]
                    direcao = padr_casa_pos_alinhados[i][2]
                    palavra, pontos = procura_palavra_padrao(vocab, padrao, jogador_letras(jog), 0)
                    if palavra == '' or pontos == 0:
                        continue
                    else:
                        padr_pal_pontos_pos_dir.append((padrao, palavra, pontos, posicao, direcao))

                padr_pal_pontos_pos_dir = sorted(padr_pal_pontos_pos_dir, key= lambda x: (-x[2]))
                if padr_pal_pontos_pos_dir == []:
                    consegue_jogar = False
                else:
                    padrao_final = padr_pal_pontos_pos_dir[0][0]
                    palavra_final = padr_pal_pontos_pos_dir[0][1]
                    pontos_final = padr_pal_pontos_pos_dir[0][2]
                    pos_final = padr_pal_pontos_pos_dir[0][3]
                    direcao_final = padr_pal_pontos_pos_dir[0][4]

                    tab = insere_palavra(tab, pos_final, direcao_final, palavra_final)
                    jog['pontos'] += pontos_final

                    letras_a_remover = []
                    cont = 0
                    for i in range(len(padrao_final)):
                        if padrao_final[i] == '.' and palavra_final[i] in ABC:
                            letras_a_remover.append(palavra_final[i])
                            cont += 1
                    for i in letras_a_remover:
                        jog['letras'].remove(i)
            
                    distribui_letras(jog, pilha, cont)

                    print(f"Jogada {jog['nivel']}: J {obtem_lin(pos_final)} {obtem_col(pos_final)} {direcao_final} {palavra_final}")
                    return True
                

### TROCAR            
        if not consegue_jogar and not eh_tabuleiro_vazio(tab): 
            letras = ''
            if len(pilha) >= 7:
                jog['letras'] = ordena_letras(jogador_letras(jog))

                letras_a_adicionar = len(jogador_letras(jog))
                for i in range(letras_a_adicionar):
                    if i > 0:
                        letras += ' '
                    letras += jog['letras'][i]
                jog['letras'] = []
                distribui_letras(jog, pilha, letras_a_adicionar)
                letras = letras.rstrip()
                print(f"Jogada {jog['nivel']}: T {letras}")
                return True
            else:
                consegue_trocar = False
##### PASSAR A VEZ
        if eh_tabuleiro_vazio(tab) or (consegue_jogar == False and consegue_trocar == False):
            print(f"Jogada {jog['nivel']}: P")
            return False




def scrabble2(jogadores, nome_fich, seed):
    """
    Função que permite jogar Scrabble com 2 a 4 jogadores (incluindo computadores)
    """
    if not isinstance(jogadores, tuple) or len(jogadores) < 2 or len(jogadores) > 4:
        raise ValueError('scrabble2: argumentos inválidos')
    if not isinstance(nome_fich, str) or nome_fich == '':
        raise ValueError('scrabble2: argumentos inválidos')
    if not isinstance(seed, int) or seed <= 0:
        raise ValueError('scrabble2: argumentos inválidos')
    
    lista_jogadores = []

    for i in jogadores:
        if not isinstance(i, str):
            raise ValueError('scrabble2: argumentos inválidos')
        
        if i[0] == '@':
            nivel = i[1:]
            if nivel == 'FACIL' or nivel == 'MEDIO' or nivel == 'DIFICIL':
                lista_jogadores += [(cria_agente(nivel)),]
            else: 
                raise ValueError('scrabble2: argumentos inválidos')
        
        if eh_humano(i):
            lista_jogadores += [(cria_humano(i)),]
    
    pilha = baralha_saco(seed)

    for j in lista_jogadores:
        distribui_letras(j, pilha, 7)

    vocabulario = ficheiro_para_vocabulario(nome_fich)
    tab = cria_tabuleiro()
    nao_jogou = 0
    
    print('Bem-vindo ao SCRABBLE2.')

    while True:
        for j in lista_jogadores:
            print(tabuleiro_para_str(tab))
            for i in lista_jogadores:
                print(jogador_para_str(i))
            if eh_humano(j):
            
                jogada = jogada_humano(tab, j, vocabulario, pilha)
                
            if eh_agente(j):
                jogada = jogada_agente(tab, j, vocabulario, pilha)

            if jogada:
                nao_jogou = 0
            if not jogada:
                nao_jogou += 1

            ## COMO TERMINA
            if nao_jogou == len(lista_jogadores) or (pilha == [] and not jogador_letras(j)):
                pontos_finais = []
                for i in lista_jogadores:
                    pontos_finais.append(jogador_pontos(i))
                return tuple(pontos_finais)

print(scrabble2(('JOG1', 'JOG2'), 'vocab25k.txt', 15))
