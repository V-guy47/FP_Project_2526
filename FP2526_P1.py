ABC = 'ABCÇDEFGHIJLMNOPQRSTUVXZ'

###########################################################################
# funções deprecated

def eh_tabuleiro(tab):
    if not isinstance(tab, list) or len(tab) != 15:
        return False
    for l in tab:
        if not isinstance(l, list) or len(l) != 15:
            return False
        for c in l:
            if not isinstance(c, str) or len(c) != 1 or (c != '.' and not c in ABC):
                return False
    return True

def eh_casa(pos):
    if not isinstance(pos, tuple) or len(pos) != 2:
        return False
    for i in range(2):
        if not isinstance(pos[i], int) or pos[i] < 1 or pos[i] > 15:
            return False
    return True

def eh_casa_livre(tab, pos):
    l = tab[pos[0]-1]
    return l[pos[1]-1] == '.'

###########################################################################
# Auxiliares minhas

def eh_conjunto(conj):
    acc = set()
    if not isinstance(conj, dict):
        return False
    for key, value in conj.items():
        if not isinstance(key, str) or len(key) != 1 or key not in ABC or key in acc:
            return False
        if not isinstance(value, int) or value < 1:
            return False
        acc.add(key)
    return True

def insere_letra_conjunto(conj, l):
    if l in conj:
        conj[l] += 1
        return True
    else:
        conj[l] = 1
        return False

def retira_letra_conjunto(conj, l):
    if l in conj:
        if conj[l] == 1:
            del conj[l]
        else:
            conj[l] -= 1
        return True
    return False

def conjunto_para_tuplo(conj):
    res = ()
    for c in ABC:
        if c in conj:
            for _ in range(conj[c]):
                res += (c,)
    return res

def insere_letra(tab, pos, c):
    tab[pos[0]-1][pos[1]-1] = c
    return tab

def ordena_letras(let):
    res = ()
    n = len(let)
    for c in ABC:
        for i in range(n):
            if let[i] == c:
                res += (c,)
    return res

def eh_jogador(jog):
    if not isinstance(jog, dict) or len(jog) != 3:
        return False
    if 'id' not in jog or 'pontos' not in jog or 'letras' not in jog:
        return False
    id = jog['id']
    if not isinstance(id, int) or id < 1:
        return False
    p = jog['pontos']
    if not isinstance(p, int) or p < 0:
        return False
    l = jog['letras']
    if not eh_conjunto(l):
        return False
    return True

###########################################################################

def cria_conjunto(let, freq):
    if not isinstance(let, tuple) or not isinstance(freq, tuple) or len(let) != len(freq):
        raise ValueError('cria_conjunto: argumentos inválidos')
    conj = {}
    for i in range(len(let)):
        if type(let[i]) != str or len(let[i]) != 1 or not let[i] in ABC or let[i] in conj:
            raise ValueError('cria_conjunto: argumentos inválidos')
        if type(freq[i]) != int or freq[i] < 1:
            raise ValueError('cria_conjunto: argumentos inválidos')
        conj[let[i]] = freq[i]
    return conj

def gera_numero_aleatorio(seed):
    seed ^= (seed << 13) & 0xFFFFFFFF
    seed ^= (seed >> 17) & 0xFFFFFFFF
    seed ^= (seed << 5) & 0xFFFFFFFF
    return seed

def permuta_letras(letras, seed):
    n = len(letras)
    for i in range(n-1, 0, -1):
        seed = gera_numero_aleatorio(seed)
        j = seed % (i+1)
        letras[i], letras[j] = letras[j], letras[i]

def baralha_conjunto(saco, seed):
    if not eh_conjunto(saco) or not isinstance(seed, int) or seed < 0 or seed > 2**64:
        raise ValueError('baralha_conjunto: argumentos inválidos')
    todas = list(conjunto_para_tuplo(saco))
    permuta_letras(todas, seed)
    return todas

def testa_palavra_padrao(palavra, padrao, letras):
    n = len(palavra)
    if n != len(padrao):
        return False
    l = letras.copy()
    for i in range(n):
        if padrao[i] == '.':
            if not retira_letra_conjunto(l, palavra[i]):
                return False
        else:
            if padrao[i] != palavra[i]:
                return False
    return True

def cria_tabuleiro():
    return [['.']*15 for _ in range(15)]

def cria_casa(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not 0 < x < 16 or not 0 < y < 16:
        raise ValueError('cria_casa: argumentos inválidos')
    return (x, y)

def obtem_valor(tab, pos):
    l = tab[pos[0]-1]
    return l[pos[1]-1]

def obtem_sequencia(tab, pos, d, n):
    res = ""
    if d == 'H':
        for k in range(n):
            res += obtem_valor(tab, (pos[0], pos[1]+k))
    if d == 'V':
        for k in range(n):
            res += obtem_valor(tab, (pos[0]+k, pos[1]))
    return res

def insere_palavra(tab, pos, d, palavra):
    i = pos[0]
    j = pos[1]
    n = len(palavra)
    if d == 'H':
        for k in range(n):
            p = (i, j+k)
            tab = insere_letra(tab, p, palavra[k])
    if d == 'V':
        for k in range(n):
            p = (i+k, j)
            tab = insere_letra(tab, p, palavra[k])
    return tab

def tabuleiro_para_str(tab):
    s = "                       1 1 1 1 1 1\n    "
    for j in range(1, 10):
        s += ' ' + str(j)
    for j in range(6):
        s += ' ' + str(j)
    s += '\n   +-'
    for j in range(15):
        s += '--'
    s += '+\n'
    for i in range(1, 10):
        s += ' ' + str(i) + ' |'
        for j in range(15):
            pos = (i, j+1)
            s += ' ' + obtem_valor(tab, pos)
        s += ' |\n'
    for i in range(10, 16):
        s += str(i) + ' |'
        for j in range(15):
            pos = (i, j+1)
            s += ' ' + obtem_valor(tab, pos)
        s += ' |\n'
    s += '   +-'
    for j in range(15):
        s += '--'
    s += '+'
    return s

def cria_jogador(n, pontos, conj):
    if not isinstance(n, int) or not 0 < n < 5 or not isinstance(pontos, int) or pontos < 0 or not isinstance(conj, dict):
        raise ValueError('cria_jogador: argumentos inválidos')
    jog = {}
    jog['id'] = n
    jog['pontos'] = pontos
    jog['letras'] = {}
    tot = 0
    for l, v in conj.items():
        if not isinstance(l, str) or l not in ABC or l in jog['letras']:
            raise ValueError('cria_jogador: argumentos inválidos')
        if not isinstance(v, int) or v < 1 or tot + v > 7:
            raise ValueError('cria_jogador: argumentos inválidos')
        jog['letras'][l] = v
        tot += v
    return jog


def jogador_para_str(jog):
    s = '#' + str(jog['id']) + ' ('
    p = jog['pontos']
    if p > 99:
        s += str(p)
    else:
        if p > 9:
            s += ' ' + str(p)
        else:
            s += '  ' + str(p)
    s += '):'
    if(len(jog['letras']) != 0):
        k = ordena_letras(conjunto_para_tuplo(jog['letras']))
        for l in k:
            s += ' ' + l
    else:
        s += ' '
    return s

def distribui_letra(letras, jog):
    if len(letras) == 0:
        return False
    l = letras.pop()
    insere_letra_conjunto(jog['letras'], l)
    return True

def joga_palavra(tab, pal, pos, d, letras, start):
    ok = eh_tabuleiro(tab)
    ok &= isinstance(pal, str) and len(pal) != 0
    ok &= eh_casa(pos)
    ok &= isinstance(d, str) and (d == 'H' or d == 'V')
    ok &= eh_conjunto(letras)
    ok &= isinstance(start, bool)
    if not ok:
        raise ValueError('joga_palavra: argumentos inválidos')
    lp = len(pal)
    # testa saída do tabuleiro
    if d == 'H' and pos[1] + lp > 16:
        return ()
    if d == 'V' and pos[0] + lp > 16:
        return ()
    if start:
        # testa centro no início
        if d == 'H':
            if pos[0] != 8 or pos[1] > 8 or pos[1] + lp < 8:
                return ()
        else:
            if pos[1] != 8 or pos[0] > 8 or pos[0] + lp < 8:
                return ()
        padrao = '.'*lp
    else:
        padrao = obtem_sequencia(tab, pos, d, lp)
        if all(c == '.' for c in padrao):
            return ()
    if testa_palavra_padrao(pal, padrao, letras):
        tab = insere_palavra(tab, pos, d, pal)
        res = ()
        for i in range(lp):
            if padrao[i] == '.':
                res += (pal[i],)
        return ordena_letras(res)
    else:
        return ()

def processa_jogada(tab, jog, saco, val, start):
    ok = eh_tabuleiro(tab) and eh_jogador(jog) and eh_conjunto(val) and isinstance(saco, list)   # falta verificar cada um dos elementos
    if not ok:
        raise ValueError('processa_jogada: argumentos inválidos')
    while True:
        msg = "Jogada J" + str(jog['id']) + ": "
        print(msg, end="", flush=True)
        while True:
            action = input()
            if len(action) != 0:
                break
        if action[0] == 'P':
            if len(action) != 1:
                continue
            return False
        if action[0] == 'T':
            t = action.split()
            if len(t) < 2 or len(saco) < 7:
                continue
            ok = True
            d = jog['letras'].copy()
            for l in t[1:]:
                if l not in ABC:
                    ok = False
                    break
                if not retira_letra_conjunto(d, l):
                    ok = False
                    break
            if not ok:
                continue
            for l in t[1:]:
                retira_letra_conjunto(jog['letras'], l)
                distribui_letra(saco, jog)
            return True
        if action[0] == 'J':
            t = action.split()
            if len(t) != 5:
                continue
            pos = (int(t[1]), int(t[2]))
            usadas = joga_palavra(tab, t[4], pos, t[3], jog['letras'], start)
            if len(usadas) != 0:
                for c in t[4]:
                    jog['pontos'] += val[c]
                for c in usadas:
                    retira_letra_conjunto(jog['letras'], c)
                    distribui_letra(saco, jog)
                return True


def scrabble(njog, saco, val, seed):
    ok = isinstance(njog, int) and njog > 1 and njog < 5
    ok &= eh_conjunto(val) and eh_conjunto(saco) and len(saco) != 0
    ok &= isinstance(seed, int) and seed > 1
    if not ok:
        raise ValueError('scrabble: argumentos inválidos')
    for l in saco:
        if l not in val:
            raise ValueError('scrabble: argumentos inválidos')
    print("Bem-vindo ao SCRABBLE.")
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    saco = baralha_conjunto(saco, seed)
    jog = ()
    for j in range(njog):
        jog += (cria_jogador(j+1, 0, {}),)
        for i in range(7):
            distribui_letra(saco, jog[j])
        print(jogador_para_str(jog[j]))
    start = True
    end = False
    passes = 0
    while not end:
        for j in range(njog):
            jogada = processa_jogada(tab, jog[j], saco, val, start)
            if not jogada:
                passes += 1
            else:
                passes = 0
            if passes == njog or len(jog[j]['letras']) == 0:
                end = True
                break
            print(tabuleiro_para_str(tab))
            for i in range(njog):
                print(jogador_para_str(jog[i]))
            start &= jog[j]['pontos'] == 0

    pontos = ()
    for j in range(njog):
        pontos += (jog[j]['pontos'],)
    return pontos
